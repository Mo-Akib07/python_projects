def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invelid month"
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:    #if it is false the the line 15 is not exicute
        return 29
    return months_days[month - 1]



year = int(input("Enter a Year : "))
month = int(input("Enter a Month : "))
days = days_in_month(year, month)
print(days)