# -*- coding: utf-8 -*-

def startdate():
    year, month= 1901,1
    date = [year, month]
    return date

def gonextmonth(date):
    list_of_days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    thismonth = list_of_days[date[1]]
    if date[0]%4==0 and date[1]==2:
        thismonth += 1
        if date[0] == 2000:
            thismonth -= 1
    remaindays = thismonth % 7
    return remaindays

if __name__ == '__main__':
    date = startdate()
    month_start_day=2
    month_starts_with_sunday = 0
    while(1):
        print date, month_start_day
        if date[0]==2000 and date[1]==12:
            break
        ym = (date[0],date[1])
        daychange = gonextmonth(ym)
        month_start_day += daychange
        if month_start_day > 7:
            month_start_day-=7
        elif month_start_day == 7:
            month_starts_with_sunday += 1
        date[1]+=1
        if date[1]>12:
            date[1] -= 12
            date[0]+=1
    print month_starts_with_sunday
