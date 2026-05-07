from datetime import datetime

def greet_user():
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "Good Morning sir"
    elif 12 <= hour < 17:
        return "Good Afternoon sir"
    elif 17 <= hour < 21:
        return "Good Evening sir"
    else:
        return "Good Night sir"

def get_date_time():
    now = datetime.now()

    date = now.strftime("%A, %d %B %Y")
    time = now.strftime("%I:%M %p")

    return f"Today is {date} and the time is {time}"

