"""Creates the objects needed to create a database table"""
import numpy as np
from . import aux_functs

class DemoDatabaseTable:
    """Class for database table"""
    def __init__(self,table_name,fields:list[str],schema_name = 'public') -> None:
        self.table_name = table_name
        self.fields = fields
        self.data = []
        self.schema_name = schema_name

    def erase_data(self):
        """Function to erase all elements in a table"""
        self.data = []

    def insert_data(self,data_array):
        """Function to insert data in a table"""
        # SECURITY CHECKINGS
        if len(self.data) != 0:
            raise EnvironmentError("Table already contains data. Erase it before inserting")
        sizes = set()
        for data in data_array:
            sizes.add(len(data))
        if len(sizes)>1:
            raise ValueError('All data arrays must have equal length')
        if len(data_array) != len(self.fields):
            raise ValueError('Data arrays must have ' + str(len(self.fields)) + ' elements')
        self.data = data_array

    def export_into_query(self):
        """Function to create a query to insert data into table"""
        query = 'INSERT INTO ' + self.schema_name + '.' + self.table_name + ' ('
        for i,title in enumerate(self.fields):
            query += title
            if i < len(self.fields) - 1:
                query +=  ', '
        query += ') VALUES\n'
        data_array = np.array(self.data)
        trasposed_array = data_array.transpose()
        for i,data_row in enumerate(trasposed_array):
            final_character = ',\n' if i < (len(trasposed_array) -1) else ';'
            query += '('
            for j,data in enumerate(data_row):
                query += str(data)
                if j < len(data_row) - 1:
                    query +=  ', '
            query += ')' + final_character
        return query

    def export_into_file(self):
        """"Function to create a file with the query to insert data into table"""
        new_file = aux_functs.create_file(self.table_name + '.sql')
        new_file.write(self.export_into_query())
        new_file.close()

class DemoDatabase:
    """Class for databases"""
    def __init__(self,name) -> None:
        self.tables = []
        self.name = name

    def table_add(self,table:DemoDatabaseTable):
        """Function to add a table into the database"""
        self.tables.append(table)

    @property
    def Name(self):
        """Name property"""
        return self.name

    @Name.setter
    def Name(self, value):
        """Name setter"""
        self.__name = value
