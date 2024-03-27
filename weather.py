from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
#FUNCTION FOR BUTTON "DABAO DABAO"
def fb():
   fun_but.config(text="KIS JAGAH KA TAPMAN JANNA HE APKO! (@_@)",bg="#517470",fg="white",font=("Calibre",11))
#DECLARING THE API FOR THE CODE
def get_weather_data(city_name):
    api_key = "6f406b3886a4e20eeed593dfe1751db1" #api is disabled add your's hehe
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for non-200 status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def show_weather():
    city_name = com.get()
    weather_data = get_weather_data(city_name)

    if weather_data:
        city = weather_data["name"]
        main_data = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        density = main_data["humidity"]
        wea_label.config(text=f"WEATHER: {weather_desc}  \n TEMPERATURE: {temperature}°C  \n PRESSURE: {pressure} hPa \nDENSITY: {density}%")
    else:
        messagebox.showerror("Error", "Invalid city name or API error.")

# CREATE MAIN WINDOW
win = Tk()
win.title("WEATHER APP")
win.config(bg="#AAA2B1")

# 1ST LABEL DECLARING
name_label = Label(win, text="PADHARO MHARE DESH!! (>.<) ", font=("Georgia", 20), bg="#201133", fg="white")
name_label.place(x=500, y=50, height=50, width=500)

# 1ST BUTTON DECLARING
fun_but = Button(win, text="PRESS IT! (+.+)", command=fb, bg="#517470", fg="white", font=("Calibre", 11))
fun_but.place(x=569, y=120, height=50, width=350)

# BOX TO CHOOSE STATES
list_of_states = ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
                  "Chandigarh", "Chhattisgarh", "Dadra and Nagar Haveli", "Daman and Diu", "Delhi", "Goa",
                  "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka",
                  "Kerala", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
                  "Nagaland", "National Capital Territory of Delhi", "Odisha", "Puducherry", "Punjab", "Rajasthan",
                  "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
                  "Ahmedabad", "Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai"]
citynm = StringVar(win)
com = ttk.Combobox(win, values=list_of_states, font=("Century Gothic", 15))
com.set("CHOOSE YOUR CITY")
com.place(x=500, y=200, height=50, width=500)

# DONE BUTTON DECLARING
done_but = Button(win, text="CHALO CHALO HO GYA (~.~) !", font=("Calibre", 10), command=win.destroy)
done_but.place(x=625, y=725, height=30, width=250)

# BUTTON TO SHOW WEATHER
wea_but = Button(win, text="SHOW WEATHER ($_$)", font=("Calibre", 10), bg="#75B39C", fg="black", command=show_weather)
wea_but.place(x=635, y=295, height=50, width=200)

# LABEL FOR SHOWING WEATHER
wea_label = Label(win, text="", font=("Georgia", 18), bg="#201133", fg="white")
wea_label.place(x=395, y=355, height=325, width=700)

win.mainloop()

