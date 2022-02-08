from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index (request):
    return render(request, 'brandreg.html')

def brand_register(request):
    errors = Brand.objects.brand_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        brand = Brand.objects.create(
            company_name = request.POST['company_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['greeting'] = brand.company_name
        return redirect('/brands/dashboard')

def brand_login (request):
    return render(request, 'brandlogin.html')

def brand_auth(request):
    errors = Brand.objects.brand_authenticate(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = Brand.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        request.session['greeting'] = user.company_name
        return redirect('/brands/dashboard')

def index_two (request):
    return render(request, 'talentreg.html')

def talent_register(request):
    errors = Brand.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        talent = Talent.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['talent_id'] = talent.id
        request.session['greeting'] = talent.first_name
        return redirect('/talent/dashboard')

def talent_login (request):
    return render(request, 'talentlog.html')

def talent_auth(request):
    errors = Talent.objects.talent_authenticate(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        talent = Talent.objects.get(email=request.POST['email'])
        request.session['talent_id'] = talent.id
        request.session['greeting'] = talent.first_name
        return redirect('/talent/dashboard')

def brands_dash(request):
    context = {
        'talent_list': Talent.objects.all()
    }
    return render(request, 'brandsdash.html', context)

def talent_dash(request):
    context = {
        'brand_list': Brand.objects.all()
    }
    return render(request, 'talentdash.html', context)


def add_new(request):
    return render(request, 'newjob.html')

def create_job (request):
    user=Brand.objects.get(id=request.session['user_id'])
    Brand.objects.create(
    company_name = request.POST['company_name'],
    category = request.POST['category']),
    return redirect('/brands/dashboard')

def favorite (request, talent_id):
    user = Brand.objects.get(id=request.session['user_id'])
    talent = Talent.objects.get(id=talent_id)
    user.favorite_talent.add(talent)
    return redirect('/brands/favorite/{talent_id}')

def logout(request):
    request.session.flush()
    return redirect('/brands/login')
