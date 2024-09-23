import time

# epoch = a date and tome from which a computer measures system time
#         when your computer thinks time began (reference point)

#print(time.ctime(1000000)) # convert a time expressed in seconds since epoch to a readable string.

#rint(time.time()) # return current seconds since

#print(time.ctime(time.time())) # prints local time

#time_object = time.localtime() # time_object = time.struct_time

# UTC (Coordinated Universal Time) is the primary time standard by which the world regulates clocks and time. It is within about
# one second of mean solar time at 0 degrees longitude and is not adjusted for daylight saving time

#time2_object = time.gmtime()
#print(time_object)
#local_time = time.strftime("%B-%d-%Y %H:%M:%S", time_object)
#print(local_time)

#time_string = "20 April, 2020"
#time_object = time.strptime(time_string, "%d %B, %Y")
#print(time_object)

time_tuple = (2024,9,22,4,20,0,0,0,-1)
time_string = time.asctime(time_tuple)
print(time_string)