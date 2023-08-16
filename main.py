"""Main"""
import names
from demo_bbdd_creator import DemoDatabaseTable
from demo_bbdd_creator import aux_functs

CLIENTS_NUMBER = 30000
PRODUCTS_NUMBER = 84
INVENTARY_NUMBER = 4000
SALES_NUMBER = 60000
SALE_DETAILS_NUMBER = 120000
SALE_STATES_NUMBER = 4
CITY_NUMBER = 8223
WAREHOUSE_NUMBER = 50
WISHLIST_NUMBER = 40000

def create_wishlist(wishlist_number):
    """Function creating wishlist."""
    table = DemoDatabaseTable('wishlist',['id_client','id_product'],'products')
    id_client_data, id_product_data = aux_functs.create_unique_random_couples(wishlist_number,
                                                                              PRODUCTS_NUMBER,
                                                                              CLIENTS_NUMBER)
    table.insert_data([id_client_data,id_product_data])
    table.export_into_file()

def create_warehouses(warehouse_number):
    """Function creating warehouses."""
    table = DemoDatabaseTable('warehouses',['"name"','address','id_city'],'products')
    name_data = [aux_functs.as_text('Warehouse' + str(i)) for i in range(warehouse_number)]
    address_data = [aux_functs.as_text('Address' + str(i)) for i in range(warehouse_number)]
    id_city_data = [aux_functs.random_num(CITY_NUMBER) for i in range(warehouse_number)]
    table.insert_data([name_data,address_data,id_city_data])
    table.export_into_file()

def create_sales(sales_number):
    """Function creating sales."""
    table = DemoDatabaseTable('sales',['id_client','id_sale_state','"date"'],'sales')
    id_client_data = [aux_functs.random_num(CLIENTS_NUMBER) for i in range (sales_number)]
    id_sale_state_data = [aux_functs.random_num(SALE_STATES_NUMBER) for i in range (sales_number)]
    date_data = [aux_functs.random_date() for i in range (sales_number)]
    table.insert_data([id_client_data,id_sale_state_data,date_data])
    table.export_into_file()

def create_clients(client_number):
    """Function creating clients."""
    table = DemoDatabaseTable('clients',
                              ['first_name','last_name','address','email','id_city','phone'],
                              'clients')
    first_name_data = []
    last_name_data = []
    email_data = []
    for i in range (client_number):
        full_name = names.get_full_name()
        first_name_data.append(full_name.split(' ')[0])
        last_name_data.append(full_name.split(' ')[1])
        email_data.append(
            full_name.split(' ')[0][:3].lower() +
              full_name.split(' ')[1][:3].lower() +
                str(aux_functs.random_num(999)) +
                  'gmail.com')
    address_data = ['Address ' + str(i) for i in range (client_number)]
    id_city_data = [aux_functs.random_num(CITY_NUMBER) for i in range (client_number)]
    phone_data = [aux_functs.random_num(999999999) for i in range (client_number)]
    table.insert_data(
        [first_name_data,last_name_data,address_data,email_data,id_city_data,phone_data]
        )
    table.export_into_file()

def create_inventory(inventory_number):
    """Function creating inventory."""
    table = DemoDatabaseTable('inventory',['id_product','id_warehouse','qty','date_in'],'products')
    id_product_data, id_warehouse_data = aux_functs.create_unique_random_couples(inventory_number,
                                                                                 PRODUCTS_NUMBER,
                                                                                 WAREHOUSE_NUMBER)
    qty_data = [aux_functs.random_num(5) for i in range(inventory_number)]
    date_in_data = [aux_functs.as_timestamp(aux_functs.random_date()) for i in range (inventory_number)]
    table.insert_data([id_product_data,id_warehouse_data,qty_data,date_in_data])
    table.export_into_file()


def create_sale_details(sale_details_number, sale_number,product_number):
    """Function creating sale_details."""
    table = DemoDatabaseTable('sale_details',['id_sale','id_product','qty','discount'],'sales')
    id_sale_data = [aux_functs.random_num(sale_number) for i in range(sale_details_number)]
    id_product_data = [aux_functs.random_num(product_number) for i in range(sale_details_number)]
    qty_data = [aux_functs.random_num(5) for i in range(sale_details_number)]
    discount_data = [aux_functs.random_num(20) for i in range(sale_details_number)]
    table.insert_data([id_sale_data,id_product_data,qty_data,discount_data])
    table.export_into_file()

def main():
    """Main function."""
    # create_clients(CLIENTS_NUMBER)
    create_inventory(INVENTARY_NUMBER)
    create_warehouses(WAREHOUSE_NUMBER)
    # create_wishlist(WISHLIST_NUMBER)
    # create_sales(SALES_NUMBER)
    # create_sale_details(SALE_DETAILS_NUMBER,SALES_NUMBER,PRODUCTS_NUMBER)
    # print(create_insert_query('table_name',['row1','row2'],[['data1','data2','data3','data4'],['data1','data2','data3','data4']]))

if __name__ == '__main__':
    main()
