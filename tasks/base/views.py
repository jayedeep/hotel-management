from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .forms import CreateUser,LoginUser,RestaurantsForm,FoodsForm,InvoiceForm
from django.contrib.auth.models import User
from .models import Restaurants,Foods,Invoice
from django.contrib.auth import login,logout,authenticate
from datetime import datetime
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def signup(request):
    if request.method=="POST":
        forms=CreateUser(request.POST)
        if forms.is_valid():
            password=forms.cleaned_data['password']
            password2= forms.cleaned_data['password2']
            username=forms.cleaned_data['username']
            email = forms.cleaned_data['email']
            if password==password2:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
            else:
                print("check your credential")
                return redirect('signup')
        else:
            forms = CreateUser()
            return render(request,'base/register.html',{"forms":forms})
    else:
        forms = CreateUser()
        return render(request, 'base/register.html', {"forms": forms})
    return render(request, 'base/register.html', {"forms": forms})

def Login(request):
    if request.method=="POST":
        forms=LoginUser(request.POST)
        if forms.is_valid():
            password=forms.cleaned_data['password']
            username=forms.cleaned_data['username']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                print('user is none')
                return redirect('login')
        else:
            print('form is in valid')
            return render(request, 'base/login.html', {"forms": forms})
    else:
        print('form is in valid2')
        forms=LoginUser()
        return render(request, 'base/login.html', {"forms": forms})
    return render(request, 'base/login.html', {"forms": forms})

def Logout(request):
    logout(request)
    return redirect('home')
#------------------------------------------------------------------------
def home(request):
    invoice=Invoice.objects.all()
    temp=[]
    for i in invoice:
        temp.append(i.datetime.year)
    temp=list(set(temp))
    context={'invoice':temp}
    return render(request,'base/index.html',context)
    # return render(request,'home.html',context)

def create_restaurant(request):
    if request.method=="POST":
        forms=RestaurantsForm(request.POST)
        if forms.is_valid():
            owner=request.user
            name=forms.cleaned_data['name']
            city = forms.cleaned_data['city']
            address = forms.cleaned_data['address']
            franchise = forms.cleaned_data['franchise']
            if not Restaurants.objects.filter(name=name).exists():
                restaurant=Restaurants.objects.create(owner=owner,name=name,city=city,address=address,franchise=franchise)
                restaurant.save()
                return redirect('list_rest')
            else:
                print("check your credential")
                return redirect('create_rest')
        else:
            forms = RestaurantsForm()
            return render(request,'base/create_rest.html',{"form":forms})
    else:
        forms = RestaurantsForm()
        return render(request, 'base/create_rest.html', {"form": forms})
    return render(request, 'base/create_rest.html', {"form": forms})

def list_restaurant(request):
    context={'restaurants':Restaurants.objects.filter(owner=request.user.id)}
    return render(request,'base/list_restaurant.html',context)

def update(request,id):
    # userdetail=User.objects.get(id=id)
    restaurantupadate=get_object_or_404(Restaurants,id=id)
    if request.method=="POST":
        forms=RestaurantsForm(request.POST,instance=restaurantupadate)
        if forms.is_valid():
            forms.save()
            return redirect("list_rest")
        else:
            print('data is in valid')
            return render(request,'base/update_rest.html',{"forms":forms})
    else:
        forms=RestaurantsForm(instance=restaurantupadate)
        return render(request,'base/update_rest.html',{"forms":forms})
    return render(request,'base/update_rest.html',{'forms':forms})


def delete(request,id):
    restaurant=get_object_or_404(Restaurants,id=id)
    restaurant.delete()
    return redirect('list_rest')

#----------------------------------------------------------------------------------
def create_food(request):
    restaurant = Restaurants.objects.filter(owner=request.user.id)
    if request.method=="POST":
        forms=FoodsForm(request.POST)
        if forms.is_valid():
            owner=request.user
            restaurant=forms.cleaned_data['restaurant']
            name=forms.cleaned_data['name']
            price = forms.cleaned_data['price']
            # created_at = forms.cleaned_data['created_at']
            print(owner,restaurant)
            food=Foods.objects.create(owner=owner,restaurant=restaurant,name=name,price=price)
            print('okay')
            food.save()
            return redirect('list_food')
        else:
            forms = FoodsForm()
            print("something problem here")
            return render(request,'base/create_food.html',{"form":forms,'restaurant':restaurant})
    else:
        forms = FoodsForm()
        return render(request, 'base/create_food.html', {"form": forms,'restaurant':restaurant})
    return render(request, 'base/create_food.html', {"form": forms,'restaurant':restaurant})

def list_food(request):
    # restaurant=Restaurants.objects.filter(owner=request.user.id)
    context={"foods":Foods.objects.filter(owner=request.user.id)}
    return render(request,'base/list_food.html',context)

def update_food(request,id):
    # userdetail=User.objects.get(id=id)
    restaurant = Restaurants.objects.filter(owner=request.user.id)
    foodupdate=get_object_or_404(Foods,id=id)
    if request.method=="POST":
        forms=FoodsForm(request.POST,instance=foodupdate)
        if forms.is_valid():
            forms.save()
            print('information saved')
            return redirect('list_food')
        else:
            print('data is in valid')
            return render(request,'base/update_food.html',{"forms":forms,'restaurant':restaurant})
    else:
        forms=FoodsForm(instance=foodupdate)
        return render(request,'base/update_food.html',{"forms":forms,'restaurant':restaurant})
    return render(request,'base/update_food.html',{'forms':forms,'restaurant':restaurant})


