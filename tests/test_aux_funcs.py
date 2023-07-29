from demo_bbdd_creator import aux_functs

def test_random_num_less_than_max():
    assert aux_functs.random_num(100) <= 100

def test_random_num_is_number():
    assert type(aux_functs.random_num(100)) is int

def test_random_num_positive():
    assert aux_functs.random_num(100) > 0

def test_random_date_is_date():
    pass