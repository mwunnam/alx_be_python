from datetime import datetime, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    return current_datetime

def calculate_future_date(number):
    future_date = datetime.now() - timedelta(days=number)
    return future_date


current_time_date = display_current_datetime()
f_current_time_date = current_time_date.strftime("%Y-%m-%d %H:%M:%S")
print(f"current date and time: {f_current_time_date}")
user_input = int(input("Enter a number of days to add to the current date: "))
future_date = calculate_future_date(user_input)
f_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
print(f"Future date: {f_future_date}")
