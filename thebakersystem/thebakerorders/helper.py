from unicodedata import name
from .models import *

def get_all_users():
    query=Customer.objects.raw("SELECT * \
                                    FROM thebakerorders_Customer")
    list_of_usernames=[]
    for user in query:
        list_of_usernames.append(user.username)
    return list_of_usernames

def get_user_id(username):
    query = Customer.objects.raw("SELECT * \
                                    FROM thebakerorders_Customer \
                                    WHERE username=%s",[username])
    query= list(query)
    if len(query) == 0 :
        return -1
    else:
        return query[0].id

def get_item_id(item_name):
    query = Items.objects.raw("SELECT * \
                                    FROM thebakerorders_Items \
                                    WHERE name=%s",[item_name])
    query= list(query)
    if len(query) == 0 :
        return -1
    else:
        return query[0].id


def get_user_password(username):
    query = Customer.objects.raw("SELECT * \
                                    FROM thebakerorders_Customer \
                                    WHERE username=%s",[username])
    query= list(query)
    if len(query) == 0 :
        return -1
    else:
        return query[0].password


def get_all_logged_users():
    query=Customer.objects.raw("SELECT * \
                                    FROM thebakerorders_Customer \
                                        WHERE log=True")
    return query

def get_list_all_logged_users():
    query=Customer.objects.raw("SELECT * \
                                    FROM thebakerorders_Customer \
                                        WHERE log=True")
    list_of_logged_usernames=[]
    for user in query:
       list_of_logged_usernames.append(user.username)
    return list_of_logged_usernames
    

def update_log_value(username):
    user = Customer.objects.get(id = get_user_id(username))
    if user.log == False :
        user.log = True
    else:
        user.log = False
    user.save()

def show_all_items(username):
    username = Customer.objects.get(id = get_user_id(username))
    list_of_items= username.items.split(",")
    return list_of_items

def get_order(sender_username):
    sender_id= get_user_id(sender_username)
    query = Orders.objects.filter(sender = sender_id)
    return query

def get_item(item_name):
    item_id= get_item_id(item_name)
    query = Items.objects.filter(id = item_id)
    return query[0]

def get_menu():
    query=Items.objects.raw("SELECT * \
                                    FROM thebakerorders_Items")
    list_of_Items=[]
    for item in query:
        list_of_Items.append(item.name)
    return list_of_Items

def get_suitable_manu(username):
    item_of_username=show_all_items(username)
    item_from_menu=get_menu()
    item_not_in_username=[]
    for item in item_from_menu :
        if item in item_of_username :
            continue
        else:
            item_not_in_username.append(item)
    return item_not_in_username

def get_order_cost(dict):
    cost=0
    for key, value in dict.items():
        cost +=int(get_item(key).price) * int(value)
    return cost    
