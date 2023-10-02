# import datetime class from the datetime module because the object of datetime support strftime method

from datetime import datetime 
now = datetime.now() # current date and time

year = now.strftime("%Y")#display year
print("year:", year)

month = now.strftime("%m")# month
print("month:", month)

day = now.strftime("%d")# day
print("day:", day)

time = now.strftime("%H:%M:%S") # time with seconds
print("time:", time)

date_time = now.strftime('%m/%d/,%Y__%H:%M:%S') # date and time
# only contain one argument
print("Date and Time:",date_time)

