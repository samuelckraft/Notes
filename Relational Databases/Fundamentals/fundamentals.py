#relational vs non-relational

    #relational database - data is structured in rows and columns; tables intercommunicate in specific information
        #columns (shows row data in a structured way) make up rows (each serve distinct function), rows make up tables, tables make up relational database
            #in the city analogy, database is a city, table is a building, row is a room and columns are individuals

        #keys
            #primary keys - identifies each row, ensuring that, inside a table, they are one of a kind

            #foreign key - coherent, interconnected relationship between rows from different tables

        #constraints
            #unique constraints - highlights differences betweeen tables (tables facade identifiable features), preventing any two tables from being indistinguishable

            #non-null constraints - mandatory alignments for every table (foundation of every structure, cannot be omited if the building is to stand)

            #check constraints - setting specific parameters within which data must fall (zoning laws of the city)

            #default value - basic means for tables to exist (the standard mailbox issued to every building)

        #relationships
            #one-to-one - exclusive sky bridge that links two skyscrapers; ensures that each entity in one table is intricately linked to a single entity in another

            #one-to-many - like a bustling main road, connecting a hub to many destinations

            #many-to-many - town square where paths intersect, coordinating a web of connections

            #self referencing - hall of mirrors, like an organizational chart reflecting back within itself

        #normalization - involves structuring data to reduce redundancy and improve data integrity
            #organizing data into two tables; dividing a database into two or more tables and defining relationships between them
            #objective is to isolate data so that modifications can be made
            #ensures clarity, reduces overlap, and makes maintenance manageable

            #Levels of normalization
                #First normal form (1NF) - table is 1NF if it contains no repeating groups of data; each column cannot be further divided and each row should be unique

                #Second normal form (2NF) - if it is in 1NF and all non-key attributes are functional and dependent on the primary key; each piece of info is stored in only one place

                #Third normal form (3NF) - if it is in 2NF and all its attributes are not fully functionally dependent on the primary key but also non-transitively dependent; everything should be directly related to the primary key


    #non-relational database - data lounging in documents, key-value pairs and wide-columns; provides more flexibility


#database management systems (DBMS)

    #MySQL - lively center of data city; caters to a wide range of needs, from small websites to large-scale enterprise applications
        #best for dealing with large datasets (web applications, content management systems, and e-commerce platforms)

    #PostgreSQL - high-speed bullet train; powers complex queries and demanding workloads; developers who need advanced data manipulation, strict adherence to standards, and robust extensibility use this for its technical prowess
        #best when working with data complexity that requires robust query power (geospatial data, scientific research and analytical workloads)

    #Oracle - wall street; known for security, scalability, and robust enterprise features; securely stores critical info and transactions for large corps. and gov intstitutes
        #best for highlighting scalability and security  (enterprise-level projects that handle massive amounts of data and complex transactions)

    #SQLite - embedded database; ideal for mobile apps and small desktop programs; compact size and ease of use make it good for smaller projects but not large scale
        #best when looking for simplicity and portability; requires separate server setup


#Entity Relationship diagrams (ERDs)
    #provide a visual representation (like a map) of the relationships between different buildings (entities) and the paths (relationships) that connect them

    #entities - primary objects in ERDs are like the various buildings or landmarks in the city; typically represent a table (like Customers and Orders can be two entities in an e-commerce database)

    #attributes - details of an entity (characteristics of a building); Customers entity might have attributes like ID, Name, Email, etc.

    #relationships - define how entities interact with each other (roads and paths between buildings); Place Order relationship might connect customers to Orders
