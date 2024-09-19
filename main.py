from datetime import datetime, timedelta, date
cycle_date = ""
cycle_date_list = []

assumed_cycle_duration = 30
reference_date = date.today()

def print_user_details():
    print("Welcome to my calendar ")
    user_name = input("whats your name? ")
    print("Hello " + user_name + " you can register your monthly cycle details and obtain your average cycle duration")
    print("Today is " + str(reference_date))
    
def recent_periode_date_computing():  
    last_periode_date = reference_date - timedelta(days= int(num_days))
    return last_periode_date

def compute_next_periode_date():
    next_periode_date = reference_date + timedelta(days=int(assumed_cycle_duration)-int(num_days))
    return next_periode_date

def submit_cycle_statistics():
   with open ("cycle_statistics.txt", "w") as f:
        for periode_start_dates in cycle_date_list:
            f.write(date.strftime(periode_start_dates, "%d-%m-%Y"))
            
def collect_cycle_statistics():
    with open("cycle_statistics.txt", "r") as f:
        cycle_date_list = f.read().splitlines()
    for i in range(len(cycle_date_list)-1):
        cycle_durations = datetime.strptime (cycle_date_list[i+1], "%d-%m-%Y") - datetime.strptime(cycle_date_list[i], "%d-%m-%Y")
        return cycle_durations
        
print_user_details()
update = input("Any update? (yes or no) ")
while update == "yes":
    period_on = input("you had your periode?")
    if period_on == "yes":
        num_days = input("How many days ago was your menstrual period?(if today, enter 0) ")    
        recent_periode_date_computing()
        cycle_date_list.append(recent_periode_date_computing())  
        submit_cycle_statistics() 
        print("so you last had your period on the " + str(recent_periode_date_computing()))    
        compute_next_periode_date() 
        cycle_date =  compute_next_periode_date()   
        print("so we can assume your next period will be on the " + str(compute_next_periode_date())) 
        reference_date = cycle_date
        print("Today is " + str(reference_date)) 
    else:
       print("Ok! see you tomorrow.")
       reference_date = reference_date + timedelta(days=1) 
       print("Today is " + str(reference_date))
    update = input("Any update? (yes or no) ")  
print("Ok! see you next time...")
print("your cycle durations for the past months are respectively: " + str(collect_cycle_statistics()))

    
    
    
    
    
    
    
    


   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''#return if year is leap year or not   
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
    number_of_days_elapsed2 = num'''
       
       
     
        