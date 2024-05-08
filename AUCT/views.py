from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# For book
def index(request: HttpRequest, id:int, name:str, price:int) -> HttpResponse:
    return render(request, 'index.html', {'id':id, 'name':name, 'price':price,} )

def booking(request):
    if request.method == 'GET': 
        id = request.GET.get('id')
        name = request.GET.get('name')
        price = request.GET.get('price')  
    elif request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
    else:
        id, name, price = None, None, None

    if id is not None and name is not None and price is not None:
        with open('book_info.txt', 'a') as f:
            f.write(f"{id}, {name}, {price}\n")    
    return render(request, 'index.html', {'id':id, 'name':name, 'price':price})





# for auto
def auto(request: HttpRequest, id:int, name:str, price:int, year:int, detail:str, color:int) -> HttpResponse:
    return render(request, 'auto.html', {'id':id, 'name':name, 'price':price, 'year':year, 'detail:':detail, 'color':color} )

def autodetail(request):
    if request.method == 'GET': 
        id = request.GET.get('id')
        name = request.GET.get('name')
        price = request.GET.get('price')
        year = request.GET.get('year')
        detail = request.GET.get('detail')
        color = request.GET.get('color')  
    elif request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
    else:
        id, name, price, year, detail, color = None, None, None, None, None, None

    if id is not None and name is not None and price is not None and year is not None and detail is not None and color is not None:
        with open('auto_detail.txt', 'a') as f:
            f.write(f"{id}, {name}, {price}$, {year}, {detail}, #{color}\n")    
    return render(request, 'auto.html', {'id':id, 'name':name, 'price':price, 'year':year, 'detail':detail, 'color':color})





# for HUMANITY
def inf(request: HttpRequest, id:int, f_name:str, l_name:str, country:str, age:int, family_member:int, fav_subject:str, fav_color:int) -> HttpResponse:
    return render(request, 'human.html', {'id':id, 'f_name':f_name, 'l_name':l_name, 'country':country, 'age':age, 'family_member':family_member, 'fav_subject':fav_subject, 'fav_color':fav_color} )

def humanity(request):
    if request.method == 'GET': 
        id = request.GET.get('id')
        f_name = request.GET.get('f_name')
        l_name = request.GET.get('l_name')
        country = request.GET.get('country')
        age = request.GET.get('age')
        family_member = request.GET.get('family_member')
        fav_subject = request.GET.get('fav_subject')
        fav_color = request.GET.get('fav_color')  
    elif request.method == 'POST':
        id = request.POST.get('id')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
    else:
        id, l_name, f_name, country, age, family_member, fav_subject, fav_color = None, None, None, None, None, None, None, None

    if id is not None and f_name is not None and l_name is not None and country is not None and age is not None and family_member is not None and fav_subject is not None and fav_color is not None:
        with open('human_info.txt', 'a') as f:
            f.write(f"{id}, {f_name}, {l_name}, {country}, {age}, {family_member}, {fav_subject}, {fav_color}\n")    
    return render(request, 'human.html', {'id':id, 'f_name':f_name, 'l_name':l_name, 'country':country, 'age':age, 'family_member':family_member, 'fav_subject':fav_subject, 'fav_color':fav_color})
