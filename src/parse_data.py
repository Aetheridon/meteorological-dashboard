import json

from values import Values

import matplotlib.pyplot as plt

def get_logs():
    with open(Values().log_file_path, "r+") as data_file:
        return json.load(data_file)

def plot_data(dates, title, measurement, filename):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.plot(dates, measurement, color="green")

    fig.savefig(f"{filename}.png")
    plt.show()

def parse_data(data_to_plot):
    dates = list(data_to_plot.keys())
    measurements = ["air_temp", "air_pressure", "humidity"]
    titles = ["Air Temperature (°C)", "Air Pressure (hPa)", "Humidity (%)"]

    air_temp_measurements = [data_to_plot[date]["air_temp"] for date in dates]
    air_pressure_measurements = [data_to_plot[date]["air_pressure"] for date in dates]
    humidity_measurements = [data_to_plot[date]["humidity"] for date in dates]

    measurement_values = [air_temp_measurements, air_pressure_measurements, humidity_measurements]
    
    for index, title in enumerate(titles):
        plot_data(dates=dates, title=title, measurement=measurement_values[index], filename=measurements[index])
    
data_to_plot = get_logs()
parse_data(data_to_plot=data_to_plot)