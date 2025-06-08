from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    try:
        # Ask user how many days to add
        days = int(input("Enter the number of days to add: "))

        # Get today's date
        current_date = datetime.now()

        # Add the number of days using timedelta
        future_date = current_date + timedelta(days=days)

        # Format and print the future date
        print("Future Date after", days, "days will be:", future_date.strftime("%Y-%m-%d"))

    except ValueError:
        print("Please enter a valid integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

    