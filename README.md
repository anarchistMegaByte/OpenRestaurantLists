## Files and their information:

#### NOTE: Generic json file parent structure
```json
{
    "restaurant_id": json_obj,
    "restaurant_id": json_obj
    ...
}
```

`json_obj`

```json
{
    "operation": "add/update", // only required when you are using update_resturant_info.json
    "id": restaurant_id,
    "name": restaurant_name, # is compusory field in case of "add" operation.
    "timings": {
        "lunch": time_obj,
        "breakfast" : time_obj,
        "dinner": time_obj
     }
}
```

#### 1. `restaurant_info.json`:
This is the base file for initalizing database with restaurant information for open hours. It has json for format:

```json
{
    "1": {
        "id": 1,
        "name": "1abc",
        "timings": {
            "breakfast": {
                "start_time": 8,
                "end_time": 11
            },
            "lunch": {
                "start_time": 14,
                "end_time": 18
            },
            "dinner": {
                "start_time": 19,
                "end_time": 22
            }
        }
    },
    "2": {
        "id": 2,
        "name": "2abc",
        "timings": {
            "breakfast": {
                "start_time": 8,
                "end_time": 12
            },
            "lunch": {
                "start_time": 11,
                "end_time": 18
            },
            "dinner": null
        }
    },..
}
```

#### 2. `update_restaurant_info.json`:
This file is to be used for updating the timings of restaurants. Do not change the name of the file as it is written inside the code.
There are two variations of json in this file:

##### i. Adding new restaurants: `name` field is compulsory while having `operation` as `add`

```json
"4": {
        "operation": "add",
        "id": 4,
        "name": "4ghi",
        "timings": {
            "breakfast": null,
            "dinner": {
                "start_time": 15,
                "end_time": 22
            }
        }
    }
```

##### ii. Updating timings of existing restaurants: Only put timings for either lunch, breakfast or dinner (all are not compulsory)

```json
"1": {
        "operation": "update",
        "id": 1,
        "timings": {
            "breakfast": {
                "start_time": 8,
                "end_time": 11
            },
            "lunch": {
                "start_time": 14,
                "end_time": 18
            }
        }
    }
 ```

###### iii. Remove particular hours from timings. Put `null` as value if you want to remove a particualar timings.

```json
"2": {
        "operation": "update",
        "id": 2,
        "timings": {
            "breakfast": {
                "start_time": 6,
                "end_time": 8
            },
            "lunch": {
                "start_time": 14,
                "end_time": 16
            },
            "dinner": null
        }
    }
```
In the above example the timings for dinner will be removed from restaurants opening hours.



## Instructions for running the this script.

```
1. Clone this repository
2. Execute the file
>> python restaurant_listing.py
```
