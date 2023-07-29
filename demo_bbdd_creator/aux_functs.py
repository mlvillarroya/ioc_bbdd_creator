import random
import time
import os

def create_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    return open(file_name, 'x')

def random_num(max):
    return int(random.randint(1,max))

def random_date():
    start = "2022-01-01"
    end = "2023-06-01"
    prop = random.random()
    time_format = '%Y-%m-%d'
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))

def create_unique_random_couples(elements_number,max_random_first,max_random_second):
    first_array = []
    second_array = []
    couples = set([])
    for i in range(elements_number):
        unique_couple_found = False
        first_element = 0
        second_element = 0
        while unique_couple_found is False:
            first_element = random_num(max_random_first)
            second_element = random_num(max_random_second)
            if (first_element,second_element) not in couples: 
                unique_couple_found = True
                couples.add((first_element,second_element))
                first_array.append(first_element)
                second_array.append(second_element)
    return first_array,second_array
