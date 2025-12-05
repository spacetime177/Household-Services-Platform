#App routes
from flask import Flask,render_template,request,url_for,redirect
from .models import *                   
from flask import current_app as app
from sqlalchemy import func
from werkzeug.utils import secure_filename
from flask import url_for



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login",methods=["GET","POST"])
def signin():
    if request.method=="POST":
        uname=request.form.get("user_name")
        pwd=request.form.get("password")
        usr=User_Info.query.filter_by(email=uname,password=pwd).first()
        if usr and usr.role==0: #Existed and admin
            return redirect(url_for("admin_dashboard",name=uname))

    return render_template("login.html",msg="")
    
@app.route("/register",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        uname=request.form.get("user_name")
        pwd=request.form.get("password") 
        full_name=request.form.get("full_name")
        address=request.form.get("location")
        pin_code=request.form.get("pin_code")
        usr=User_Info.query.filter_by(email=uname).first()
        if usr:
            return render_template("signup.html",msg="Sorry, this mail already registered!!!")
        new_usr=User_Info(email=uname,password=pwd,full_name=full_name,address=address,pin_code=pin_code)
        db.session.add(new_usr)
        db.session.commit()
        return render_template("login.html",msg="Registration successfull, try login now")
    
    return render_template("signup.html",msg="")


@app.route("/admin/<name>")
def admin_dashboard(name):
    theatres=get_theatres()
    return render_template("admin_dashboard.html",name=name,theatres=theatres)
@app.route("/user/<id>/<name>")
def user_dashboard(id,name):
    theatres=get_theatres()
    dt_time_now=datetime.today().strftime('%Y-%m-%dT%H:%M')
    dt_time_now=datetime.strptime(dt_time_now,"%Y-%m-%dT%H:%M")
    return render_template("user_dashboard.html",uid=id,name=name,theatres=theatres,dt_time_now=dt_time_now)

#Many controllers/routers here
@app.route("/venue/<name>",methods=["POST","GET"])
def add_venue(name):
    if request.method=="POST":
        vname=request.form.get("name")
        location=request.form.get("location")
        pin_code=request.form.get("pin_code")
        capacity=request.form.get("capacity")
        file=request.files["file_upload"]
        url=""
        if file.filename:
            file_name=secure_filename(file.filename) #Verification of the file is done
            url='./uploaded_files/'+vname+"_"+file_name
            file.save(url)
        new_theatre=Theatre(name=vname,location=location,pin_code=pin_code,capacity=capacity,venue_pic_url=url)
        db.session.add(new_theatre)
        db.session.commit()
        return redirect(url_for("admin_dashboard",name=name))
    
    return render_template("add_venue.html",name=name)

@app.route("/show/<venue_id>/<name>",methods=["POST","GET"])
def add_show(venue_id,name):
    if request.method=="POST":
        sname=request.form.get("name")
        tags=request.form.get("tags")
        tkt_price=request.form.get("tkt_price")
        date_time=request.form.get("dt_time") #data is string format
        #print(date_time)
        #processing date/time
        dt_time=datetime.strptime(date_time,"%Y-%m-%dT%H:%M")
        new_show=Show(name=sname,tags=tags,tkt_price=tkt_price,date_time=dt_time,theatre_id=venue_id)
        db.session.add(new_show)
        db.session.commit()
        return redirect(url_for("admin_dashboard",name=name))
    
    return render_template("add_show.html",venue_id=venue_id,name=name)
        

@app.route("/search/<name>",methods=["GET","POST"])
def search(name):
    if request.method=="POST":
        search_txt=request.form.get("search_txt")
        by_venue=search_by_venue(search_txt)
        by_location=search_by_location(search_txt)
        if by_venue:
            return render_template("admin_dashboard.html",name=name, theatres=by_venue)
        elif by_location:
            return render_template("admin_dashboard.html",name=name, theatres=by_location)

    return redirect(url_for("admin_dashboard",name=name))

@app.route("/edit_venue/<id>/<name>",methods=["GET","POST"])
def edit_venue(id,name):
    v=get_venue(id) 
    if request.method=="POST":
        tname=request.form.get("tname")
        location=request.form.get("location")
        pin_code=request.form.get("pin_code")
        capacity=request.form.get("capacity")
        v.name=tname
        v.location=location
        v.pin_code=pin_code
        v.capacity=capacity
        db.session.commit()
        return redirect(url_for("admin_dashboard",name=name))
    
    return render_template("edit_venue.html",venue=v,name=name)

@app.route("/delete_venue/<id>/<name>",methods=["GET","POST"])
def delete_venue(id,name):
    v=get_venue(id) 
    db.session.delete(v)
    db.session.commit()
    return redirect(url_for("admin_dashboard",name=name))

@app.route("/edit_show/<id>/<name>",methods=["GET","POST"])
def edit_show(id,name):
    s=get_show(id) 
    if request.method=="POST":
        sname=request.form.get("mname")
        tags=request.form.get("tags")
        tkt_price=request.form.get("tkt_price")
        date_time=request.form.get("dt_time") #data is string format
        dt_time=datetime.strptime(date_time,"%Y-%m-%dT%H:%M")
        s.name=sname
        s.tags=tags
        s.tkt_price=tkt_price
        s.date_time=dt_time
        db.session.commit()
        return redirect(url_for("admin_dashboard",name=name))
    
    return render_template("edit_show.html",show=s,name=name)