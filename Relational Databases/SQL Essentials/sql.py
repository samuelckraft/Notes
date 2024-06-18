#DDL (Data Definition Language) - consists of commands to create, modify, and remove database objects like tables, indexes and users


        #Creating database
    #create database e_commerce_db;

    # use e_commerce_db;
        #Creating tables/columns/rows
    # CREATE TABLE Customers (
    # 	id INT auto_increment PRIMARY KEY,
    #     name VARCHAR(255) NOT NULL,
    #     email varchar(255) NULL
    # );

    # create TABLE Orders(
    # 	id INT auto_increment primary key,
    #     date DATE NOT NULL,
    #     customer_id int,
    #     foreign key (customer_id) references Customers(id)
    # );

        #modifying existing tables
    # alter table Customers
    # add phone VARCHAR(15);

    # alter table Customers
    # modify email VARCHAR(320);

        #removing tables/databases
    #drop table Customers;

    #drop database e_commerce_db;



#Core DML (Data Manipulation Data) commands

    #Insert

    # insert into {Table Name} ('column 1', 'column 2', 'column 3')
    # values ('value for column 1', 'value for column 2', 'value for column 3');


        # insert into Customers (name, email, phone)
        # values ('Sam Kraft', 'samuelckraft@gmail', '615-651-4354');
    #            ('John Smith', 'test@test.com', '123-456-5555');

    #Update

    # update {Table Name}
    # set {column} = {value}, {column} = {value}
    # where {location};

        # update Customers
        # set name = 'John Johnson', email = 'kraft@gmail.com'
        # where id = 2;

    #Delete

    #delete from {Table Name}
    #where {location}
            # delete from Customers
            # where id = 3;


    # set SQL_SAFE_UPDATES = 0; #this turns off safe updates meaning you can delete multiple rows at once
    # delete from {Table Name}
    # where email is null; #selects every column with a null email and deletes it
    # set SQL_SAFE_UPDATES = 1; #this turns it back on

        # set SQL_SAFE_UPDATES = 0;
        # delete from Customers
        # where email is null;
        # set SQL_SAFE_UPDATES = 1;



#Data Query Language (DQL)

    #select * from {table name} #shows everything in a given table
        #select * from Customers

    #select {column 1}, {column 2} from {Table Name} #displays only the select columns
        #select name, email from Customers

    #select {specific columns or *} from {table name}
    #where {column} is/is not/= {criteria}
        #select * from customers
        #where name = 'Sam Kraft'

    #can use multiple criteria for "where" function
        #and
            #where name = 'Sam Kraft' and email = 'samuelckraft@gmail.com'

        #or
            #where name = 'Sam Kraft' or number = '123-456-5666'

        #not
            #where name not 'Sam Kraft'

    #Order by - allows us to sort data (Ascending (ASC) or Descending (DESC))

    # select * from customers
    # order by name ASC #sorts names from A-Z

    # select * from customers
    # order by id desc #sorts by largest to smallest id


    #Distinct command - filters out any duplicates
    #select distinct email from Customers;


    #Like function - looks for a pattern
        #select * from {Table name}
        #where {column} like {criteria}

            #criteria
                #% sign acts like a wild card ('J%' or '%e' will pull words that start with J or ends with e)


    #in function - selects specific values/items

        #select * from customers
        #where id in (4,5)

    #between function 
        # select * from customers
        # where id between 1 and 5


    #Number functions

    #min/max - returns smallest or highest; also sorts alphabetical

        #select min/max({column}) from {table name}


    #count function

        #select count({criteria}) from {table name}

    #average

        #select average({criteria}) from {table name}




#Crafting data relationships

#inserting
    # insert into orders (date, customer_id)
    # values('2023-07-15', 1),
    # ('2023-12-13', 1),
    # ('2023-10-15', 5)


#updating
    # update orders
    # set date = '2024-10-04'
    # where id = 7

#deleting

    # delete from orders
    # where customer_id = 5 and id = 7

#selecting

    # select o.id as OrderID, o.date as OrderDate, c.id as CustomerID, c.name, c.email
    # from customers c, orders o
    # where c.id = o.customer_id

