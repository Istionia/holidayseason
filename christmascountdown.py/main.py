from datetime import datetime, timedelta
import time

christmas_date = datetime(year=2023, month=12, day=25)

def calculate_time_until_target(target_date: datetime) -> timedelta:
    """
    Calculate the time difference between the current date and a specified future date.

    Parameters:
    - target_date (datetime): The future date to calculate the time difference to.

    Returns:
    - timedelta: The time difference between the current date and the specified future date.
    """
    current_date = datetime.now()
    time_until_target = target_date - current_date
    return time_until_target

def display_countdown(target_date: datetime):
    """
    Display a countdown to the target date in the console.

    Parameters:
    - target_date (datetime): The date to count down to.
    """
    while True:
        time_until_target = calculate_time_until_target(target_date)
        if time_until_target.total_seconds() <= 0:
            print("Merry Christmas!")
            break

        minutes, seconds = divmod(int(round(time_until_target.total_seconds())), 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        weeks, days = divmod(days, 7)

        countdown_str = (
            f"{weeks:02} weeks {days:02} days {hours:02}:{minutes:02}:{seconds:02}"
        )

        print(countdown_str, end="\r")
        time.sleep(1)

if __name__ == "__main__":
    # Set the target date for Christmas
    christmas_date = datetime(year=2023, month=12, day=25)

    # Display the Christmas countdown
    display_countdown(christmas_date)