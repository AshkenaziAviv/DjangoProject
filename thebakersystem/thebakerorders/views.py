from django.shortcuts import redirect, render
from .models import *
from .helper import *

# Create your views here.
def customers(request):
    if (request.method =='POST'):
        username = request.POST['username']
        if (request.POST['action'] == 'Order_Request') :
            return render(request,'order_request.html',{'items':show_all_items(username),'all_items':' '.join(show_all_items(username)),'username':username})
        elif(request.POST['action'] == 'AddItem') :
            return render(request,'additem.html',{'items':get_suitable_manu(username),'all_items':' '.join(show_all_items(username)),'username':username})
        elif (request.POST['action'] == 'LogOut') :
            return render(request,'logout.html',{'username':username})
    else:
        return render(request,'login.html')

def back_to_home(request):
    if (request.method =='POST'):
        username = request.POST['username']
        username = Customer.objects.get(id = get_user_id(username))
        username_orders = get_order(username.username)
        return render(request,'template.html',{'message':'hey, good to see you again','items':show_all_items(username.username),'username':username,'orders':username_orders})
    else:
        return render(request,'login.html')


def additem(request):
    if (request.method =='POST'):
        username = request.POST['username']
        if len(get_suitable_manu(username)) > 0 :
            username = Customer.objects.get(id = get_user_id(username))
            username_orders = get_order(username.username)
            if len(username.items) > 0 :
                username.items +=','+str(request.POST['action'])
                username.save()
                return render(request,'template.html',{'message':'hey, good to see you again','items':show_all_items(username.username),'username':username,'orders':username_orders})
            else :
                username.items +=str(request.POST['action'])
                username.save()
                return render(request,'template.html',{'message':'hey, good to see you again','items':show_all_items(username.username),'username':username,'orders':username_orders})
        else:
            return render(request,'status.html',{'message':'you already added all','username':username})
    else:
        return render(request,'login.html')


def sign_up(request):
     if (request.method =='POST'):
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        profile= Customer(name=name,username=username,email=email,password=password)
        profile.save()
        return redirect('/')
     else:
        return render(request,'signup.html')
    
def login(request):
     if (request.method =='POST'):
        username = request.POST['username']
        if username in get_all_users():
            password = request.POST['password']
            if password == get_user_password(username):
                pass
                if username in get_list_all_logged_users():
                    return render(request,'login.html',{'message':'user already login'})
                else:
                    update_log_value(username)
                    username = Customer.objects.get(id = get_user_id(username))
                    username_orders = get_order(username.username)
                    return render(request,'template.html',{'message':'hey, good to see you again','items':show_all_items(username.username),'username':username,'orders':username_orders})
            else:
                return render(request,'login.html',{'message':'Password is incorrect'})
        else:
            return render(request,'login.html',{'message':'UserName is incorrect'})
     else:
        return render(request,'login.html')
    
def logout(request):
    if (request.method =='POST'):
        username = request.POST['username']
        if username in get_all_users():
            pass
            if username in get_list_all_logged_users():
                password = request.POST['password']
                if password == get_user_password(username):
                    update_log_value(username)
                    return redirect('/')
                else:
                    return render(request,'logout.html',{'message':'Password is incorrect'})
            else:
                return render(request,'logout.html',{'message':'UserName is out'})
        else:
            return render(request,'logout.html',{'message':'UserName need to signup'})
    else:
        return render(request,'logout.html')


def add_order(request):
    if (request.method =='POST'):
        sender = request.POST['sender']
        if sender in get_all_users():
            duedate = request.POST['duedate']
            date = request.POST['date']
            description={}
            for item in show_all_items(sender):
                description[item]=eval(request.POST[str(item.strip())])
            sender = Customer.objects.get(id = get_user_id(sender))
            cost= get_order_cost(description)
            profile= Orders(sender=sender,description=description,duedate=duedate,date=date,cost=cost)
            profile.save()
            return render(request,'status.html',{'message':'Order number '+str(profile.id)+' is accepted','order':profile,'username':sender.username})
        else:
            return render(request,'order_request.html',{'message':'The users need to signup'})
    else:
        return render(request,'order_request.html')
