from django.shortcuts import render
from polls.models import User
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse

def index(request) :
    
    str = request.GET.get("_id", None)
    
    if (str == None) :
        return HttpResponse("Enter some data please")
    else :
        return HttpResponse(str);
    
    
def bad_mofo(request) :
    return HttpResponse("How dare you call me mother fucker")


def save_user(request) :
    p_name = request.GET.get("name", None)
    p_age = request.GET.get("age", None)
    
    if (None == p_name or None == p_age) :
        return HttpResponse("Something is missing.")
    else :
        obj_user = User(name = p_name, age = p_age)
        obj_user.save()
        return HttpResponse("User saved.")  
        
def get_all_users(request) :

    data_dict = {}
    records=[]
    
    #data = User.objects.all()
    data = User.objects.raw("select * from polls_user where age > 10")
    
    for datum in data:
        name = datum.name
        age = datum.age
        record = {"name":name, "age":age}
        records.append(record)
        
    data_dict["users"] = records
    
    return JsonResponse(data_dict)

