from django.shortcuts import render, redirect
from .forms import Patientsform
from .models import patients
from django.http import JsonResponse
from maxapp import models
#   Serverside Datatables Packages

# from django_serverside_datatable.views import ServerSideDatatableView
from django_serverside_datatable.views import datatable
from django.views import View
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet

# Create your views here.


def index(request):  
    if request.method == 'POST':
        ptfrm = Patientsform(request.POST)
        if ptfrm.is_valid():
            ptfrm.save()
    return render(request, 'index.html')


def showdata(request):
    # ptfrm=patients.objects.all().order_by('-id').values()

    return render(request, 'showdata.html')
    # ,{'ptfrm':ptfrm}


def update(request, id):
    ptdata = patients.objects.get(id=id)
    if request.method == 'POST':
        ptfrm = Patientsform(request.POST)
        if ptfrm.is_valid():
            ptfrm = Patientsform(request.POST, instance=ptdata)
            ptfrm.save()
            print("Record updated successfully")
            return redirect('showdata')
        else:
            print(ptfrm.errors)

    return render(request, 'update.html', {'ptdata': patients.objects.get(id=id)})


def deletedata(request, id):
    ptdata = patients.objects.get(id=id)
    patients.delete(ptdata)
    return redirect('showdata')


# class ItemListView(ServerSideDatatableView,JsonResponse):
# 	queryset = models.patients.objects.all()
# 	data = ['id','fname','lname','gender']

# Class for loading serverside datatables...

class ServerSideDatatableView(View):
    queryset = models.patients.objects.all()
    data = ['id', 'fname', 'lname','dob', 'gender']
    # model = patients

    def get(self, request, *args, **kwargs):
        result = datatable.DataTablesServer(
            request, self.data, self.get_queryset()).output_result()
        return JsonResponse(result, safe=False)

    def get_queryset(self):
      
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )

        return queryset


# class ItemListView(ServerSideDatatableView):
# 	queryset = models.patients.objects.all()
# 	columns = ['id','fname','lname','dob','gender']
