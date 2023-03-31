import sys

# enter folder location and change \ to //
sys.path.insert(1,'D://bi12-year2//advpython//project//python_prj//mysql_connect')
# access connect(model)
from connect import get_sql_connection as sql #type: ignore


def get_existing_id(type: str):
    # find the amount of "type" (users, products,...) already in the database
    cursor = sql().cursor()
    query = f"SELECT {type}_id FROM food_market.{type}s"
    cursor.execute(query)
    result_set = cursor.fetchall()  # fetch all rows of result set
    id_list = [int(row[0]) for row in result_set]  # create list of type_id integers
    return id_list


#                                   USERS
# insert user
def insert_user(id: int):
    cursor = sql().cursor()

    # user information
    user_id = id
    full_name = str(input("Enter full name: "))
    user_name = str(input("Enter user name: "))
    password = str(input("Enter password: "))
    gender = str(input("Enter gender: "))
    phone_number = int(input("Enter phone number: "))
    address = str(input("Enter address: "))
    user_type = int(input("You are a 1.Customer   2.Seller: "))

    # adding user to data base 
    query = "INSERT INTO users (user_id, full_name, user_name, password, gender, phone_number, address, type)\
             VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"
    data = (user_id, full_name, user_name, password, gender, phone_number, address, user_type)
    cursor.execute(query, data)
    sql().commit()

# get all of a single user's information
def get_user_infos(get_id):
    cursor = sql().cursor()
    # sql command
    query = f"SELECT * FROM food_market.users WHERE user_id ={get_id}"
    cursor.execute(query)

    # create a dict to store user's infos and return said dict
    user_info = {}
    for (user_id, full_name, user_name, password, gender, phone_number, address, type) in cursor:
        user_info = {
            'id' : user_id,
            'full_name' : full_name,
            'user_name' : user_name,
            'password' : password,
            'gender' : gender,
            'phone_number' : phone_number,
            'address' : address,
            "user_type" : type
        }
    
    return user_info

# get a specific info from an user
def get_user_info(get_id: int, select):
    # recall the function get_user_infos to create a dict and use 'select' to get a key from said dict
    return get_user_infos(get_id)[select]

# get all users infos
def get_all_users_infos():
    cursor = sql().cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)    

    user_infos = []

    for (user_id, full_name, user_name, password, gender, phone_number, address, type) in cursor:
        user_infos.append(
            {
            'id' : user_id,
            'full_name' : full_name,
            'user_name' : user_name,
            'password' : password,
            'gender' : gender,
            'phone_number' : phone_number,
            'address' : address,
            "user_type" : type
            }
        )
    
    return user_infos

# sort user
def sort_users(type: str):
    cursor = sql().cursor()
    query = f"SELECT * FROM users ORDER BY {type}"
    cursor.execute(query)

    result_set = cursor.fetchall()
    sorted_id = [int(row(0)) for row in result_set]

    return sorted_id

# modify users
def modify_user(id: int, mod_type: str, mod_into):
    cursor = sql().cursor()
    query_check = f"SELECT * FROM users WHERE user_id = {id}"
    cursor.execute(query_check)
    if len(cursor.fetchall()) == 0:
        print(f"user ID: {id} does not exist")
    else:
        query = f"UPDATE users SET `{mod_type}` = '{mod_into}' WHERE users.user_id = {id}"
        cursor.execute(query)
        sql().commit()

# delete an user
def delete_user(user_id: int):
    cursor = sql().cursor()
    query_check = f"SELECT * FROM users WHERE user_id = {user_id}"
    cursor.execute(query_check)
    if len(cursor.fetchall()) == 0:
        print(f"User ID {user_id} does not exist")
    else:
        query = f"DELETE FROM users WHERE user_id = {user_id};"
        cursor.execute(query)
        sql().commit()



