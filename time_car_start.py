import datetime
from time import sleep
import pickle
import numpy as np


def check_time():
    start_time = datetime.datetime.now()
    h = start_time.hour
    m = start_time.minute
    s = start_time.second
    time_2_check = h * 3600 + m * 60 + s
    f = open("timecheck.pickle", "wb")
    f.write(pickle.dumps(time_2_check))
    f.close()


def now():
    current_time = datetime.datetime.now()
    h = current_time.hour
    m = current_time.minute
    s = current_time.second
    return np.array([h, m, s])


def real_time():
    h = now()[0]
    m = now()[1]
    s = now()[2]
    temp = h * 3600 + m * 60 + s
    time_2_check = 'timecheck.pickle'
    data_time_check = pickle.loads(open(time_2_check, "rb").read())
    check = temp - data_time_check
    return np.array([check, temp])


if __name__ == "__main__":
    sleep(0.00001)
