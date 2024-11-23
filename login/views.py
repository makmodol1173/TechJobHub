from django.shortcuts import redirect, render
import mysql.connector as sql
from django.urls import reverse

em=''
pwd=''

def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m= sql.connect(host="localhost",user="root",password="73060694moaz@",database="techjobhub")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t= tuple(cursor.fetchall())

        return redirect("/dashboard")

    return render(request,'Login.html')