#                                   PRODUCT
#insert product
def insert_product(id: int):
    cursor = sql().cursor()

    # product information
    product_id = id
    name = str(input("Enter the product's name: "))
    type_id = int(input("Enter the product's type id: "))
    price_per_unit = float(input("Enter the product's price per unit: "))
    unit_id = int(input("Enter the product's unit id: "))
    quantity = int(input("Enter the product's quantity: "))
    date_of_manufacture = str(input("Enter the product's date of manufacture (format: yyyy-mm-dd): "))
    date_of_expire = str(input("Enter the product's date of expire (format: yyyy-mm-dd): "))
    description = str(input("Enter the product's description: "))

    # adding product into database
    query = ("INSERT INTO products (product_id, name, type_id, price_per_unit, unit_id, quantity, date_of_manufacture, date_of_expire, description)\
             VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
    data = (product_id, name, type_id, price_per_unit, unit_id, quantity, date_of_manufacture, date_of_expire, description)
    cursor.execute(query, data)
    sql().commit()

# search products
def search_products(search: str):
    cursor = sql().cursor()
    query = f"SELECT * FROM products WHERE name LIKE BINARY '%{search}%';"
    cursor.execute(query)
    
    result_set = cursor.fetchall()
    id_list = [int(row[0]) for row in result_set]
    return id_list

# get all of a product information
def get_product_infos(get_id):
    cursor = sql().cursor()
    # sql command
    query = f"SELECT * FROM food_market.products WHERE product_id = {get_id};"
    cursor.execute(query)

    # get all of products's infos into a dict and return said dict
    product_info = {}
    for (product_id, name, type_name, price_per_unit, unit_name, quantity, date_of_manufacture, date_of_expire, description) in cursor:
        product_info = {
                'id': product_id,
                'name': name,
                'type_name': type_name,
                'price_per_unit': price_per_unit,
                'unit_name': unit_name,
                'quantity': quantity,
                'dom': date_of_manufacture,
                'doe': date_of_expire,
                'description': description
            }

    return product_info
    
# get product info
def get_product_info(get_id:int, select):
    # recall the dict created in function get_product_infos and use 'select' to get a key from the dict
    return get_product_infos(get_id)[select]

# get all products infos
def get_all_products_infos():
    cursor = sql().cursor()
    query = "SELECT products.product_id, products.name, type.type_name, products.price_per_unit, unit.unit_name, products.quantity, products.date_of_expire, products.date_of_manufacture, products.description\
             FROM products INNER JOIN unit on products.unit_id = unit.unit_id\
             INNER JOIN type on products.type_id = type.type_id;"
    cursor.execute(query)    

    product_infos = []
    for (product_id, name, type_name, price_per_unit, unit_name, quantity, date_of_manufacture, date_of_expire, description) in cursor:
        product_infos.append(
            {
                'id': product_id,
                'name': name,
                'type_name': type_name,
                'price_per_unit': price_per_unit,
                'unit_name': unit_name,
                'quantity': quantity,
                'dom': date_of_manufacture,
                'doe': date_of_expire,
                'description': description
            }
        )

    return product_infos

# sort products
def sort_products(type: str):
    cursor = sql().cursor()
    query = f"SELECT * FROM products ORDER BY {type}"
    cursor.execute(query)

    result_set = cursor.fetchall()
    sorted_id = [int(row[0]) for row in result_set]
    
    return sorted_id 
    
# modify products
def modify_product(id: int, mod_type: str, mod_into):
    cursor = sql().cursor()
    query_check = f"SELECT * FROM products WHERE product_id = {id}"
    cursor.execute(query_check)
    if len(cursor.fetchall()) == 0:
        print(f"Product ID: {id} does not exist")
    else:
        query = f"UPDATE products SET `{mod_type}` = '{mod_into}' WHERE products.product_id = {id}"
        cursor.execute(query)
        sql().commit()

# delete a product
def delete_product(product_id: int):
    cursor = sql().cursor()
    query_check = f"SELECT * FROM products WHERE product_id = {product_id}"
    cursor.execute(query_check)
    if len(cursor.fetchall()) == 0:
        print(f"Product ID: {product_id} does not exist")
    else:
        query = f"DELETE FROM products WHERE product_id = {product_id};"
        cursor.execute(query)
        sql().commit()



#                                   SELLER

# def get_seller_info():
#     cursor = sql().cursor()
#     query = "select full_name, user_name, gender, phone_number, address from users where users.type = 'Seller';"
#     cursor.execute(query)
#     for (full_name, user_name, gender, phone_number, address) in cursor:
#         seller_info.append(
#             {
#                 'full_name': full_name,
#                 'user_name': user_name,
#                 'gender': gender,
#                 'phone_number': phone_number,
#                 'address': address,
#             }
#         )
#     return seller_info

# def add_seller():
    # cursor = sql().cursor()
    # query = ("insert into seller (seller_full_name, seller_user_name, seller_gender, seller_phone_number, seller_address) select full_name, user_name, gender, phone_number, address from users where users.type = 'Seller' and users.user_id = (select max(users.user_id) from users);")
    # cursor.execute(query)
    # sql().commit()

def show_type():
    cursor = sql().cursor()
    query = ("SELECT * FROM food_market.type;")
    cursor.execute(query)
    for i in cursor:
        print(i)

def show_unit():
    cursor = sql().cursor()
    query = ("SELECT * FROM food_market.unit;")
    cursor.execute(query)
    for i in cursor:
        print(i)

if __name__ == '__main__':
    connection = sql()
    '''product check'''
    # print(get_product_infos(1))
    # print(get_product_info(1,"name"))
    # print(get_all_products_infos())
    # insert_product(11)
    # delete_product(12)
    # print(sort_products('name'))
    # print(modify_product(6, 'quantity', 60))
    # print(search_products("o"))

    '''user check'''
    # print(get_existing_id("user")
    # print(get_user_infos(1))
    # print(get_user_info(1,"id"))
    # insert_user(4)
    # delete_user(19)


    # show_type()
    #show_unit()
