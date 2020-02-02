# api-design-PupilTong
api-design-PupilTong created by GitHub Classroom

## Preparation
download essential files
```bash
git clone https://github.com/BUEC500C1/api-design-PupilTong.git
```
Import to your codes
```python
import airportWeather
```
## instructions
### Initilization Object
```python
apw = airportWeather("BOS")
#Set the airpot as boston logan international airport
```

### Get airports Information
```python
airportWeather("BOS").GetAirportInfo()
```
The return of this method will be a json string, like this
```json
{"iata_code": "BOS", "id": "3422", "ident": "KBOS", "type": "large_airport", "name": "General Edward Lawrence Logan International Airport", "locate": {"latitude_deg": "42.36429977", "longitude_deg": "-71.00520325", "elevation_ft": "20", "continent": "NA", "iso_country": "US", "iso_region": "US-MA", "municipality": "Boston"}, "scheduled_service": "yes", "gps_code": "KBOS", "local_code": "BOS", "internet_info": {"home_link": "http://www.massport.com/logan/", "wikipedia_link": "https://en.wikipedia.org/wiki/Logan_International_Airport", "keywords": ["General", "Edward", "Lawrence", "Logan", "International", "Airport"]}}
```
