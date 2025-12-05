#Data models
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from datetime import datetime

db=SQLAlchemy()

#First entity
class User_Info(db.Model):
    __tablename__="user_info"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String,unique=True,nullable=False)
    password=db.Column(db.String,nullable=False)
    role = db.Column(db.Enum("admin", "user","professional", name="role_enum"), default="user", nullable=False)
    full_name=db.Column(db.String,nullable=False)
    status = db.Column(Enum("active", "block", name="status_enum"), nullable=False, default="active")
    tickets=db.relationship("User_Info",cascade="all,delete",backref="user_info",lazy=True) #User can access all of his tickets

    
    
#Entity 2  serviceprof 
class ServiceProf(db.Model):
    __tablename__="serviceprof"
    prof_id=db.Column(db.Integer, db.ForeignKey("user_info.id"),nullable=False)
    experience = db.Column(db.String(200), nullable=False, default="No experience")
    service_type = db.Column(
    db.Enum("Plumbing", "Electrical", "Carpentry", "Other", name="service_type_enum"), 
    nullable=False, 
    default="Other"
    )
    rating = db.Column(db.Float, nullable=False, default=0.0)
    shows=db.relationship("Show",cascade="all,delete",backref="theatre",lazy=True) #Theatre can access all of its shows
    


#Entity3 service
class Service(db.Model):
    __tablename__="service"
    service_id=db.Column(db.Integer,primary_key=True)
    base_price = db.Column(db.Float, nullable=False, default=0.0)  # Price for the service
    time_required = db.Column(db.Integer, nullable=False, default=0)  # Time in minutes
    description = db.Column(db.String(500), nullable=False, default="No description provided")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Timestamp when service is created
    shows=db.relationship("Show",cascade="all,delete",backref="theatre",lazy=True) #Theatre can access all of its shows

#Entity4 customer
class Customer(db.Model):
    __tablename__="customer"
    customer_id=db.Column(db.Integer, db.ForeignKey("user_info.id"),nullable=False)
    tickets=db.relationship("Ticket",cascade="all,delete",backref="show",lazy=True) #Show can access its tickets
  


#Entity 5 service request
class Servicereq(db.Model):
    __tablename__="servicereq"
    request_id=db.Column(db.Integer,primary_key=True)
    customer_id=db.Column(db.Integer, db.ForeignKey("customer.id"),nullable=False)
    service_id=db.Column(db.Integer, db.ForeignKey("service.id"),nullable=False)
    prof_id=db.Column(db.Integer, db.ForeignKey("serviceprof.id"),nullable=False)
    status = db.Column(Enum("requested", "assigned","closed", name="status_enum"), nullable=False, default="closed")
    date_of_req = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Request date
    date_of_completion = db.Column(db.DateTime, nullable=True)  # Completion date
    remarks = db.Column(db.String(500), nullable=True, default="No remarks provided")  # Remarks for the request

    tickets=db.relationship("Ticket",cascade="all,delete",backref="show",lazy=True) #Show can access its tickets
  

#Entity 6 review
class Review(db.Model):
    __tablename__="review"
    review_id=db.Column(db.Integer,primary_key=True)
    customer_id=db.Column(db.Integer, db.ForeignKey("customer.id"),nullable=False)
    request_id=db.Column(db.Integer, db.ForeignKey("servicereq.id"),nullable=False)
    prof_id=db.Column(db.Integer, db.ForeignKey("serviceprof.id"),nullable=False)
    rating = db.Column(db.Float, nullable=False)  # Rating out of 5 or any scale
    comments = db.Column(db.String(500), nullable=True, default="No comments provided")  # User comments
    review_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Date when the review is posted



    """