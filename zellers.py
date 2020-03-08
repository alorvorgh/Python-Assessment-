name= input("Enter your name: ")
year = int(input('Enter year(e.g. 2018) : '))
month = int(input('Enter month(1-12) : '))
day = int(input('Enter day of the month(1-31) : '))

if month == 1:
    month = month + 12
    year = year - 1
    
elif month == 2:
    month = month + 12
    year = year - 1
    
print("{} was born on {}th which is".format(name,day,))
century = (year // 100)
century_year = (year % 100)

# Day of the week formula
dotw = (day + ((26 * (month + 1)) // (10)) + century_year + ((century_year) // \
    (4)) + ((century) // (4)) + (5 * century)) % 7

if dotw == 0:
    print('Saturday')
elif dotw == 1:
    print('Sunday')
elif dotw == 2:
    print('Monday')
elif dotw == 3:
    print('Tuesday')
elif dotw == 4:
    print('Wednesday')
elif dotw == 5:
    print('Thursday')
elif dotw == 6:
    print('Friday')

    
