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

        days, remainder = divmod(time_until_target.seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        countdown_str = "{:02} days {:02}:{:02}:{:02}".format(
            days, hours, minutes, seconds
        )

        print(countdown_str, end="\r")
        time.sleep(1)

if __name__ == "__main__":
    # Set the target date for Christmas
    christmas_date = datetime(year=2023, month=12, day=25)

    # Display the Christmas countdown
    display_countdown(christmas_date)