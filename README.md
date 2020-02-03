# api-design-PupilTong
api-design-PupilTong created by GitHub Classroom
## User Stories
As a developer, I may implement an RSS on my website to privides user weather information.
## Preparation
### download essential files
```bash
git clone https://github.com/datasets/airport-codes.git
git clone https://github.com/BUEC500C1/api-design-PupilTong.git
```
Import to your codes
```python
import airportWeather
```
### register & get an API key of Open Weather
check https://openweathermap.org/ for more infomation

## instructions
### Initilization Object
```python
apw = airportWeather("BOS")
#Set the airpot as boston logan international airport
```

#### Object Initilization parameter

* **airportIATACode** : String. Set the airport.

* **openWeatherKeys** : String. Your own openweather key.
### Get airports Information
```python
airportWeather("BOS").GetAirportInfo()
```
The return of this method will be a json string, like this
```json
{
	"iata_code": "BOS",
	"id": "3422",
	"ident": "KBOS",
	"type": "large_airport",
	"name": "General Edward Lawrence Logan International Airport",
	"locate": {
		"latitude_deg": "42.36429977",
		"longitude_deg": "-71.00520325",
		"elevation_ft": "20",
		"continent": "NA",
		"iso_country": "US",
		"iso_region": "US-MA",
		"municipality": "Boston"
	},
	"scheduled_service": "yes",
	"gps_code": "KBOS",
	"local_code": "BOS",
	"internet_info": {
		"home_link": "http://www.massport.com/logan/",
		"wikipedia_link": "https://en.wikipedia.org/wiki/Logan_International_Airport",
		"keywords": ["General", "Edward", "Lawrence", "Logan", "International", "Airport"]
	}
}
```
### Get current weather
Get current weather of the airport. Data comes form open weather api.
```python
airportWeather("ORD",openWeatherKeys=openWeatherKeys).GetCurrentWeather()
```
The return of this method will be a json string, like this
```json
{
	"air": {
		"temp": 277.16,
		"temp_min": 274.82,
		"temp_max": 279.26,
		"pressure": 1006,
		"humidity": 93
	},
	"clouds": 1,
	"weather": {
		"id": 800,
		"main": "Clear",
		"description": "clear sky",
		"icon": "01n"
	},
	"wind": {
		"speed": 1.5,
		"deg": 260
	},
	"sun": {
		"sunrise": 1580648629,
		"sunset": 1580684797
	},
	"timeStamp": 1580697870
}
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

### Get weather forecast
Get weather forecast of the airport. Data comes form https://api.weather.gov/.
```python
airportWeather("ORD").GetForcast()
```
The return of this method will be a json string, like this
```json
[{
	"number": 1,
	"name": "Tonight",
	"startTime": "2020-02-02T21:00:00-05:00",
	"endTime": "2020-02-03T06:00:00-05:00",
	"isDaytime": false,
	"temperature": 34,
	"temperatureUnit": "F",
	"temperatureTrend": null,
	"windSpeed": "8 mph",
	"windDirection": "W",
	"icon": "https://api.weather.gov/icons/land/night/bkn?size=medium",
	"shortForecast": "Mostly Cloudy",
	"detailedForecast": "Mostly cloudy, with a low around 34. West wind around 8 mph."
}]
```
### Get hourly weather forecast
Get weather forecast of the airport. Data comes form https://api.weather.gov/.
```python
airportWeather("ORD").GetForcast(2)
```
The return of this method will be a json string, like this
```json
[{
	"number": 1,
	"name": "",
	"startTime": "2020-02-02T23:00:00-06:00",
	"endTime": "2020-02-03T00:00:00-06:00",
	"isDaytime": false,
	"temperature": 36,
	"temperatureUnit": "F",
	"temperatureTrend": null,
	"windSpeed": "5 mph",
	"windDirection": "WNW",
	"icon": "https://api.weather.gov/icons/land/night/few?size=small",
	"shortForecast": "Mostly Clear",
	"detailedForecast": ""
}, {
	"number": 2,
	"name": "",
	"startTime": "2020-02-03T00:00:00-06:00",
	"endTime": "2020-02-03T01:00:00-06:00",
	"isDaytime": false,
	"temperature": 35,
	"temperatureUnit": "F",
	"temperatureTrend": null,
	"windSpeed": "5 mph",
	"windDirection": "NW",
	"icon": "https://api.weather.gov/icons/land/night/few?size=small",
	"shortForecast": "Mostly Clear",
	"detailedForecast": ""
}]
```
#### Method parameter

* **hours** : integer. How many hourly weather forcast from now you want to get.
### Get historical weather
Get historical weather of the airport. Data comes form https://api.weather.gov/.
```python
airportWeather("ORD").GetHistoricalWeather("2020-02-01T23:00:00-06:00","2020-02-02T23:00:00-06:00",2)
#Get weather information form 2020-02-01T23:00:00 to 2020-02-02T23:00:00 and set 2 as the maxium data count.
```
The return of this method will be a json string, like this
```json
[{
	"number": 1,
	"name": "",
	"startTime": "2020-02-03T04:55:00+00:00",
	"endTime": "2020-02-03T04:55:00+00:00",
	"timestamp": "2020-02-03T04:55:00+00:00",
	"temperature": 2.2000000000000455,
	"temperatureUnit": "unit:degC",
	"windSpeed": "1.5 mph",
	"windDirection": 270,
	"windDirectionUnit": "unit:degree_(angle)",
	"icon": "https://api.weather.gov/icons/land/night/skc?size=medium"
}, {
	"number": 2,
	"name": "",
	"startTime": "2020-02-03T04:53:00+00:00",
	"endTime": "2020-02-03T04:53:00+00:00",
	"timestamp": "2020-02-03T04:53:00+00:00",
	"temperature": 2.2000000000000455,
	"temperatureUnit": "unit:degC",
	"windSpeed": "3.1 mph",
	"windDirection": 260,
	"windDirectionUnit": "unit:degree_(angle)",
	"icon": "https://api.weather.gov/icons/land/night/skc?size=medium"
}]
```
#### Method parameter

* **startTime** : String. Start time. YYYY-MM-DD'T'hh:mmTZD. Check ISO8601 for more info.
* **Endtime** : String. End time. YYYY-MM-DD'T'hh:mmTZD. Check ISO8601 for more info.
* **limit** : integer. How many historical weather data from now you want to get. The number of data may less than your setting.
