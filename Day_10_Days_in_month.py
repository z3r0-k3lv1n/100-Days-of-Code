
def is_leap(year):
  is_leap_year = False
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        is_leap_year = True
      else:
        is_leap_year = False
    else:
      is_leap_year = True
  else:
    is_leap_year = False
  return is_leap_year
  

def days_in_month(year, month):
  # month_days = [{"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}]
  # name_of_month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  if month > 12 or month < 1:
    return "Invalid month. Please try again."
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2: # If the year entered is a leap year according to the "is_leap(year)" function, and the month selected is the second month / Feb. Then 29 will be returned as there are 29 days in Feb during a leap year.
    return 29
  return month_days[month - 1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












