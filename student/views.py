from django.shortcuts import render, redirect
from django.db import connection
import bcrypt

# Create your views here.


def student(request):
    email = request.session.get("email")
    if email is not None:
        if request.method == "POST":
            data = request.POST
            Leader_Name = data.get("Lname")
            Teammate_Name = data.get("Tname")
            Project_Title = data.get("Title")
            Technology_stack = data.get("stack")
            Theme = data.get("Theme")
            Achievement = data.get("Achievement")

            Short_Description = data.get("desc")

            cur = connection.cursor()
            query = """
                    insert into view_projects (Leader_Name,Teammate_Name,Project_Title,Technology_stack,Theme,Achievement,Short_Description,email) 
                    values (%s,%s,%s,%s,%s,%s,%s,%s);
                """
            cur.execute(
                query,
                [
                    Leader_Name,
                    Teammate_Name,
                    Project_Title,
                    Technology_stack,
                    Theme,
                    Achievement,
                    Short_Description,
                    email,
                ],
            )
            cur.close()
            return redirect("/")
    cursor = connection.cursor()
    cursor.execute(f"select * from view_projects where email='{email}';")
    data = cursor.fetchall()
    cursor.close()
    if len(data) > 0:
        return render(request, "editproject.html", {"active": True, "data": data[0]})
    return render(request, "student.html", {"active": True})


def edit(request):
    email = request.session.get("email")
    if email is not None:
        if request.method == "POST":
            data = request.POST
            Leader_Name = data.get("Lname")
            Teammate_Name = data.get("Tname")
            Project_Title = data.get("Title")
            Technology_stack = data.get("stack")
            Theme = data.get("Theme")
            Achievement = data.get("Achievement")

            Short_Description = data.get("desc")

            cur = connection.cursor()
            query = """
                    update view_projects 
                    set Leader_Name=%s, 
                    Teammate_Name=%s,
                    Project_Title=%s,
                    Technology_stack=%s,
                    Theme=%s,
                    Achievement=%s,
                    Short_Description=%s 
                    where email=%s;
                """
            cur.execute(
                query,
                [
                    Leader_Name,
                    Teammate_Name,
                    Project_Title,
                    Technology_stack,
                    Theme,
                    Achievement,
                    Short_Description,
                    email,
                ],
            )
            cur.close()
            return redirect("/")
