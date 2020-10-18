from django.urls import path
from .views import home,signup,Login,Logout,delete,list_restaurant,charts_months,update,create_restaurant,create_food,list_food,update_food,delete_food,create_invoice,generateInvoice,list_invoice
urlpatterns = [
            path('', home,name='home'),

    path('signup/',signup,name='signup'),
    path('login/', Login, name='login'),
    path('logout/',Logout,name='logout'),

    path('create_rest/',create_restaurant,name='create_rest'),
    path('list_rest',list_restaurant,name='list_rest'),
    # path('detail/<int:id>/',detail, name='detail'),
    path('update_rest/<int:id>/',update, name='update_rest'),
    path('delete_rest/<int:id>/',delete, name='delete_rest'),

    path('create_food/',create_food,name='create_food'),
    path('list_food',list_food,name='list_food'),
    path('update_food/<int:id>/', update_food, name='update_food'),
    path('delete_food/<int:id>/', delete_food, name='delete_food'),

    path('invoice',create_invoice, name='create_invoice'),
    path('list_invoice',list_invoice,name='list_invoice'),
    path('generate_invoice/<int:id>', generateInvoice, name='generate_invoice'),

    path('charts_months/<int:year>/',charts_months,name='charts_months'),

]