def delete_food(request,id):
    food=get_object_or_404(Foods,id=id)
    food.delete()
    return redirect('list_food')


#--------------------------------------------------------------------

def create_invoice(request):
    restaurant = Restaurants.objects.filter(owner=request.user.id)
    food = Foods.objects.filter(owner=request.user.id)

    if request.method=="POST":
        forms=InvoiceForm(request.POST)
        if forms.is_valid():
            owner=request.user
            restaurants=forms.cleaned_data['restaurants']
            table_no=forms.cleaned_data['table_no']
            foods=forms.cleaned_data['foods']
            datetime = forms.cleaned_data['datetime']
            totalbill=forms.cleaned_data['totalbill']

            food=Invoice.objects.create(owner=owner,table_no=table_no,restaurants=restaurants,foods=foods,datetime=datetime,totalbill=totalbill)
            print('okay')
            food.save()
            return redirect('list_invoice')
        else:
            forms = InvoiceForm()
            print("something problem here")
            return render(request,'base/create_invoice.html',{"form":forms,'restaurant':restaurant,'food':food})
    else:
        forms = InvoiceForm()
        return render(request, 'base/create_invoice.html', {"form": forms,'restaurant':restaurant,'food':food})
    return render(request, 'base/create_invoice.html', {"form": forms,'restaurant':restaurant,'food':food})


def list_invoice(request):
    invoice=Invoice.objects.filter(owner=request.user)
    context={'invoice':invoice}
    return render(request,'base/list_invoice.html',context)


def generateInvoice(request, id):
    foodDetail = Invoice.objects.get(id=id)
    data = io.BytesIO()
    pdf = canvas.Canvas(data)
    pdf.drawString(250, 650, "Your order invoice")

    pdf.drawString(50, 600, "Restaurant Name :")
    pdf.drawString(180, 600, str(foodDetail.restaurants))

    pdf.drawString(50, 570, "Food Name and Qty :")
    temp=",".join(foodDetail.foods)
    pdf.drawString(180, 570, str(temp))

    pdf.drawString(50, 550, "You Bought At:")
    pdf.drawString(180, 550, str(foodDetail.datetime))

    pdf.drawString(50, 520, "Customer were sit at :")
    pdf.drawString(180, 520, str(foodDetail.table_no)+" "+"table no.")

    pdf.drawString(50, 490, "Total Amount :")
    pdf.drawString(180, 490, str(foodDetail.totalbill))

    # pdf.drawString(50, 490, "Table NO. :")
    # pdf.drawString(130, 490, str(foodDetail.tableNo))
    #
    # pdf.drawString(50, 460, "Order Date :")
    # pdf.drawString(130, 460, str(foodDetail.orderDate))
    #
    # pdf.drawString(50, 430, "Order Time :")
    # pdf.drawString(130, 430, str(foodDetail.time))
    #
    # pdf.drawString(50, 400, "Total NO of items :")
    # pdf.drawString(160, 400, str(foodDetail.noOdItems))
    #
    # pdf.drawString(50, 370, "Total Bill :")
    # pdf.drawString(130, 370, str(foodDetail.totalBill))

    pdf.showPage()
    pdf.save()
    data.seek(0)
    return FileResponse(data, as_attachment=True, filename='invoice.pdf')

def charts_months(request,year):
    invoice=Invoice.objects.filter(owner=request.user,datetime__year=year)
    print(invoice)
    jan=[]
    feb = []
    mar = []
    apr = []
    may = []
    jun=[]
    jul=[]
    aug = []
    sep = []
    oct = []
    nov = []
    dec = []

    for inv in invoice:
        date_time_str=inv.datetime
        # date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        if date_time_str.month==1:
            jan.append(float(inv.totalbill))
        elif date_time_str.month==2:
            feb.append(float(inv.totalbill))
        elif date_time_str.month==3:
            mar.append(float(inv.totalbill))
        elif date_time_str.month==4:
            apr.append(float(inv.totalbill))
        elif date_time_str.month==5:
            may.append(float(inv.totalbill))
        elif date_time_str.month==6:
            jun.append(float(inv.totalbill))
        elif date_time_str.month==7:
            jul.append(float(inv.totalbill))
        elif date_time_str.month==8:
            aug.append(float(inv.totalbill))
        elif date_time_str.month==9:
            sep.append(float(inv.totalbill))
        elif date_time_str.month==10:
            oct.append(float(inv.totalbill))
        elif date_time_str.month==11:
            nov.append(float(inv.totalbill))
        elif date_time_str.month==12:
            dec.append(float(inv.totalbill))

    context={"datas":[sum(jan),sum(feb),sum(mar),sum(apr),sum(may),sum(jun),sum(jul),sum(aug),sum(sep),sum(oct),sum(nov),sum(dec)]}
    # print([sum(jan),sum(feb),sum(mar),sum(apr),sum(may),sum(aug),sum(sep),sum(oct),sum(nov),sum(dec)])
    return render(request,'base/charts.html',context)
