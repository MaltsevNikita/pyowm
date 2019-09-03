import pyowm

owm = pyowm.OWM('0fb6abd182fa3df4608f1eabacf82ff6' )  # You MUST provide a valid API key


observation = owm.weather_at_place('Volgograd,ru')

w = observation.get_weather()

# 0fb6abd182fa3df4608f1eabacf82ff6

temperature = w.get_temperature('celsius')['temp']

print("Температура:")
print(str(temperature)+" Градусов Цельсия")
print("Влажность: ")
print(str(w.get_humidity()) + "%")
