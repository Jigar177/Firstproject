
from django.urls import path
from maxapp import views
urlpatterns = [
    path('', views.index),
    path('showdata/', views.showdata ),
    path('update/<int:id>', views.update),
    path('deletedata/<int:id>', views.deletedata),
    #Json Response
    #path('json/', views.patients_json),
    path('data/', views.ServerSideDatatableView.as_view()), 

]   
