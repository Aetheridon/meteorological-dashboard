'''Templated data to test out the dashboard whilst aircraft is worked on.'''

import json

from datetime import date

from values import Values

CURRENT_DATE = date.today().strftime("%Y-%m-%d")
LOG_PATH = Values().log_file_path

def get_data_from_sensors():
    return { # Hard fixed temp data for testing.
        CURRENT_DATE: {
            "air_temp": 20,
            "air_pressure": 1006,
            "humidity": 27.66
        }
    }

def write_to_log():
    current_data = get_data_from_sensors()

    with open(LOG_PATH, "r+") as data_file:
        existing_data = json.load(data_file)

    current_data.update(existing_data)

    with open(LOG_PATH, "w+") as data_file:
        json.dump(current_data, data_file, indent=4)

write_to_log()