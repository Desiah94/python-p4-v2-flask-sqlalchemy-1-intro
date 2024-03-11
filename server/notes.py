# It takes 4 parts to define a model in FLASK-SQLALCHEMY
# -inheritence from db.model class
# a __tablename__ class attribute
# one or more class attributes assigned to the db.Column
# One class attribute specified to be the tables Primary Key
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData

# contains definitions of tables and associated schema constructs
# read more about Metadata using the link at the bottom of the page
# metadata = MetaData()

# create the Flask SQLAlchemy extension
# db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.
# class Pet(db.Model):
#     __tablename__ = 'pets'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     species = db.Column(db.String)
