```
Fetching resturant information..

{'1': {'id': 1, 'name': '1abc', 'timings': {'breakfast': {'start_time': 8, 'end_time': 11}, 'lunch': {'start_time': 14, 'end_time': 18}, 'dinner': {'start_time': 19, 'end_time': 22}}}, '2': {'id': 2, 'name': '2abc', 'timings': {'breakfast': {'start_time': 8, 'end_time': 12}, 'lunch': {'start_time': 11, 'end_time': 18}, 'dinner': None}}, '3': {'id': 3, 'name': '3abc', 'timings': {'breakfast': {'start_time': 8, 'end_time': 17}, 'lunch': None, 'dinner': None}}}


Creating cache..

Cache was created.
{'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': ['1**breakfast', '2**breakfast', '3**breakfast'], '9': ['1**breakfast', '2**breakfast', '3**breakfast'], '10': ['1**breakfast', '2**breakfast', '3**breakfast'], '11': ['2**breakfast', '2**lunch', '3**breakfast'], '12': ['2**lunch', '3**breakfast'], '13': ['2**lunch', '3**breakfast'], '14': ['1**lunch', '2**lunch', '3**breakfast'], '15': ['1**lunch', '2**lunch', '3**breakfast'], '16': ['1**lunch', '2**lunch', '3**breakfast'], '17': ['1**lunch', '2**lunch'], '18': [], '19': ['1**dinner'], '20': ['1**dinner'], '21': ['1**dinner'], '22': [], '23': []}


Options:
1. Fetch open restaurant list
2. Update Restaurant timings
Press -1 to exit.
Enter one of the options mentioned above: 1


Enter hours for which restaurant list is needed (0-23)
Press -1 to exit
: 2
No restaurants open at this point of time. Try again later..


Options:
1. Fetch open restaurant list
2. Update Restaurant timings
Press -1 to exit.
Enter one of the options mentioned above: 1


Enter hours for which restaurant list is needed (0-23)
Press -1 to exit
: 22
No restaurants open at this point of time. Try again later..


Options:
1. Fetch open restaurant list
2. Update Restaurant timings
Press -1 to exit.
Enter one of the options mentioned above: 2
##### Changing timings for: 1#####
Old Values of [breakfast] removed for the restaurant 1abc
Updated with new ones  1 breakfast 

Old Values of [lunch] removed for the restaurant 1abc
Updated with new ones  1 lunch 

##### Changing timings for: 2#####
Old Values of [breakfast] removed for the restaurant 2abc
Updated with new ones  2 breakfast 

Old Values of [lunch] removed for the restaurant 2abc
Updated with new ones  2 lunch 

Nothing to remove as timings are not set for this restaurant 2abc
Updated with new ones  2 dinner 

{'1': {'id': 1, 'name': '1abc', 'timings': {'breakfast': {'start_time': 8, 'end_time': 11}, 'lunch': {'start_time': 14, 'end_time': 18}, 'dinner': {'start_time': 19, 'end_time': 22}}}, '2': {'id': 2, 'name': '2abc', 'timings': {'breakfast': {'start_time': 6, 'end_time': 8}, 'lunch': {'start_time': 14, 'end_time': 16}, 'dinner': {'start_time': 20, 'end_time': 22}}}, '3': {'id': 3, 'name': '3abc', 'timings': {'breakfast': {'start_time': 8, 'end_time': 17}, 'lunch': None, 'dinner': None}}}
{'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': ['2**breakfast'], '7': ['2**breakfast'], '8': ['3**breakfast', '1**breakfast'], '9': ['3**breakfast', '1**breakfast'], '10': ['3**breakfast', '1**breakfast'], '11': ['3**breakfast'], '12': ['3**breakfast'], '13': ['3**breakfast'], '14': ['3**breakfast', '1**lunch', '2**lunch'], '15': ['3**breakfast', '1**lunch', '2**lunch'], '16': ['3**breakfast', '1**lunch'], '17': ['1**lunch'], '18': [], '19': ['1**dinner'], '20': ['1**dinner', '2**dinner'], '21': ['1**dinner', '2**dinner'], '22': [], '23': []}


updated the database and cache with given inputs


Options:
1. Fetch open restaurant list
2. Update Restaurant timings
Press -1 to exit.
Enter one of the options mentioned above: 1


Enter hours for which restaurant list is needed (0-23)
Press -1 to exit
: 20



Here are restaurant IDS opened at 20 

{'1', '2'}


Options:
1. Fetch open restaurant list
2. Update Restaurant timings
Press -1 to exit.
Enter one of the options mentioned above: -1
