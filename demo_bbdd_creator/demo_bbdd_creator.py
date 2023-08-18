"""Creates the objects needed to create a database table"""
import numpy as np
from . import aux_functs

class DemoDatabaseTable:
    """Class for database table"""
    def __init__(self,table_name,fields:list[str],schema_name = 'public') -> None:
        self.__table_name = table_name
        self.__fields = fields
        self.__data = []
        self.__schema_name = schema_name

    @property
    def table_name(self):
        """Property: table name"""
        return self.__table_name

    @property
    def fields(self):
        """Property: fields"""
        return self.__fields

    @property
    def data(self):
        """Property: data"""
        return self.__data

    @property
    def schema_name(self):
        """Property: schema name"""
        return self.__schema_name

    def erase_data(self):
        """Function to erase all elements in a table"""
        self.__data = []

    def insert_data(self,data_array):
        """Function to insert data in a table"""
        # SECURITY CHECKINGS
        if len(self.__data) != 0:
            raise EnvironmentError("Table already contains data. Erase it before inserting")
        sizes = set()
        for data in data_array:
            sizes.add(len(data))
        if len(sizes)>1:
            raise ValueError('All data arrays must have equal length')
        if len(data_array) != len(self.__fields):
            raise ValueError('Data arrays must have ' + str(len(self.__fields)) + ' elements')
        self.__data = data_array

    def export_into_query(self):
        """Function to create a query to insert data into table"""
        query = 'INSERT INTO ' + self.__schema_name + '.' + self.__table_name + ' ('
        for i,title in enumerate(self.__fields):
            query += title
            if i < len(self.__fields) - 1:
                query +=  ', '
        query += ') VALUES\n'
        data_array = np.array(self.__data)
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
        new_file = aux_functs.create_file(self.__table_name + '.sql')
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
    def name(self):
        """Name property"""
        return self.name

    @name.setter
    def name(self, value):
        """Name setter"""
        self.__name = value
