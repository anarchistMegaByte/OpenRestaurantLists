## Files and their information:

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

## Instructions for running the this script.

```
1. Clone this repository
2. Execute the file
>> python restaurant_listing.py
```
