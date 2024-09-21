from datetime import datetime, timedelta, date
from statistics import mean

cycle_date = ""
cycle_date_list = []

assumed_cycle_duration = 30
least_cycle_duration = 21
reference_date = date.today() - timedelta(days=150)


def print_user_details():
    print("Welcome to my calendar ")
    user_name = input("whats your name? ")
    print(
        "Hello "
        + user_name
        + " you can register your monthly cycle details and obtain your average cycle duration"
    )
    print("Today is " + str(reference_date))


def recent_periode_date_computing():
    last_periode_date = reference_date - timedelta(days=int(num_days))
    return last_periode_date


def compute_next_periode_date():
    next_periode_date = reference_date + timedelta(
        days=int(assumed_cycle_duration) - int(num_days)
    )
    return next_periode_date


def submit_cycle_statistics():
    with open("cycle_statistics.txt", "w") as f:
        for periode_start_dates in cycle_date_list:
            f.write(date.strftime(periode_start_dates, "%d-%m-%Y") + "\n")


def collect_cycle_statistics():
    duration_list = []
    cycle_date_list = load_cycle_date_from_file()
    for i in range(len(cycle_date_list) - 1):
        cycle_durations = datetime.strptime(
            cycle_date_list[i + 1], "%d-%m-%Y"
        ) - datetime.strptime(cycle_date_list[i], "%d-%m-%Y")
        duration_list.append(cycle_durations.days)
        duration_details = (
            "cycle "
            + str(i + 1)
            + " went from "
            + str(cycle_date_list[i])
            + " to "
            + str(cycle_date_list[i + 1])
        )
        print(duration_details + " making it " + str(cycle_durations.days) + " days")
    if len(cycle_date_list) >= 2:
        average_duration = int(mean(duration_list))
        print(
            "your average cycle durations for the past months is : "
            + str(average_duration)
        )


def load_cycle_date_from_file():
    with open("cycle_statistics.txt", "r") as f:
        cycle_date_list = f.read().splitlines()
    return cycle_date_list


def custom_formatter(number_list: list[int]):
    if len(number_list) >= 2:
        number_list_last_item = str(number_list[-1])
        return (
            ", ".join(list(map(str, number_list[:-1])))
            + " and "
            + number_list_last_item
        )
    elif len(number_list) == 1:
        return str(number_list[0])
    else:
        return ""


collect_cycle_statistics()
print_user_details()
user_response = "yes"
while reference_date <= date.today() and user_response != "quit":
    user_response = input("Did you have your periode? ")
    if user_response == "yes":
        num_days = input(
            "How many days ago was your menstrual period?(if today, enter 0) "
        )
        while cycle_date != "" and int(num_days) >= 10:
            print(
                "your last had you periode on the "
                + str(reference_date - timedelta(days=30))
                + " so you could not possibly have your next periode before the "
                + str(cycle_date - timedelta(days=9))
            )
            print(
                "what you had was not your menstrual period, it could be something else"
            )
            print("it could occur as a result of rough and harsh sexual activities")
            question = "Any sexual activity ?(yes or no) "
            activity = input(question)
            while activity not in  ("yes","no"):
                activity = input("Invalid response, what do you mean? " + question)
            if activity == "yes":
                list_of_possible_causes = [
                    "i was sexually abused",
                    "its my boyfriend",
                    "its my husband",
                    "its my sugar-daddy",
                ]
                for i, causes in enumerate(list_of_possible_causes):
                    i += 1
                    print(str(i) + " : " + causes)
                user_response = int(
                    input("what could be the cause? (choose a number please) ")
                )

                if user_response == 1:
                    print("Oh thats so sad, sorry to hear that ")
                elif user_response == 2:
                    print("Oh thats so sad, you should tell him to be soft ")
                elif user_response == 3:
                    print("Oh thats so sad, you should tell him to be soft ")
                elif user_response == 4:
                    print(
                        "Oh thats so sad, sugar-daddies usually don't have enough strenght to be that rough,",
                        "he might be a sex-addict, you could go to social services",
                    )
            else:
                print("Try consulting a doctor ")
            reference_date = reference_date + timedelta(days=1)
            print("Today is " + str(reference_date))
            num_days = input(
                "How many days ago was your menstrual period?(if today, enter 0) "
            )
        recent_periode_date_computing()
        cycle_date_list.append(recent_periode_date_computing())
        submit_cycle_statistics()
        print(
            "so you last had your period on the " + str(recent_periode_date_computing())
        )
        compute_next_periode_date()
        cycle_date = compute_next_periode_date()
        print(
            "so we can assume your next period will be on the "
            + str(compute_next_periode_date())
        )
        reference_date = cycle_date
        if reference_date <= date.today():
            print("Today is " + str(reference_date))
    elif user_response == "no":
        number_of_days_to_today = (date.today() - reference_date).days
        deal_date = min(number_of_days_to_today, 5)
        reference_date = reference_date + timedelta(days=deal_date)
        if reference_date <= date.today():
            print("Ok! see you in", deal_date, "days.")
            print("Today is " + str(reference_date))

    elif user_response != "quit":
        print("sorry what do you mean?")


























"""#return if year is leap year or not   
def determine_leap_year(year:int):
    if (year % 100 != 0 and year % 4 == 0 or year % 400 == 0):
        return True
    return False
#given a date, returns number of days elapsed from the begining of the current year(1st january)
def days_elapsed_from_begining_of_year_to_given_date(day:int, month:int, year:int):
    days_elapsed = int(day)
    switcher = {
        10: 30,
        9: 31,
        8: 30,
        7: 31,
        6: 31,
        5: 30,
        4: 31, 
        3: 30, 
        2: 31,
        1: 28,
        0: 31
    }
    if (determine_leap_year(year) and month > 1):
        days_elapsed += 1
        days_elapsed += switcher.get(int(month))
        print(days_elapsed)
#given a year and days elapsed in it, finds dates by storing results in day and month         
def date_finder(number_of_days_elapsed:int, year:int, day:int, month:int):
    month = [ 0, 31, 28, 30, 31, 30, 31, 31, 30, 31, 30]
    if (determine_leap_year(year)):
        month[2] = 29
    for i in range(1, 13):
        if (number_of_days_elapsed <= month[i]):
            break
        number_of_days_elapsed = number_of_days_elapsed - month[i] 
    day[0] = number_of_days_elapsed
    month[0] = i + 1
#adding x days to the given date
def add_number_of_days_to_date(day1:int, month1:int, year1:int, num:int): 
    number_of_days_elapsed1 = days_elapsed_from_begining_of_year_to_given_date(day1, month1, year1)
    if determine_leap_year(year1):
        days_left = 366 - number_of_days_elapsed1
    else:
        days_left = 365 - number_of_days_elapsed1
    #year2 is giong to store result year and number_of_days_elapsed2 is going to store number_of_days_elapsed in result year.
    if (num <= days_left):
        year2 = year1
        number_of_days_elapsed2 = number_of_days_elapsed1 + num
    else:
        #num may store thousands of days.We find correct year and number_of_days_elapsed in the year
        num -= days_left
        year2 = year1 + 1 
        if determine_leap_year(year2):
            year2_days = 366
        else:
           year2_days = 365
        while (num >= year2_days):
            num -= year2_days
            year2 += 1
        if determine_leap_year(year2):    
                year2_days = 366
        else:
           year2_days = 365
    number_of_days_elapsed2 = num"""
