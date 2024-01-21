def calculate_future_hour(hour, period, hours_ahead):
    hour_in24 = hour + 12 if period.lower() == "pm" else hour
    future_hour_in24 = (hour_in24 + hours_ahead) % 24
    future_hour = future_hour_in24 if future_hour_in24 <= 12 else future_hour_in24 - 12
    future_period = "am" if future_hour_in24 < 12 else "pm"
    print(f"Future time: {future_hour} {future_period}")


hour = int(input("Enter hour (between 1 to 12): "))
period = input("Enter 'am' or 'pm': ").lower()
hours_ahead = int(input("How many hours ahead?: "))
calculate_future_hour(hour, period, hours_ahead)
