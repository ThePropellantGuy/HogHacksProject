import requests
import time  # Import time to add a unique timestamp to the request


def show_data(topic, difficulty, qtype, amount):
   category_ids = {
       "History": 22, "Geography": 23, "General Knowledge": 9, "Science: Mathematics": 19,
       "Science: Computers": 18, "Sports": 21, "Art": 25, "Entertainment: Books": 10,
       "Science & Nature": 17, "Politics": 24, "Vehicles": 28
   }


   if topic not in category_ids:
       return "Invalid topic selected!"


   # Add a unique timestamp to the URL to prevent caching
   timestamp = int(time.time())
   url = f"https://opentdb.com/api.php?amount={amount}&category={category_ids[topic]}&difficulty={difficulty}&type={qtype}&_={timestamp}"
   response = requests.get(url)
   print("API URL:", url)  # Debugging: Print the full API URL
   print("API Response:", response.json())  # Debugging: Print the raw API response
   data = response.json().get("results", [])


   if not data:
       return "No data found!"
   return data
