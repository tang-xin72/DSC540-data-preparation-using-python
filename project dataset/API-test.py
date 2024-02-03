AppID = 'ec83f46dfbe12662beeee4a7ae75a168'
BaseGeoURL = 'http://api.openweathermap.org/geo/1.0/direct?q='
BaseURL = 'http://api.openweathermap.org/data/2.5/weather?q='
BaseUrl_by_zip = 'https://api.openweathermap.org/data/2.5/weather?zip='
UrlGeoCheck = 'https://api.openweathermap.org/data/2.5/weather?lat='

import requests
City = "austin"
State = "TX"
Country = "us"

FullURL = BaseGeoURL + City + ',' + State + ',' + Country + '&appid=' + AppID
print(FullURL)
ApiData = requests.get(FullURL)
#ApiData = requests.get(   'http://api.openweathermap.org/geo/1.0/direct?q=austin,TX,US&limit=5&appid=ec83f46dfbe12662beeee4a7ae75a168')

ReturnedData = ApiData.json()

Lat = str(ReturnedData[0]['lat'])
Lon = str(ReturnedData[0]['lon'])



Test = UrlGeoCheck + Lat + '&lon=' + Lon + '&appid=' + AppID 
#Test = 'https://api.openweathermap.org/data/2.5/weather?lat=77.22&lon=28.7&appid=ec83f46dfbe12662beeee4a7ae75a168'
#print(Test)
ApiAgain = requests.get(Test)
Data = ApiAgain.json()
#print(ReturnedInfo)
Temp = (Data['main']['temp'])-273.15
Humidity = Data['main']['humidity']
Description = Data['weather'][0]['description']
print(Temp)
print(Humidity)
print(Data['wind']['speed'])
print(Description)


