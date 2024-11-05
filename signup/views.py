from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import mysql.connector as sql
fn=''
ln=''
em=''
pwd=''
r=''

# Create your views here.

def signaction(request):
    global fn,ln,em,pwd,r
    if request.method == 'POST':
        m= sql.connect(host="localhost",user="root",password="73060694moaz@",database="techjobhub")
        cursor = m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=="fname":
                fn=value
            if key=="lname":
                ln=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="role":
                r=value
        c= "insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,em,pwd,r)
        cursor.execute(c)
        m.commit()
        if m and (r=="Recruiter" or r=="Startup"):
            return redirect("/company-details")
        elif m and r=="Job Seeker":
            return redirect("/dashboard")
        else:
            return redirect('/login')
    return render(request,"Signup.html")

