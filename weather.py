import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data=np.array([['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],
      [30,20,45,35,25,19,35],# temperature , average ()
      ['50%','69%','60%','40%','65%','76%','75%'],#humidity max ,min
      ['10km/h','15km/h','27km/h','9km/h','13km/h','20km/h','30km/h']])# speed of wind if 20km
days=data[0]
temperature_data = data[1].astype(float)
temperature_avg=np.mean (temperature_data)
print(f'The average temperature is {temperature_avg}')# average temperature
humidity_data =np.array([float(value.strip('%'))for value in  data[2]])
maximum_humidity=np.max(humidity_data)
# print(f'the maximum value is {maximum_humidity}%')
minimum_humidity=np.min(humidity_data)
# print(f'the maximum value is {minimum_humidity}%')
max_index=np.argmax(humidity_data)
min_index=np.argmin(humidity_data)
max_day=data[0][max_index]
min_day=data[0][min_index]
print(f' The maximum humidity on {max_day} is {maximum_humidity}')
print(f'The minimum humidity is {min_day} is {minimum_humidity}')
wind_speed=np.array([float(speed.strip('km/h'))for speed in data[3]])
high_speed_index=np.where(wind_speed>20)[0]
print(high_speed_index)
high_speed_days=np.array([ data[0][i] for i in high_speed_index])
high_speed_values=[wind_speed[i] for i in high_speed_index]
for day,speed in zip(high_speed_days,high_speed_values):
    print(f'Wind speed on {day} is {speed}km/h ')


fig, axes = plt.subplots(3, 1, figsize=(10, 6))

# Temperature
sns.barplot(ax=axes[0], x=days, y=temperature_data)
axes[0].set_title("Temperature Throughout the Week", fontsize=12)
axes[0].set_ylabel("Temperature (°C)", fontsize=12)

# Humidity
sns.lineplot(ax=axes[1], x=days, y=humidity_data, marker="o", color="blue")
axes[1].set_title("Humidity Levels Throughout the Week", fontsize=12)
axes[1].set_ylabel("Humidity (%)", fontsize=12)

# Wind Speed
sns.scatterplot(ax=axes[2], x=days, y=wind_speed, color="green", s=100, label="Wind Speed")
axes[2].scatter(high_speed_days, high_speed_values, color="red", s=150, label=">20 km/h")
axes[2].set_title("Wind Speeds Throughout the Week", fontsize=12)
axes[2].set_ylabel("Wind Speed (km/h)", fontsize=12)
axes[2].legend()

plt.tight_layout()
plt.show()

    