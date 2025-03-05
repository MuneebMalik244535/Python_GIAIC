import requests
def Weather_App(city):
     BASE_URL = f"https://wttr.in/{city}?format=%C+%t"  # noqa: F821
     try:
         response = requests.get(BASE_URL)
         if response.status_code == 200:
             print (f"\n🌦️ Weather in {city}: {response.text}")
         else :
             print("\n❌ Network Error! Please check your internet connection.")
     except requests.Exception.RequestException:
         print("\n❌ Network Error! Please check your internet connection.")
             

city_name = input("Enter Your city Name : ")
Weather_App(city_name)                  
        