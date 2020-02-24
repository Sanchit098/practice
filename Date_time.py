import datetime


y = datetime.datetime.now()
print(y)

x = datetime.datetime(2020, 2, 17)
print(x)
print(x.strftime("%M"))
print(x.strftime("%B %Y"))

####dat1=datetime.datetime(2018,4,16)
##print(dat1)
##print(dat1.year)
##print(dat1.month)
##print(dat1.day)

dm_date=datetime.date(2016,11,16)
dm_time=datetime.time(8,20,20)
dm_datetime=datetime.datetime(2016,11,16,8,20,20)

print(dm_date)
print(dm_time)
print(dm_datetime)
