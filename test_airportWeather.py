from airportWeather import *
from apikeys import *
import pytest
def test_airportInfo():
    assert airportWeather("BOS").GetAirportInfo() == """{"iata_code": "BOS", "id": "3422", "ident": "KBOS", "type": "large_airport", "name": "General Edward Lawrence Logan International Airport", "locate": {"latitude_deg": "42.36429977", "longitude_deg": "-71.00520325", "elevation_ft": "20", "continent": "NA", "iso_country": "US", "iso_region": "US-MA", "municipality": "Boston"}, "scheduled_service": "yes", "gps_code": "KBOS", "local_code": "BOS", "internet_info": {"home_link": "http://www.massport.com/logan/", "wikipedia_link": "https://en.wikipedia.org/wiki/Logan_International_Airport", "keywords": ["General", "Edward", "Lawrence", "Logan", "International", "Airport"]}}"""
    with pytest.raises(Exception):
        assert(airportWeather("PKX"))
        assert(airportWeather(""))
    
def test_CurrentWeather():
    #assert type(airportWeather("ORD",openWeatherKeys=openWeatherKeys).GetCurrentWeather())==type("string")
    with pytest.raises(Exception):
        assert(airportWeather("ORD").GetCurrentWeather())
def test_GetForcast():
    assert type(airportWeather("ORD").GetForcast())==type("string")
    with pytest.raises(Exception):
        assert(airportWeather("PKX").GetForcast())
def test_GetForcastHourly():
    assert type(airportWeather("ORD").GetForcastHourly())==type("string")
    assert len(json.loads(airportWeather("ORD").GetForcastHourly(2)))==2
    with pytest.raises(Exception):
        assert(airportWeather("PKX").GetForcastHourly())
def test_GetHistoricalWeather():
    assert type(airportWeather("ORD").GetHistoricalWeather("2020-02-01T23:00:00-06:00","2020-02-02T23:00:00-06:00",2))==type("string")
    assert len(json.loads(airportWeather("ORD").GetHistoricalWeather("2020-02-01T23:00:00-06:00","2020-02-02T23:00:00-06:00",2)))==2
    with pytest.raises(Exception):
        assert(airportWeather("PKX").GetForcastHourly())
        assert(airportWeather("ORD").GetHistoricalWeather("","",2))
        assert(airportWeather("ORD").GetHistoricalWeather())