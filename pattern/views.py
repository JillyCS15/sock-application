from pattern.models import SHACLPattern, ClassPattern
from django.shortcuts import render, redirect
from django.db import connection

def pattern_page(request):
    is_admin = False
    if request.user.is_superuser:
        is_admin = True
    
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM pattern_shaclpattern')
        list_shacl = dictfetchall(cursor)
        print("testing")
        print(list_shacl)
    context = {
        'list_shacl':list_shacl,
        "is_admin": is_admin,
    }
    return render(request, 'main/pattern-page.html', context)


def detail(request, code):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM pattern_shaclpattern')
        list_shacl = dictfetchall(cursor)
        print("testing")
        print(list_shacl)
    context = {
        'list_shacl':list_shacl
    }
    return render(request, 'main/pattern-page.html', context)



def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]