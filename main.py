import requests

api_key = "567b3b033941413ffdd9c3cdf293ed94"
base_url = "https://api.openweathermap.org/data/2.5/weather"


city = input("Enter City Name: ")
print("")

url = f"{base_url}?q={city}&appid={api_key}"

r = requests.get(url)
if (r.status_code==200):
	data = r.json() 	#Getting response data in json

	weather = data['weather'][0]['description']   #Grabing weather from the response json
	print("The Current Weather for " +city + " is "+ weather)
	
	temp = data['main']['temp']                   #Grabing temprature from the response json
	print("The Current Temprature in Celcius is " +str(round(temp-273.15,2)))


else:
	print("We are sorry! An Error Occurred")
