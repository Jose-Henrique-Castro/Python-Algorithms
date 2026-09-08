def is_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0):
        return True
    else: 
        return False


try:

    year = int(input("What is the year ?\n"))

    if(is_leap_year(year)): 
        print(f"{year} IS a leap year!\n")

    else:
        print(f"{year} IS NOT a leap year!\n")


except:
    print("Invalid input. Please enter a valid number")