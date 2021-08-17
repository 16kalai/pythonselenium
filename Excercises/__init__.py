#### Excercise

# like paragraph
import datetime

from dateutil.utils import today

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky.")

# finding version
import sys
print ('pyhton version')
print(sys.version)
print('version ifo')
print(sys.version_info)

fname = 'kalai'
lname = 'nati'
print("hello " + lname + " " + fname)


num = ("1,2,5,7,8")
list = num.split(",")
tuple = tuple(list)
print("List: ", list)
print("Tuple: ",tuple)

Exam_date = (1,2,2021)
print("Tamil: %i/%i/%i"%Exam_date)


#import calendar
#y = int(input("input the year: "))
#m = int(input("input the month: "))
#print(calendar.month(y,m))


from datetime import date
k = datetime.datetime
s = date(1994,2,16)
t = date.today()
u = s - t
print(u.days)


#volume of sphere
# the formula is v=4/3 *3.141*r^2

import math
pi = math.pi
r = 6
V = 4/3 *pi* r**3
print("Volume of sphere is: ",V)




