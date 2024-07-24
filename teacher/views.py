from django.shortcuts import render , HttpResponse, redirect
# Create your views here.
import pandas as pd 
from django.db import connection


def teacher(request):
    
    email = request.session.get("email")
    if email is not None:
        cursor = connection.cursor()
        cursor.execute("select * from enrollment_list;")
        data = cursor.fetchall()
        cursor.close()
        return render(request, 'teacher.html', {"active": True,"data":data})
    return redirect("/")





def enroll(request):
    email = request.session.get("email")
    if email is None:
        return redirect("/")
    data=[]
    if request.method=="POST":
        cursor = connection.cursor()
        cursor.execute("select * from enrollment_list;")
        data = cursor.fetchall()
        cursor.close()
        temp = request.FILES['enroll'] # this is my file
        df = pd.read_csv(temp)
        cursor = connection.cursor()
        for index, row in df.iterrows():
            cursor.execute(
                "INSERT INTO ENROLLMENT_LIST (ENROLLMENT_ID, NAME) VALUES (%s, %s)",
            (row['ENROLLMENT_ID'], row['NAME'])
            )
        connection.commit()
        cursor.close()
    return render(request, 'teacher.html', {"active": True,"data":data})

