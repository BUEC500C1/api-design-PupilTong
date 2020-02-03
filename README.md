# api-design-PupilTong
api-design-PupilTong created by GitHub Classroom

## Preparation
### download essential files
```bash
git clone https://github.com/BUEC500C1/api-design-PupilTong.git
```
Import to your codes
```python
import airportWeather
```
### register an API key of Open Weather
check https://openweathermap.org/ for more infomation

## instructions
### Initilization Object
```python
apw = airportWeather("BOS")
#Set the airpot as boston logan international airport
```

#### Object Initilization parameter

airportIATACode : String. Set the airport.

openWeatherKeys : String. Your own openweather key.
### Get airports Information
```python
airportWeather("BOS").GetAirportInfo()
```
The return of this method will be a json string, like this
```json
{"iata_code": "BOS", "id": "3422", "ident": "KBOS", "type": "large_airport", "name": "General Edward Lawrence Logan International Airport", "locate": {"latitude_deg": "42.36429977", "longitude_deg": "-71.00520325", "elevation_ft": "20", "continent": "NA", "iso_country": "US", "iso_region": "US-MA", "municipality": "Boston"}, "scheduled_service": "yes", "gps_code": "KBOS", "local_code": "BOS", "internet_info": {"home_link": "http://www.massport.com/logan/", "wikipedia_link": "https://en.wikipedia.org/wiki/Logan_International_Airport", "keywords": ["General", "Edward", "Lawrence", "Logan", "International", "Airport"]}}
```
### Get current weather
Get current weather of the airport.
```python
airportWeather("ORD",openWeatherKeys=openWeatherKeys).GetCurrentWeather()
```
The return of this method will be a json string, like this
```json
{"air": {"temp": 277.16, "temp_min": 274.82, "temp_max": 279.26, "pressure": 1006, "humidity": 93}, "clouds": 1, "weather": {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}, "wind": {"speed": 1.5, "deg": 260}, "sun": {"sunrise": 1580648629, "sunset": 1580684797}, "timeStamp": 1580697870}
```
#### Parameters
| Name  | Description | Unit |
| ------------- | ------------- | ------------- |
| temp  | Temperature  | Kelvin  |
| temp_min  | Minimum temperature at the moment.  | Kelvin  |
| temp_max  | Maximum temperature at the moment.  | Kelvin  |
| pressure  | Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data)  | hPa  |
| humidity  | humidity  | %  |
| clouds  | Cloudiness  | %  |
| sunrise  |  Sunrise time | unix, UTC  |
| sunset  | Sunset time  | unix, UTC  |
| timeStamp  |  | unix, UTC  |
| speed  | wind speed | meter/sec |
