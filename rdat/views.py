from django.shortcuts import render
from .models import *

def index(request):
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    state = State.objects.all()
    companydetail = CompanyDetail.objects.all()
    job = Job.objects.all()

    context = {'category':category,'subcategory':subcategory, 'state':state, 'companydetail':companydetail,'job':job

    }
    return render(request, 'index.html', context)
