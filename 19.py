"""
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]

days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

year = 1901
month = "Jan"
day = "Tue"
date = 1

sundays = 0

month_days_dict = {
    "Jan": 31,
    "Feb": [28,29],
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "Aug": 31,
    "Sep": 30,
    "Oct": 31,
    "Nov": 30,
    "Dec": 31
}

week_index = 0


#Recurring For Loop - for Month, Date, Day
while year <= 2000:
    for month_index in months:
        

        date = 0

        month = month_index

        day = days[week_index]

        amount_of_days = month_days_dict[month]

        if month_index == "Feb":
            if year % 4 == 0:
                amount_of_days = amount_of_days[1]
            else:
                amount_of_days = amount_of_days[0]
        
        while date < amount_of_days:
            if week_index == 6:
                week_index = 0 
            else:
                week_index += 1
            
            day = days[week_index]
            date += 1

            if date == 1 and day == "Sun":
                sundays += 1

    year += 1

    
print(sundays)


