#this is the shebang line indicating the script should be run using Python3
#!/usr/bin/env python3

#randomint and choice are functions from the Python random module that are used to generate 
#random integers and make random selections from a list
from random import randint, choice as rc

#faker is a class from the Faker module  that is used to generate random fake data
from faker import Faker

#app is an instance of a Flask application ???????what does that mean??IT MEANS THAT I AM ACTUALLY IMPORTING APP FROM THE APP MODULE
from app import app

from models import db, Bakery, BakedGood

fake = Faker()

#this creates a context for the Flask app, whcih is necessary to interact with the db???????what does that mean??
with app.app_context():

    BakedGood.query.delete()
    Bakery.query.delete()
    
    bakeries = []
    for i in range(20):
        b = Bakery(
            name=fake.company()
        )
        bakeries.append(b)
    
    #i know this adds all the bakeries with the fake names we just created, but how and where does it add it?  
    #how does it know where to put it in our db.  Remember, db is just the access to all SQLAlchemy methods
    db.session.add_all(bakeries)

    baked_goods = []
    names = []
    for i in range(200):

        name = fake.first_name()
        while name in names:
            name = fake.first_name()
        names.append(name)

        bg = BakedGood(
            name=name,
            price=randint(1,10),
            bakery=rc(bakeries)
        )

        baked_goods.append(bg)

    db.session.add_all(baked_goods)
    db.session.commit()
    
    most_expensive_baked_good = rc(baked_goods)
    most_expensive_baked_good.price = 100
    db.session.add(most_expensive_baked_good)
    db.session.commit()

