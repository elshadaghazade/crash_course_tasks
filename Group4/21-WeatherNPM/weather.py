# Here we include the weather-api so we can use it in our Python application.
from weather import Weather, Unit

# Then we use the module to search for the weather at a location
weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('Anchorage, AK')
condition = location.condition
print(condition.text)
