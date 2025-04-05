import requests
import time
import html 
def show_data(topic, difficulty, qtype, amount):
    category_ids = {
        "History": 22, "Geography": 23, "General Knowledge": 9, "Science: Mathematics": 19,
        "Science: Computers": 18, "Sports": 21, "Art": 25, "Entertainment: Books": 10,
        "Science & Nature": 17, "Politics": 24, "Vehicles": 28
    }

    if topic not in category_ids:
        return "Invalid topic selected!"

    timestamp = int(time.time())
    url = f"https://opentdb.com/api.php?amount={amount}&category={category_ids[topic]}&difficulty={difficulty.lower()}&type={qtype}&_={timestamp}"
    
    response = requests.get(url)
    
    try:
        data = response.json()
    except ValueError:
        return "Error: Unable to parse API response!"

    if "results" not in data or not data["results"]:
        return "No data found!"

    for question in data["results"]:
        question["question"] = html.unescape(question["question"])
        question["correct_answer"] = html.unescape(question["correct_answer"])
        question["incorrect_answers"] = [html.unescape(ans) for ans in question["incorrect_answers"]]

    return data["results"]