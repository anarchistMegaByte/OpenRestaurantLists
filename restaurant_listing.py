import json 


class Restaurant:

    # Used as type tags for updating timings of a restaurant
    LUNCH = "lunch"
    BREAKFAST = "breakfast"
    DINNER = "dinner"

    file_name = "restaurant_info.json"
    update_file = "update_restaurant_info.json"
    restaurant_obj = {}
    cache_store = {}

    def __init__(self):
        pass
    
    def read_from_file(self):
        with open(self.file_name, 'r') as openfile: 
            # Reading from json file 
            self.restaurant_obj = json.load(openfile)
        return self.restaurant_obj
    
    # cache format: KEYS = 0 to 23 numbers
    # value = restaurant_id**(LUNCH|BREAKFAST|DINNER)
    def store_in_indexed_format(self):
        self.cache_store = {}
        for i in range(0,24):
            self.cache_store[str(i)] = []
        for key, value in self.restaurant_obj.items():
            for time_key, time_value in value["timings"].items():
                if time_value is not None:
                    for open_time in range(time_value["start_time"], time_value["end_time"]):
                        self.cache_store[str(open_time)].append(self.get_cache_key(key, time_key))
        print("Cache was created.")
        return self.cache_store
    
    def delete_entries_from_cache(self, restaurant_key_to_delete, start_time, end_time):
        for each_hour in range(start_time, end_time):
            self.cache_store[str(each_hour)].remove(restaurant_key_to_delete)

    def add_entries_to_cache(self, restaurant_key_to_add, start_time, end_time):
        for each_hour in range(start_time, end_time):
            self.cache_store[str(each_hour)].append(restaurant_key_to_add)

    def get_cache_key(self, restaurant_id, type_tag):
        return str(restaurant_id) + "**" + type_tag

    def remove_timings(self, restaurant_id, type_tag):
        temp_restr = self.restaurant_obj[str(restaurant_id)]
        temp_timings = None
        if type_tag in [self.LUNCH, self.BREAKFAST, self.DINNER]:
            temp_timings = temp_restr["timings"][type_tag]
        
        if temp_timings is not None:
            # deleting from cache
            self.delete_entries_from_cache( self.get_cache_key(restaurant_id, type_tag), temp_timings["start_time"], temp_timings["end_time"])
            # updating the database
            self.restaurant_obj[str(restaurant_id)]["timings"][type_tag] = None
            print("Old Values of [" + type_tag + "] removed for the restaurant " + str(temp_restr["name"]))
        else:
            print("Nothing to remove as timings are not set for this restaurant " + str(temp_restr["name"]))

    def update_timings(self, restaurant_id, type_tag, new_start_time, new_end_time):
        if new_start_time < new_end_time:
            temp_restr = self.restaurant_obj[str(restaurant_id)]
            temp_timings = temp_restr["timings"]
            if temp_timings is not None:
                # remove old entries
                self.remove_timings(restaurant_id, type_tag)
            
            # update data base
            self.restaurant_obj[str(restaurant_id)]["timings"][type_tag] = {
                "start_time": new_start_time,
                "end_time": new_end_time
            }

            # update the cache
            self.add_entries_to_cache( self.get_cache_key(restaurant_id, type_tag), new_start_time, new_end_time)
            print("Updated with new ones ", restaurant_id, type_tag, "\n")   
        else:
            print("[ERROR]: start time should be less than end time.\n")

    def get_or_create_restaurants(self, restaurant_id, name=None):
        if str(restaurant_id) not in self.restaurant_obj:
            self.restaurant_obj[str(restaurant_id)] = {
                "id": restaurant_id,
                "name": name,
                "timings": {
                    self.LUNCH: None,
                    self.BREAKFAST: None,
                    self.DINNER: None
                }
            }
        return self.restaurant_obj[str(restaurant_id)]

    def get_from_cache(self, hour_input):
        res_array = self.cache_store[str(hour_input)]
        final_res = []
        for each_res in res_array:
            if each_res.split("**")[0] not in final_res:
                final_res.append(each_res.split("**")[0])
        return final_res

    def update_resturant_timings_from_file(self):
        with open(self.update_file, 'r') as openfile: 
            # Reading from json file 
            updated_info = json.load(openfile)
            for rkey, rvalue in updated_info.items():
                print("##### Changing timings for: " + str(rkey) + "#####")
                if rvalue["operation"] == "add":
                    if "name" not in rvalue:
                        print("Skipping creation of restaurant " + str(rkey) + ". As name field is compulsory.")
                    else:
                        pass
                    self.get_or_create_restaurants(rkey, rvalue["name"])
                
                # update database and timings
                eat_type_array = [self.LUNCH, self.BREAKFAST, self.DINNER]
                for each_type, type_value in rvalue["timings"].items():
                    if each_type not in eat_type_array:
                        print("\n[ERROR] Invalid timings type. Use one of the values: " + str(eat_type_array))
                        continue
                    if type_value is not None:
                        self.update_timings(rkey, each_type, type_value["start_time"], type_value["end_time"])
                    else:
                        self.remove_timings(rkey, each_type)

        print(self.restaurant_obj)
        print(self.cache_store)   
        return self.restaurant_obj, self.cache_store

    def get_if_restaurant_exist(self, restaurant_id):
        if str(restaurant_id) in self.restaurant_obj:
            return self.restaurant_obj[str(restaurant_id)] 
        else:
            return None


if __name__=="__main__":
    r = Restaurant()
    print("\n\nFetching resturant information..\n")
    print(r.read_from_file())
    print("\n\nCreating cache..\n")
    print(r.store_in_indexed_format())
    while True:
        print("\n\nOptions:\n1. Fetch open restaurant list\n2. Update Restaurant timings\nPress -1 to exit.")
        user_input = int(input("Enter one of the options mentioned above: "))
        if user_input not in [1, 2, -1]:
            print("Invalid input try again.\n")
            continue
        else:
            if user_input == 1:
                hour_input = int(input("\n\nEnter hours for which restaurant list is needed (0-23)\nPress -1 to exit\n: "))
                if hour_input != -1:
                    open_array = r.get_from_cache(hour_input)
                    if len(open_array) == 0:
                        print("No restaurants open at this point of time. Try again later..")
                    else:
                        print("\n\n\nHere are restaurant IDS opened at " + str(hour_input) + " \n")
                        print(set(open_array))   
            
            elif user_input == 2:
                r.update_resturant_timings_from_file()
                print("\n\nupdated the database and cache with given inputs\n\n")
                            
            elif user_input == -1:
                break
            else:
                pass

