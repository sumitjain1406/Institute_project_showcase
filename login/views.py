from django.shortcuts import render, redirect
from django.db import connection
import bcrypt

# Create your views here.


def login(request):
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        password = data.get("password")
        cur = connection.cursor()

        query = "select pass,role from user where email = %s"
        cur.execute(query, [email])
        try:
            data = cur.fetchall()
            if len(data) == 0:
                return render(request, "index.html", {"loginerror": True})

            db_password = data[0][0]
            db_role = data[0][1]

            correct = bcrypt.checkpw(
                password.encode("utf-8"), db_password.encode("utf-8")
            )

            if correct:
                request.session["email"] = email
                if db_role == "student":
                    return redirect("/student")
                else:
                    return redirect("/teacher")
        except:
            return render(request, "index.html", {"loginerror": True})
        cur.close()

        return render(request, "index.html", {"loginerror": True})


def register(request):
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        password = data.get("password")
        name = data.get("name")
        enrollment = data.get("enrollment")
        branch = data.get("branch")
        passout_year = data.get("year")
        role = "student"
        cur = connection.cursor()
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        cur.execute(f'select id from user where enrollment={enrollment};')
        data=cur.fetchall()
        if len(data)>0:
            return render(request,'invalidregister.html',{'message':'USER ALREADY EXIST'})
        cur.execute(f"select name from enrollment_list where ENROLLMENT_ID={enrollment};")
        data=cur.fetchall()
        if len(data)==0:
            return render(request,'invalidregister.html',{'message':'YOUR ENROLLMENT ID IS NOT REGISTER PLEASE CONTACT YOUR CC. '})
        query = """
            insert into user (email,pass,name,enrollment,branch,passout_year,role) values (%s,%s,%s,%s,%s,%s,%s);
        """
        cur.execute(
            query, [email, hashed, name, enrollment, branch, passout_year, role]
        )
        print([email, hashed, name, enrollment, branch, passout_year, role])
        cur.close()
        return redirect("/")
    return render(request, "register.html")


def logout(request):
    email=request.session.get("email")
    if email is not None:
        del request.session["email"]
    return redirect("/")
