from tkinter import *
import requests, json
from tkinter import ttk

root = Tk()

 
 

def weather():
    api_key = "c933ed56e8ebf0eef5dece823984a0c8"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #city_name = input("Enter city name : ")
    city_name = scity_name.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    print(complete_url)
    response = requests.get(complete_url)
    data = response.json()
    print("------------------")
    print("Json Data")
    print(data)
    print("----------------")
    if data["cod"] != "404":
        record = data["main"]
        current_temperature = record["temp"]
        temp_degree = int(current_temperature -273.15)
        feel_temperature = record["feels_like"]
        feel_degree = int(feel_temperature -273.15)
        current_pressure = record["pressure"]
        current_humidiy = record["humidity"]
        record1 = data["weather"]
        weather_description = record1[0]["description"]
        print(" Temperature (in kelvin unit) = ",current_temperature)
        print(" Temperature (in Degree) = " +
					str(temp_degree) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description))
    else:
        print(" City Not Found ")
        
    cityname = Label(root, text="Temperature in °C in " + city_name + " is : ")
    cityname.place(x=10,y=200)
    
    label = Label(root, text=temp_degree)
    label.place(x=400,y=200)

    cityweather = Label(root, text="Skies seems to be with :")
    cityweather.place(x=10,y=250)

    citycloud = Label(root, text=weather_description)
    citycloud.place(x=400,y=250)

    cityhumid = Label(root, text="Humidity in percentage :")
    cityhumid.place(x=10,y=300)

    citycloud = Label(root, text=current_humidiy)
    citycloud.place(x=400,y=300)

    feel = Label(root, text="Feel like Temperature in °C in ")
    feel.place(x=10,y=350)

    feellike = Label(root, text=feel_degree)
    feellike.place(x=400,y=350)
    
 
    
root.geometry("600x400")
root.title('Weather App')
root.configure(bg="light blue")

scity_name = StringVar()
selected= StringVar()


lblHeading = Label(root,text='Weather Info ',bg="light blue",font=('Impact',20))
lblHeading.place(x=250,y=10)

lblValue1 = Label(root,text='Enter City Name   ')
lblValue1.place(x=10,y=70)

txtValue1 = Entry(root,textvariable = scity_name)
txtValue1.place(x=150,y=70)


btnAdd = Button(root,text='Get weather',command = weather)
btnAdd.place(x=300,y=70)

 

root.mainloop()
