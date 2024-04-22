from django.shortcuts import render
from django.views.generic import View
from data_management.models import Summary
# Create your views here.


class DashboardMainView(View):
    def get(self,request):
        summary = Summary.objects.all()
        return render(request,'dashboard.html',context={'summary_data':summary})
