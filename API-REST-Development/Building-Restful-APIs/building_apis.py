#RESTful services adhere to a "Uniform interface" (RESTful web services is a music festival)
    #get (request a song)
        #retrieves resource
        #guaranteed to not cause side-effect
        #cacheable

    #post (add song to playlist)
        #creates a new resource
        #unsafe, effect of this verb isn't defined by http

    #put (change song version)
        #updates existing resource
        #used for resource creation when client knows URI
        #can call it N times, same thing will always happen
    
    #delete (remove a song from the list)
        #removes resource
        #can call N times, same thing will always happen

#stateless operation
    #each request from a client to a server must contain all the info necessary to complete the request

#Flask (organizer of a small music stage (can host wide range of performances from solos (basic web pages) to small band gigs (complex web apps)))

    #Flask-Marshmallow - extension for flask used for object serialization and deserialization; provides validation ensuring data fits formatting
    #easy to set up and perfect for hosting a wide range of web applications 
from flask import Flask
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
ma = Marshmallow(app)


    #when you launch a flask app, it initiates a local server, acting as the control hub
        #server manages incoming HTTP requests (think song requests, artist updates, or cancellations) and sends back the right responses

    #localhost - refers to the device running the server
        #accessing localhost in a web browser means communicating with the flask server on your machine
        #127.0.0.1 is the loopback IP address corresponding to the hostname 'localhost'
            #when running flask it runs on http://127.0.0.1:5000 or http://localhost:5000 indicating the flash server is operational and can be accessed via this specific internal address

#routing - process of defining URLs (paths) that direct to specific functions
    #@app.route('/')
        #default route 
        #defines the root of the web application and is the most basic and essential route, representing the home page or starting point

        #e.g.
            #@app.route('/customers', methods=['GET']) - for retrieving customer info

            #@app.route('/customers', methods=['PUT']) - for updating specific customer info


#endpoint design
    #like planning the layout and activities of each stage of the music festival
    #involves what each part of the festival (application) should do and how it should be accessed

    #endpoint refers to a specific "target" within a web app that performs a certain function
        #endpoints are often named for their functionality (e.g. add_customer, delete_customer)

        #endpoints are associated with functions; when defining a route you can specify an endpoint name or Flask will just use the name of the function as the endpoint


#Status codes
    #200 - ok
    #201 - created
    #204 - no content
    #400 - bad request
    #401 - unauthorized
    #403 - forbidden
    #404 - not found
    #500 - internal server eror API