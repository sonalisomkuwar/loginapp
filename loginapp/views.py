from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import request
from loginapp.models import login
from idlelib.idle_test.mock_tk import Entry
from lib2to3.fixes.fix_input import context
from ctypes.test.test_pickling import name

# Create your views here.
def gmail_view(request):
    return render(request,"gmail.html")


def signin_view(request):
    #print("hello from view")
    return render(request, "abc.html")

def signup_view(request):
    return render(request, "sign_up.html")

    
'''
def data_from_view(request):
    #l=login()
    sign = login()
    for i in sign:
        una=request.POST["usaname"]
        pswa=request.POST["passwd"]
        
        #sign = login.objects.all()
        if sign.user_name==una and sign.password==pswa:
            return render(request,"inbox.html")
        else:
            return render(request,"error.html")
        
def data_from_view(request, user_name,password):
     user = User.objects.get(username=username)
8.    product = user.product_set.all()
9.    template = get_template('user_page.html')
10.  variables = Context({
                      'username': username,
                      'product': product
                      })
11.  output = template.render(variables)
12.  return HttpResponse(output)

 print(2)
    Login.save()
    print(3)
  
    if username == "SONALI" and password == "1234":
        return render(request,"inbox.html")
    else:
        return render(request,"error.html")

print(request.method)
    una=request.POST["usaname"]
    print(una)
    pswa=request.POST["passwd"]
    print(pswa)
    
    all_objects= login.objects.all()
    #for count in all_objects:
        all_objects.user_name="una1"
        print("una1")
        all_objects.password="pswa1" 
        print("pswa1") 
    #for i in all_objects:
        if (una == "una1") and (pswa=="pswa1"):
            return render(request, "inbox.html")
        else:    
            return render(request, "error.html")
        
'''       
        
def data_from_view(request):
    
    username = request.POST["usaname"]
    print(username)
    
    passrd = request.POST["passwd"]
    print(passrd)
    
    print(" I am in data from view")
    
    aa=login.objects.values_list('user_name','password')
    
    print(aa)
    
    for data in aa:
            name,paswd=data
            print(name)
            print(paswd)
            if (name==username and paswd==passrd):
                return render(request,"inbox.html")
    else:
        return render(request,"error.html")
            
             
    
    
   
   
def data_from_signup(request):
    print(request.method)
    un=request.POST["uname"]
    ps=request.POST["psw"]
    print(un)
    print(ps)
    Login=login()
    Login.user_name=un
    print(1)
    Login.password=ps
    print(3)
    Login.save()
    print(5)
    
    
'''   
def delete_from_view(request):
    if request.method == 'POST':
        login.objects.filter(id=id).delete()
        return redirect( 'gmail.html')
'''    
def login_members(request):
    members= login.objects.values('id','user_name','password')
    print(members)
    context= {'members': members  }
    return render(request, 'home.html', context)

def delete_members(request):
    idnumber=request.POST["id"]
    login.objects.filter(id=idnumber).delete()
    return render(request,"delete.html")

def update_members(request):
    ID=request.POST["id"]
    print("ID")
    a=login.objects.filter(id=ID)
    print(a)
    
    b=a.values_list('id','user_name','password')
    print(b)
    
    for data in b:
        id1,use,pas=data
        print(id1)
        print(use)
        print(pas)
    #print(i,u,p)
    dict={"in":id1,"us":use,"pa":pas}
    return render(request,"ud.html",dict)


def update_new(request):
    print(request.method)
    un=request.POST["usaname"]
    print(un)
    
    pw = request.POST["passwd"]
    print(pw)
    
    i=request.POST["ii"]
    print(i)
    
    n=login.objects.get(id=i)
    n.user_name=un
    n.password=pw
    n.save()
    return render(request,"update.html")
        
 
            
             
    
    
    
    
    
    
    