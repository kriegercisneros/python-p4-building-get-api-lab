# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# from sqlalchemy_serializer import SerializerMixin

# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })

# db = SQLAlchemy(metadata=metadata)

# class Bakery(db.Model, SerializerMixin):
#     __tablename__ = 'bakeries'

#     #adding this to add rules for our serializer to follow
#     serialize_rules =('-baked_goods.bakery',)

#     id = db.Column(db.Integer, primary_key=True)
#     #here unique=True means that the corresponding db column should not allow duplicate values
#     name = db.Column(db.String, unique=True)
#     #this is a function provided by the sqlalchemy that generates a database-specific sql expression represeting the current timestamp
#     #in sqlalchemy, server_default is an argumentthat can be passed to the COlumn constructor to provide a default valuse for a column at the db server level
#     #the db server will use this default as the value for the column if not other is specified.  This is helpful 
#     #because the default value is set at the database level so it is not necessary to do it in the code

#     #the func module is part of the sqlalchemy core and provides a collections of functions that generate sql expressions
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     #in sqlalchemy, onupdate is an argument that can be passed to the column constructor to specifiy a default value that should be used for the 
#     # column when it is updated.  
#     updated_at = db.Column(db.DateTime, onupdate=db.func.now())
#     #relationship function is used to define a relationship between two database tables.  it is typically defined on the model class of 
#     #table that is on the many side of the relationship and takes several args to specify the details.  The first arg is the name of the target 
#     #model class, BakedGood, this tells SQLAlchemy that the baked_goods relationship links to the BakedGood model
#         #the backref arg is used to define a ref back from the BakedGood model to the Bakery model.  It creates a new attribute on 
#         #the BakedGood model the refers back to the Bakery model.  the attribute is named bakery and can be used to access the bakery associated with a particular
#         #BakedGood obj
#         #why do i describe a relationship here and a foreign key downthere?
#     baked_goods = db.relationship('BakedGood', backref='bakery')

#     #this returns a string as a representation of the object.  Ideally, it is information-rich and could be used to recreate
#     #an objuect with the same value.  it is a python function
#     def __repr__(self):
#         return f'<Bakery {self.name}>'

# class BakedGood(db.Model, SerializerMixin):
#     __tablename__ = 'baked_goods'

#     serialize_rules=('-bakery.baked_goods',)

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, unique=True)
#     price = db.Column(db.Integer)
#     created_at =db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime, onupdate=db.func.now())

#     #this is making a new column with the bakery_id as a foreignKey
#     bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))

#     def __repr__(self):
#         return f'<Baked Good {self.name}, ${self.price}>'

# #dont forget to set up the environment in the server folder
#     #export FLASK_APP=app.py
#     #export FLASK_RUN_PORT = 5555
# #FLASK_APP is the variable that tells Flask which file contains the Flask application.  
# # In this case, the Flask app is located in the app.py file.  setting it equal to app.py 
# #tells flask to look for the application in that file
# #FLASK_RUN_PORT is the variable that specifies the port on which the flask application will run

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    serialize_rules = ('-baked_goods.bakery',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    baked_goods = db.relationship('BakedGood', backref='bakery')

    def __repr__(self):
        return f'<Bakery {self.name}>'

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    serialize_rules = ('-bakery.baked_goods',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))

    def __repr__(self):
        return f'<Baked Good {self.name}, ${self.price}>'