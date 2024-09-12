def user_details():
    print("Welcome to my calendar ")
    input("whats your name? ")
    input("How old are you? ")
    
    
def compute_cyle():
    last_period_date = input("When last was your menstrual period?(d, m, y) ")
    menstrual_periode_duration = input("How long does your menstrual periode usually last? ")
    normal_cycle_duration = 28 
    normal_ovulation_date = 14
    Next_periode_date = last_period_date + (normal_cycle_duration-1)
 #return if year is leap year or not   
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
    number_of_days_elapsed2 = num
       
       
days_elapsed_from_begining_of_year_to_given_date(20, 12, 2020)      
        