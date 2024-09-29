from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return current_date

def calculate_future_date():
    try:
        number_of_days= int(input("Enter number of days to calculate a future date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%y-%m-%d")
        print(f"Future Date: {formatted_future_date}")
    except ValueError:
        print("Invalid Input. Please input a valid number of days")


def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
