"""Needed static functions"""
import random
import time
import os

def create_file(file_name):
    """Creates a file given the name"""
    if os.path.exists(file_name):
        os.remove(file_name)
    return open(file_name, 'x', encoding="utf-8")

def random_num(max_random_number):
    """Creates a random number between 0 and max"""
    return int(random.randint(1,max_random_number))

def random_date():
    """Creates a random date between start and end"""
    start = "2022-01-01"
    end = "2023-06-01"
    prop = random.random()
    time_format = '%Y-%m-%d'
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))

def create_unique_random_couples(elements_number,max_random_first,max_random_second):
    """Creates unique couples, given how many couples, the max number of the first and the second"""
    first_array = []
    second_array = []
    couples = set([])
    for _ in range(elements_number):
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

def as_text(text):
    """Formats the output as text for a SQL sentence"""
    return '\'' + text + '\''

def as_timestamp(text):
    """Formats the output as timestamp for a SQL sentence"""
    return 'TO_TIMESTAMP(\'' + text + '\',\'YYYY-MM-DD\')'
