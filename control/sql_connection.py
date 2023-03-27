import sys

# enter folder location and change \ to //
sys.path.insert(1,'D://bi12-year2//advpython//project//python_prj//mysql_connect')
# access connect(model)
from connect import get_sql_connection as sql


#những fuction def t để trong """ thì đừng có chạy :)

product_info = []
person_info = []
store_creator_info = []
seller_info = []

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
    phone_number = int(input("Enter phone numer: "))
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
    query = ("INSERT INTO product (product_id, name, type_id, price_per_unit, unit_id, quantity, date_of_manufacture, date_of_expire, description)\
             VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
    data = (product_id, name, type_id, price_per_unit, unit_id, quantity, date_of_manufacture, date_of_expire, description)
    cursor.execute(query, data)
    sql().commit()


# get all of a product information
def get_product_infos(get_id):
    cursor = sql().cursor()
    # sql command
    query = f"SELECT * FROM food_market.product WHERE product_id = {get_id};"
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




def get_all_products_infos(connection):
    cursor = connection.cursor()
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


"""def get_person_info(connection):
    cursor = connection.cursor()
    query = "select person.person_id, person.first_name, person.last_name, person_type.person_type_name, person.address, person.phone_number from person inner join person_type on person.person_type_id = person_type.person_type_id;"
    cursor.execute(query)
    for (person_id, first_name, last_name, person_type_name, address, phone_number) in cursor:
        person_info.append(
            {
                'person_id': person_id,
                'first_name': first_name,
                'last_name': last_name,
                'person_type_name': person_type_name,
                'address': address,
                'phone_number': phone_number,
            }
        )
    return person_info
"""

def get_seller_info(connection):
    cursor = connection.cursor()
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

def add_seller(connection):
    cursor = connection.cursor()
    query = ("insert into seller (seller_full_name, seller_user_name, seller_gender, seller_phone_number, seller_address) select full_name, user_name, gender, phone_number, address from users where users.type = 'Seller' and users.user_id = (select max(users.user_id) from users);")
    cursor.execute(query)
    connection.commit()

"""def get_store_creator_info(connection):
    cursor = connection.cursor()
    query = "select first_name, last_name, address, phone_number from person where person_type_id = 1;"
    cursor.execute(query)
    for (person_id, first_name, last_name, address, phone_number) in cursor:
        store_creator_info.append(
            {
                'person_id': person_id,
                'first_name': first_name,
                'last_name': last_name,
                'address': address,
                'phone_number': phone_number,
            }
        )
    return store_creator_info
"""
"""def insert_person(connection):
    cursor = connection.cursor()

    first_name = str(input("Enter your first name: "))
    last_name = str(input("Enter your last name: "))
    person_type_id = int(input("Enter your id (1 if you are a seller, 2 if you are a customer): "))
    address = str(input("Enter your address: "))
    phone_number = int(input("Enter your phone number: "))
    
    query = ("insert into person (first_name, last_name, person_type_id, address, phone_number) value (%s, %s, %s, %s, %s);")
    data = (first_name, last_name, person_type_id, address, phone_number)
    cursor.execute(query, data)
    connection.commit()
    if person_type_id == 1:
        add_creator(connection)
    else:
        pass 

def add_creator(connection):
    cursor = connection.cursor()
    query = ("insert into creator (first_name, last_name, address, phone_number) select first_name, last_name, address, phone_number from person where person.person_type_id = 1 and person.person_id = (select max(person.person_id) from person);")
    cursor.execute(query)
    connection.commit()
"""
"""# do not use this function :)
def delete_person(connection):
    cursor = connection.cursor()
    first_name = str(input("Enter first name: "))
    last_name = str(input("Enter last name: "))
    query = ("DELETE FROM person where first_name = %s and last_name = %s;")
    data = (first_name, last_name,)
    cursor.execute(query, data)
    connection.commit()"""


    
"""# do not use this function :)
def delete_product(connection):
    cursor = connection.cursor()
    name = str(input("Enter the product's name: "))
    query = ("DELETE FROM product where name = %s;")
    data = (name,)
    cursor.execute(query, data)
    connection.commit()"""

def show_type(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM food_market.type;")
    cursor.execute(query)
    for i in cursor:
        print(i)

def show_unit(connection):
    cursor = connection.cursor()
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

    '''user check'''
    # print(get_user_infos(1))
    # print(get_user_info(1,"password"))
    # insert_user(4)


    # show_type(connection)
    #show_unit(connection)

    """select max(person_id) from person;
    alter table person auto_increment = 11;"""