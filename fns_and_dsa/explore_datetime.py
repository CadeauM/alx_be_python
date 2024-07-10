from datetime import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print('current date and time:', current_date.strftime("%Y-%m-%d, %H:%M:%S"))

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current datetime:"))
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
