import datetime
def converting_time(time_str):
    input_format = '%I:%M:%S %p'
    time = datetime.datetime.strptime(time_str, input_format)
    time1 = time.strftime('%H:%M:%S')
    return time1
time_in_12 = '04:30:00 PM'
time_in_24 = converting_time(time_in_12)
print('Time in 24-hour format:', time_in_24);
