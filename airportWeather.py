import json,csv,requests
import importlib
from apikeys import *
class airportWeather:
    __airportInfo__:dict = {}
    openWeatherKeys : str = ""
    def __init__(self,airportIATACode:str,openWeatherKeys=""):
        self.openWeatherKeys = openWeatherKeys
        with open('airports.csv',newline='',errors='ignore',encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',',quotechar='"')
            title = spamreader.__next__()
            regionParamaterPosition = 0
            for i in range(len(title)):
                regionParamaterPosition = i
                if title[i]=='iso_country':
                    break
            if title[regionParamaterPosition] != 'iso_country':
                raise Exception("Error: airport file error, check/redownload it.")

            
            iataCodeParamaterPosition = 0
            for i in range(len(title)):
                iataCodeParamaterPosition = i
                if title[i]=='iata_code':
                    break
            if title[iataCodeParamaterPosition] != 'iata_code':
                raise Exception("Error: airport file error, check/redownload it.")

            for row in spamreader:
                if row[regionParamaterPosition] =='US' and row[iataCodeParamaterPosition] ==airportIATACode:
                    airportInfo:dict={}
                    airportInfo['iata_code']=row[iataCodeParamaterPosition]
                    if title[0]=='id':
                        airportInfo['id']=row[0]
                    if title[1]=='ident':
                        airportInfo['ident']=row[1]
                    if title[2]=='type':
                        airportInfo['type']=row[2]
                    if title[3]== 'name':
                        airportInfo['name']=row[3]
                    airportInfo['locate']={}
                    if title[4]=='latitude_deg':
                        airportInfo['locate']['latitude_deg'] = row[4]
                    if title[5]=='longitude_deg':
                        airportInfo['locate']['longitude_deg'] = row[5]
                    if title[6]=='elevation_ft':
                        airportInfo['locate']['elevation_ft'] = row[6]
                    if title[7]=='continent':
                        airportInfo['locate']['continent'] = row[7]
                    airportInfo['locate']['iso_country'] = row[regionParamaterPosition]
                    if title[9]=='iso_region':
                        airportInfo['locate']['iso_region'] = row[9]
                    if title[10]=='municipality':
                        airportInfo['locate']['municipality'] = row[10]
                    if title[11]== 'scheduled_service':
                        airportInfo['scheduled_service']=row[11]
                    if title[12]== 'gps_code':
                        airportInfo['gps_code']=row[12]
                    if title[14]=='local_code':
                        airportInfo['local_code']=row[14]
                    airportInfo['internet_info']={}
                    if title[15]=='home_link':
                        airportInfo['internet_info']['home_link']=row[15]
                    if title[16]=='wikipedia_link':
                        airportInfo['internet_info']['wikipedia_link']=row[16]
                    if title[17]=='keywords':
                        airportInfo['internet_info']['keywords']=str(row[17]).split()
                    self.__airportInfo__ = airportInfo
                    return
            
            raise Exception("Error: No airport found!")
        pass
    def GetAirportInfo(self) -> str:
        return json.dumps(self.__airportInfo__)
    pass
    def GetCurrentWeather(self) ->str:
        try:
            response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+ str(self.__airportInfo__["locate"]['latitude_deg']) +"&lon=" + str(self.__airportInfo__["locate"]['longitude_deg']) +"&appid=" +  self.openWeatherKeys )
        except:
            raise Exception("Error: Internet Connection failed")
        if(response.status_code==200):
            try:
                response = response.json()
                result :dict= {}
                result["air"]=response["main"]
                result["air"].pop("feels_like")
                result["clouds"]=response["clouds"]["all"]
                result["weather"]=response["weather"][0]
                result["wind"]=response["wind"]
                result["sun"]={}
                result["sun"]["sunrise"]=response["sys"]["sunrise"]
                result["sun"]["sunset"]=response["sys"]["sunset"]
                result["timeStamp"] = response["dt"]
                return json.dumps(result)
            except :
                raise Exception("Error: api decoding failed, try to get the latest version of this library")
            #printresponse[""]
        else:
            raise Exception("Error:  OpenWeather API Quest Failed")
        pass
    def GetForcast(self) ->str:
        try:
            response = requests.get("https://api.weather.gov/points/" + str(self.__airportInfo__["locate"]['latitude_deg']) + "," + str(self.__airportInfo__["locate"]['longitude_deg']))
            response = response.json()
            response = requests.get(response["properties"]["forecast"]).json()
            return json.dumps(response["properties"]["periods"])
        except :
            raise Exception("Error: api decoding failed, try to get the latest version of this library")
        pass
    def GetForcastHourly(self,hours:int=6) ->str:
        try:
            response = requests.get("https://api.weather.gov/points/" + str(self.__airportInfo__["locate"]['latitude_deg']) + "," + str(self.__airportInfo__["locate"]['longitude_deg']))
            response = response.json()
            response = requests.get(response["properties"]["forecast"] + "/hourly").json()
            return json.dumps(response["properties"]["periods"][0:hours])
        except :
            raise Exception("Error: api decoding failed, try to get the latest version of this library")
        pass
    def GetHistoricalWeather(self) ->str:
        pass

if __name__ == '__main__':
    apw = airportWeather("ORD",openWeatherKeys=openWeatherKeys)
    #print(apw.GetAirportInfo())
    #print(apw.GetCurrentWeather())
    #print(apw.GetForcast())
    print(apw.GetForcastHourly(2))