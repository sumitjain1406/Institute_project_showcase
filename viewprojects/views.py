from django.shortcuts import render, HttpResponse
from django.db import connection

# Create your views here.


def view_projects(request):
    cursor = connection.cursor()
    cursor.execute(
        "select view_projects.id,Leader_Name,Teammate_Name,Project_Title,Technology_stack,Theme,Short_Description,Achievement,branch,passout_year,view_projects.email from view_projects inner join user on view_projects.email=user.email where Achievement is NOT NULL;"
    )
    data = cursor.fetchall()
    cursor.close()
    return render(request, "viewprojects.html", {"data": data})


def search(request):
    if request.method == "POST":
        data = request.POST
        dropdown = data.get("dropdown")
        search_value = data.get("search").lower()
        cursor = connection.cursor()
        cursor.execute(
            f"select view_projects.id,Leader_Name,Teammate_Name,Project_Title,Technology_stack,Theme,Short_Description,Achievement,branch,passout_year,view_projects.email from view_projects  inner join user on view_projects.email=user.email where  LOWER({dropdown}) LIKE '{search_value}%';"
        )
        data = cursor.fetchall()
        cursor.close()
        return render(request, "viewprojects.html", {"data": data})


def all(request):
    cursor = connection.cursor()
    cursor.execute(
        "select view_projects.id,Leader_Name,Teammate_Name,Project_Title,Technology_stack,Theme,Short_Description,Achievement,branch,passout_year,view_projects.email from view_projects inner join user on view_projects.email=user.email;"
    )
    data = cursor.fetchall()
    cursor.close()
    return render(request, "viewprojects.html", {"data": data})
