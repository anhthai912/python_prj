import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='food_market')
    return __cnx


#bỏ """ để tạo bảng và print data vào bảng
#tạo xong bảng thì đặt lại vào """

"""

  CREATE TABLE `food_market`.`unit` (
  `unit_id` INT NOT NULL AUTO_INCREMENT,
  `unit_name` VARCHAR(100) NULL,
  PRIMARY KEY (`unit_id`));

  CREATE TABLE `food_market`.`type` (
  `type_id` INT NOT NULL AUTO_INCREMENT,
  `type_name` VARCHAR(100) NULL,
  PRIMARY KEY (`type_id`));

  CREATE TABLE `food_market`.`product` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `type_id` INT NULL,
  `price_per_unit` double NULL,
  `unit_id` INT NULL,
  `quantity` INT NULL,
  `date_of_manufacture` varchar(100) NULL,
  `date_of_expire` varchar(100) NULL,
  `description` varchar(100) NULL,
  PRIMARY KEY (`product_id`));

CREATE TABLE `food_market`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(100) NULL,
  `user_name` VARCHAR(100) NULL,
  `password` VARCHAR(100) NULL,
  `gender` VARCHAR(45) NULL,
  `phone_number` INT NULL,
  `address` VARCHAR(100) NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`));

CREATE TABLE `food_market`.`seller` (
  `seller_id` INT NOT NULL AUTO_INCREMENT,
  `seller_full_name` VARCHAR(100) NULL,
  `seller_user_name` VARCHAR(100) NULL,
  `seller_gender` VARCHAR(45) NULL,
  `seller_phone_number` INT NULL,
  `seller_address` VARCHAR(100) NULL,
  PRIMARY KEY (`seller_id`));

INSERT INTO `food_market`.`seller` (`seller_id`, `seller_full_name`, `seller_user_name`, `seller_gender`, `seller_phone_number`, `seller_address`) VALUES ('1', 'James Smith', 'James', 'Male', '2147483647', 'Broadway');
INSERT INTO `food_market`.`seller` (`seller_id`, `seller_full_name`, `seller_user_name`, `seller_gender`, `seller_phone_number`, `seller_address`) VALUES ('2', 'John', 'Williams', 'Male', '956456555', 'St. Mark\'s Place');
INSERT INTO `food_market`.`seller` (`seller_id`, `seller_full_name`, `seller_user_name`, `seller_gender`, `seller_phone_number`, `seller_address`) VALUES ('3', 'David', 'Jones', 'Male', '955765354', 'Washington Street');
INSERT INTO `food_market`.`seller` (`seller_id`, `seller_full_name`, `seller_user_name`, `seller_gender`, `seller_phone_number`, `seller_address`) VALUES ('4', 'Patricia', 'Miller', 'Female', '325754754', 'Crosby Street');
INSERT INTO `food_market`.`seller` (`seller_id`, `seller_full_name`, `seller_user_name`, `seller_gender`, `seller_phone_number`, `seller_address`) VALUES ('5', 'Linda', 'Rodriguez', 'Female', '923123412', 'Riverside Drive');


INSERT INTO `food_market`.`unit` (`unit_id`, `unit_name`) VALUES ('1', 'each');
INSERT INTO `food_market`.`unit` (`unit_id`, `unit_name`) VALUES ('2', 'g');
INSERT INTO `food_market`.`unit` (`unit_id`, `unit_name`) VALUES ('3', 'kg');



INSERT INTO `food_market`.`type` (`type_id`, `type_name`) VALUES ('1', 'meat');
INSERT INTO `food_market`.`type` (`type_id`, `type_name`) VALUES ('2', 'seafood');
INSERT INTO `food_market`.`type` (`type_id`, `type_name`) VALUES ('3', 'dry_food');
INSERT INTO `food_market`.`type` (`type_id`, `type_name`) VALUES ('4', 'spices');
INSERT INTO `food_market`.`type` (`type_id`, `type_name`) VALUES ('5', 'snacks');
INSERT INTO `food_market`.`type` (`type_id`, `type_name`) VALUES ('6', 'drinks');
INSERT INTO `food_market`.`type` (`type_id`, `type_name`) VALUES ('7', 'fruit');
INSERT INTO `food_market`.`type` (`type_id`, `type_name`) VALUES ('8', 'vegetable');


INSERT INTO `food_market`.`product` (`product_id`, `name`, `type_id`, `price_per_unit`, `unit_id`, `quantity`, `date_of_manufacture`, `date_of_expire`) VALUES ('1', 'pork', '1', '14', '2', '24', '2022-12-12', '2022-12-30');
INSERT INTO `food_market`.`product` (`product_id`, `name`, `type_id`, `price_per_unit`, `unit_id`, `quantity`, `date_of_manufacture`, `date_of_expire`) VALUES ('2', 'apple', '7', '5', '3', '52', '2022-12-12', '2022-12-30');
INSERT INTO `food_market`.`product` (`product_id`, `name`, `type_id`, `price_per_unit`, `unit_id`, `quantity`, `date_of_manufacture`, `date_of_expire`) VALUES ('3', 'chocolate', '5', '6', '1', '25', '2022-12-12', '2022-12-30');
INSERT INTO `food_market`.`product` (`product_id`, `name`, `type_id`, `price_per_unit`, `unit_id`, `quantity`, `date_of_manufacture`, `date_of_expire`) VALUES ('4', 'broccoli', '8', '2', '2', '245', '2022-12-12', '2022-12-30');
INSERT INTO `food_market`.`product` (`product_id`, `name`, `type_id`, `price_per_unit`, `unit_id`, `quantity`, `date_of_manufacture`, `date_of_expire`) VALUES ('5', 'fish', '2', '10', '2', '23', '2022-12-12', '2022-12-30');
INSERT INTO `food_market`.`product` (`product_id`, `name`, `type_id`, `price_per_unit`, `unit_id`, `quantity`, `date_of_manufacture`, `date_of_expire`) VALUES ('6', 'cooking oil', '4', '4', '1', '56', '2022-12-12', '2022-12-30');
INSERT INTO `food_market`.`product` (`product_id`, `name`, `type_id`, `price_per_unit`, `unit_id`, `quantity`, `date_of_manufacture`, `date_of_expire`) VALUES ('7', 'pepper', '4', '2', '2', '76', '2022-12-12', '2022-12-30');
INSERT INTO `food_market`.`product` (`product_id`, `name`, `type_id`, `price_per_unit`, `unit_id`, `quantity`, `date_of_manufacture`, `date_of_expire`) VALUES ('8', 'sticky rice', '3', '4', '3', '23', '2022-12-12', '2022-12-30');
INSERT INTO `food_market`.`product` (`product_id`, `name`, `type_id`, `price_per_unit`, `unit_id`, `quantity`, `date_of_manufacture`, `date_of_expire`) VALUES ('9', 'milk', '6', '2', '1', '78', '2022-12-12', '2022-12-30');
INSERT INTO `food_market`.`product` (`product_id`, `name`, `type_id`, `price_per_unit`, `unit_id`, `quantity`, `date_of_manufacture`, `date_of_expire`) VALUES ('10', 'orange', '7', '6', '3', '25', '2022-12-12', '2022-12-30');


INSERT INTO `food_market`.`users` (`user_id`, `full_name`, `user_name`, `password`, `gender`, `phone_number`, `address`, `type`) VALUES ('1', 'James Smith', 'James', '123', 'Male', '2147483647', 'Broadway', 'Seller');
INSERT INTO `food_market`.`users` (`user_id`, `full_name`, `user_name`, `password`, `gender`, `phone_number`, `address`, `type`) VALUES ('2', 'Robert', 'Johnson', '1234', 'Male', '2147483647', 'Park Avenue', 'Customer');
INSERT INTO `food_market`.`users` (`user_id`, `full_name`, `user_name`, `password`, `gender`, `phone_number`, `address`, `type`) VALUES ('3', 'John', 'Williams', '12345', 'Male', '956456555', 'St. Mark's Place', 'Seller');
INSERT INTO `food_market`.`users` (`user_id`, `full_name`, `user_name`, `password`, `gender`, `phone_number`, `address`, `type`) VALUES ('4', 'Michael', 'Brown', '123456', 'Male', '987648477', '5th Avenue', 'Customer');
INSERT INTO `food_market`.`users` (`user_id`, `full_name`, `user_name`, `password`, `gender`, `phone_number`, `address`, `type`) VALUES ('5', 'David', 'Jones', '1234567', 'Male', '955765354', 'Washington Street', 'Seller');
INSERT INTO `food_market`.`users` (`user_id`, `full_name`, `user_name`, `password`, `gender`, `phone_number`, `address`, `type`) VALUES ('6', 'Mary', 'Garcia', '12345678', 'Female', '324654677', 'Wall Street', 'Customer');
INSERT INTO `food_market`.`users` (`user_id`, `full_name`, `user_name`, `password`, `gender`, `phone_number`, `address`, `type`) VALUES ('7', 'Patricia', 'Miller', '123456789', 'Female', '325754754', 'Crosby Street', 'Seller');
INSERT INTO `food_market`.`users` (`user_id`, `full_name`, `user_name`, `password`, `gender`, `phone_number`, `address`, `type`) VALUES ('8', 'Jennifer', 'Davis', '1234567890', 'Female', '931234123', 'Doyers Street', 'Customer');
INSERT INTO `food_market`.`users` (`user_id`, `full_name`, `user_name`, `password`, `gender`, `phone_number`, `address`, `type`) VALUES ('9', 'Linda', 'Rodriguez', '12345678901', 'Female', '923123412', 'Riverside Drive', 'Seller');
INSERT INTO `food_market`.`users` (`user_id`, `full_name`, `user_name`, `password`, `gender`, `phone_number`, `address`, `type`) VALUES ('10', 'Elizabeth', 'Martinez', '123456789012', 'Female', '324235642', 'Prospect Park West', 'Customer');


INSERT INTO `food_market`.`seller` (`seller_id`, `seller_full_name`, `seller_user_name`, `seller_gender`, `seller_phone_number`, `seller_address`) VALUES ('2', 'John', 'Williams', 'Male', '956456555', 'St. Mark\'s Place');
INSERT INTO `food_market`.`seller` (`seller_id`, `seller_full_name`, `seller_user_name`, `seller_gender`, `seller_phone_number`, `seller_address`) VALUES ('3', 'David', 'Jones', 'Male', '955765354', 'Washington Street');
INSERT INTO `food_market`.`seller` (`seller_id`, `seller_full_name`, `seller_user_name`, `seller_gender`, `seller_phone_number`, `seller_address`) VALUES ('4', 'Patricia', 'Miller', 'Female', '325754754', 'Crosby Street');
INSERT INTO `food_market`.`seller` (`seller_id`, `seller_full_name`, `seller_user_name`, `seller_gender`, `seller_phone_number`, `seller_address`) VALUES ('5', 'Linda', 'Rodriguez', 'Female', '923123412', 'Riverside Drive');



"""