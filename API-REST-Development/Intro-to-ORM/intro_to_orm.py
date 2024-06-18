#ORM's are like a train and traditional SQL commands are like walking on foot


#Common SQLAlchemy Functions
    #create_engine()
        #establishes the connection to the database

        #like setting up main control panel in the station to communicate with different train lines (databases)

    #declarative_base()
        #creates a base class for all model classes

        #like designing a standard structure/template for all areas of the station

    #session management
        #manage database sessions, akin to handling the flow of passengers in and out of the station

#Flask-SQLAlchemy
    #extension for flask that adds support for SQLAlchemy

    #simplifies SQLAlchemy with Flask by adding helpful defaults and extra helpers

    #Common Flask-SQLAlchemy:
        #SQLAlchemy()
            #class is used to integrate SQLAlchemy with a Flask application

        #db.Model
            #inherited from SQLAlchemy, it represents the base class for models in Flask-SQLAlchemy

        #Configuration keys
            #various configuration options for Flask-SQLAlchemy, set via the Flask app's config

            #Key cofigurations
                #SQLALCHEMY_DATABASE_URI
                #SQLALCHEMY_BINDS
                #SQLALCHEMY_TRACK_MODIFICATIONS

#Key ORM Functions for data handling
    #.query - allows you to create query objects to retrieve data from the database

    #.all() - fetches all records from the database that meet the specifications specified in the query

    #filter_by() or .filter() - filerting of records based on specified conditions

    #.get()