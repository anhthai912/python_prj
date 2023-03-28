import sys

# enter folder location and change \ to //
sys.path.insert(1,'D://bi12-year2//advpython//project//python_prj//mysql_connect')
# access connect(model)
from connect import get_sql_connection as sql #type: ignore


#những fuction def t để trong """ thì đừng có chạy :)

product_info = []
person_info = []
store_creator_info = []
seller_info = []



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
    user_infos = {}
    for (user_id, full_name, user_name, password, gender, phone_number, address, type) in cursor:
        user_infos = {
            'id' : user_id,
            'full_name' : full_name,
            'user_name' : user_name,
            'password' : password,
            'gender' : gender,
            'phone_number' : phone_number,
            'address' : address,
            "user_type" : type
        }
    
    return user_infos

# get a specific info from an user
def get_user_info(get_id: int, select):
    # recall the function get_user_infos to create a dict and use 'select' to get a key from said dict
    return get_user_infos(get_id)[select]

# thg sơn lo nốt cái func này t lười r
'''
def get_all_users_infos():
    cursor = sql().cursor()
    query = "SELECT product.product_id, product.name, type.type_name, product.price_per_unit, unit.unit_name, product.quantity\
             FROM product INNER JOIN unit on product.unit_id = unit.unit_id\
             INNER JOIN type on product.type_id = type.type_id;"
    cursor.execute(query)    

    for (product_id, name, type_name, price_per_unit, unit_name, quantity, date_of_manufacture, date_of_expire, description) in cursor:
        product_info.append(
            {
                'product_id': product_id,
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

    return product_info
'''


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


# get all of a product information
def get_product_infos(get_id):
    cursor = sql().cursor()
    # sql command
    query = f"SELECT * FROM food_market.products WHERE product_id = {get_id};"
    cursor.execute(query)

    # get all of products's infos into a dict and return said dict
    product_infos = {}
    for (product_id, name, type_name, price_per_unit, unit_name, quantity, date_of_manufacture, date_of_expire, description) in cursor:
        product_infos = {
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

    return product_infos
    
        
# get product info
def get_product_info(get_id:int, select):
    # recall the dict created in function get_product_infos and use 'select' to get a key from the dict
    return get_product_infos(get_id)[select]




def get_all_products_infos():
    cursor = sql().cursor()
    query = "SELECT products.product_id, products.name, type.type_name, products.price_per_unit, unit.unit_name, products.quantity\
             FROM products INNER JOIN unit on products.unit_id = unit.unit_id\
             INNER JOIN type on products.type_id = type.type_id;"
    cursor.execute(query)    

    for (product_id, name, type_name, price_per_unit, unit_name, quantity, date_of_manufacture, date_of_expire, description) in cursor:
        product_info.append(
            {
                'product_id': product_id,
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

    return product_info


# delete a product
def delete_product(product_id: int):
    cursor = sql().cursor()
    query = f"DELETE FROM products WHERE product_id = {product_id};"
    cursor.execute(query)
    sql().commit()



#                                   SELLER

def get_seller_info():
    cursor = sql().cursor()
    query = "select full_name, user_name, gender, phone_number, address from users where users.type = 'Seller';"
    cursor.execute(query)
    for (full_name, user_name, gender, phone_number, address) in cursor:
        seller_info.append(
            {
                'full_name': full_name,
                'user_name': user_name,
                'gender': gender,
                'phone_number': phone_number,
                'address': address,
            }
        )
    return seller_info

def add_seller():
    cursor = sql().cursor()
    query = ("insert into seller (seller_full_name, seller_user_name, seller_gender, seller_phone_number, seller_address) select full_name, user_name, gender, phone_number, address from users where users.type = 'Seller' and users.user_id = (select max(users.user_id) from users);")
    cursor.execute(query)
    sql().commit()


    

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
    delete_product(16)

    '''user check'''
    # print(get_existing_id("user")
    # print(get_user_infos(1))
    # print(get_user_info(1,"id"))
    # insert_user(4)


    # show_type()
    #show_unit()

    """select max(person_id) from person;
    alter table person auto_increment = 11;"""