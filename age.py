from datetime import date, datetime


def age_calculator():
    today = date.today()
    current_date = today.strftime("%d-%m-%Y")
    current = datetime.strptime(current_date, "%d-%m-%Y").date()
    time_str = input("Enter date (dd-mm-YYYY): ")
    chosen_date = (datetime.strptime(time_str, "%d-%m-%Y").date())
    difference = current - chosen_date
    return f"{int((difference.days)/365)} years"


print(age_calculator())
