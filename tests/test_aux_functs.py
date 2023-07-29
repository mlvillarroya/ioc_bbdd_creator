from demo_bbdd_creator import aux_functs
from datetime import datetime

def test_random_num_less_than_max():
    assert aux_functs.random_num(100) <= 100

def test_random_num_is_number():
    assert type(aux_functs.random_num(100)) is int

def test_random_num_positive():
    assert aux_functs.random_num(100) > 0

def test_random_date_is_date():
    time_format = '%Y-%m-%d'
    test_str = aux_functs.random_date()
    assert bool(datetime.strptime(test_str, time_format)) == True

def test_create_unique_random_couples_has_element_number():
    a,b = aux_functs.create_unique_random_couples(5,5,5)
    assert len(a) == 5
    assert len(b) == 5
