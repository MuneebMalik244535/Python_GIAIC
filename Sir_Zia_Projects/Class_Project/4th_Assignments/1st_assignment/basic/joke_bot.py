import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # ✅ Agar error aaye to handle karega
        data = response.json()
        return f"😂 {data['setup']} - {data['punchline']}"
    
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error fetching joke: {e}"

if __name__ == "__main__":
    print(get_joke())  # ✅ Ab joke print bhi hoga
