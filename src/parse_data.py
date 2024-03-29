import json

from values import Values
from load_data import write_to_log

import matplotlib.pyplot as plt

def get_logs():
    with open(Values().log_file_path, "r+") as data_file:
        return json.load(data_file)

def plot_data(dates, title, measurement, filename):
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.plot(dates, measurement, color="c")

    fig.savefig(f"static/pics/{filename}.png")
    plt.show()


def parse_data():
    write_to_log()
    data_to_plot = get_logs()

    dates = list(data_to_plot.keys())
    measurements = ["air_temp", "air_pressure", "humidity"]
    titles = ["Air Temperature (°C)", "Air Pressure (hPa)", "Humidity (%)"]

    air_temp_measurements = [data_to_plot[date]["air_temp"] for date in dates]
    air_pressure_measurements = [data_to_plot[date]["air_pressure"] for date in dates]
    humidity_measurements = [data_to_plot[date]["humidity"] for date in dates]

    measurement_values = [air_temp_measurements, air_pressure_measurements, humidity_measurements]
    
    for index, title in enumerate(titles):
        plot_data(dates=dates, title=title, measurement=measurement_values[index], filename=measurements[index])

