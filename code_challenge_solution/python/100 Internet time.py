import datetime

def convert_to_internet_time(time):
    beats = (time.hour * 3600 + time.minute * 60 + time.second) / 86.4
    return beats

current_time = datetime.datetime.now().time()
internet_time = convert_to_internet_time(current_time)
print("Current Internet Time: ", internet_time)