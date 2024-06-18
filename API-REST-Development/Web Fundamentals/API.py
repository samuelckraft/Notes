#internet is a vast space station that connects numerous planets (websites) via the internet with individuals represented by spacecraft

#when you type a web address in, a request is sent across channels to that specific server, which responds by sending back the necessary data for you to explore


#Web Architecture
    
    #monolithic
        #big, interconnected space station
        #easy to start, but as it grows maintaining and scaling becomes difficult; entire application apart of one unified codebase

    #service-oriented architecture (SOA)
        #space station with specialized big modules
        #large services communicate over a network
        #more manageable/scaleable than monolithic

    #microservices
        #space station with specialized small modules
        #each module operates independently, communicates efficiently and can be developed, deployed and scaled separately


#Communication methods

    #REST (Representational Estate Transfer)
        #universal language
        #uses HTTP methods and is the universal language keeping things simple and stateless

    #GraphQL
        #personalized talk with a planet
        #ask for specified data and it will give exactly that
        #all about efficient and precise data exchanges

    #gRPC (gRPC Remote procedure calls)
        #messages zipping through the station
        #made by google
        #great for speedy communication in things like microservices

    #WebSocket
        #two way communication channel
        #perfect for real time stuff like live streaming or online gaming where quick and steady data flow is key


#Creating virtual environment

    #make directory
        #mkdir venv_project

    #navigate to directory
        #cd venv_project

    #Creates the virtual environment
        #python -m venv myenv

    #Turns on the environment (creates symbol on left side to know you're in the virtual environment)
        #myenv\Scripts\activate
            #means anything you download in this environment is only in that environment



#Installing packages

    #pip install *package1* *package2*


#fetching and manipulating data from an API 
    #JSON (JavaScript Object Notation) - universal language of data exchange
        #written as key-value pairs (like dictionary)

        #converting JSON to python objects
            #see fetch_pokemon_json.py

