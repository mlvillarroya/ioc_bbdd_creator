from demo_bbdd_creator import DemoDatabaseTable
import pytest

def test_class_initialization_name_OK():
    a = DemoDatabaseTable('table_name',['field1','field2','field3'])
    assert a.table_name == 'table_name'
def test_class_initialization_fields_OK():
    a = DemoDatabaseTable('table_name',['field1','field2','field3'])
    assert len(a.fields) == 3
    assert a.fields[0] == 'field1'
    assert a.fields[1] == 'field2'
    assert a.fields[2] == 'field3'
def test_class_initialization_data_OK():
    a = DemoDatabaseTable('table_name',['field1','field2','field3'])
    assert a.data == []
def test_insert_with_data_throws_exception():
    a = DemoDatabaseTable('table_name',['field1','field2','field3'])
    a.insert_data([['data1'],['data2'],['data3']])
    with pytest.raises(Exception) as exc_info:
        a.insert_data([['data1'],['data2']])
    assert str(exc_info.value) == 'Table already contains data. Erase it before inserting'
def test_insert_data_incorrect_length_throws_exception():
    a = DemoDatabaseTable('table_name',['field1','field2','field3'])
    with pytest.raises(Exception) as exc_info:
        a.insert_data([['data1'],['data2']])
    assert str(exc_info.value) == 'Data arrays must have 3 elements'
def test_insert_data_unequal_length_throws_exception():
    a = DemoDatabaseTable('table_name',['field1','field2','field3'])
    with pytest.raises(Exception) as exc_info:
        a.insert_data([['data1a','data1b'],['data2']])
    assert str(exc_info.value) == 'All data arrays must have equal length'
def test_insert_data_works_OK():
    a = DemoDatabaseTable('table_name',['field1','field2','field3'])
    a.insert_data([['data1'],['data2'],['data3']])
    assert len(a.data) == 3
    assert a.data == [['data1'],['data2'],['data3']]
def test_erase_data_works():
    a = DemoDatabaseTable('table_name',['field1','field2','field3'])
    a.insert_data([['data1'],['data2'],['data3']])
    a.erase_data()
    assert a.data == []
def test_export_into_query_works():
    a = DemoDatabaseTable('table_name',['field1','field2','field3'])
    a.insert_data([['data1'],['data2'],['data3']])
    assert a.export_into_query() == 'INSERT INTO table_name (field1, field2, field3) VALUES\n(data1, data2, data3);'