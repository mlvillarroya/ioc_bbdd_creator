import numpy as np
from . import aux_functs

class DemoDatabaseTable:
    def __init__(self,table_name,fields:list[str]) -> None:
        self.table_name = table_name
        self.fields = fields
        self.data = []

    def erase_data(self):
        self.data = []

    def insert_data(self,data_array):
        # SECURITY CHECKINGS
        if len(self.data) != 0: raise Exception("Table already contains data. Erase it before inserting")
        sizes = set()
        for data in data_array:
            sizes.add(len(data))
        if len(sizes)>1: raise Exception('All data arrays must have equal length')
        if len(data_array) != len(self.fields): raise Exception('Data arrays must have ' + str(len(self.fields)) + ' elements')
        self.data = data_array

    def export_into_query(self):
        query = 'INSERT INTO ' + self.table_name + ' ('
        for i,title in enumerate(self.fields):
            query += title
            if i < len(self.fields) - 1: query +=  ', '
        query += ') VALUES\n'
        data_array = np.array(self.data)
        trasposed_array = data_array.transpose()
        for i,data_row in enumerate(trasposed_array):
            final_character = ',\n' if i < (len(trasposed_array) -1) else ';'
            query += '('
            for j,data in enumerate(data_row):
                query += str(data)
                if j < len(data_row) - 1: query +=  ', '
            query += ')' + final_character
        return query
    
    def export_into_file(self):
        f = aux_functs.create_file(self.table_name + '.sql')
        f.write(self.export_into_query())
        f.close()
            
class DemoDatabase:
    def __init__(self,bbdd_name) -> None:
        self.tables = []
        
    def table_add(self,table:DemoDatabaseTable):
        self.tables.append(table)