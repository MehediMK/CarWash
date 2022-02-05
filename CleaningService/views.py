from django.shortcuts import render
from .models import CleanningService,CleaningPlan,ServicePoint,Employee,Testimonial,Carousel,AboutUs,Office


def home(request):
    context = {}

    service = CleanningService.objects.all()
    context['services'] = service

    office = Office.objects.all()
    context['offices'] = office

    plan = CleaningPlan.objects.all()
    context['plans'] = plan
    
    servicePoints = ServicePoint.objects.all()
    context['servicePoints'] = servicePoints

    count_servicePoints = ServicePoint.objects.all().count()
    context['countSevice_point'] = count_servicePoints
    
    employees = Employee.objects.all()
    context['employees'] = employees

    count_employees = Employee.objects.all().count()
    context['count_employees'] = count_employees
    
    testimonial = Testimonial.objects.filter(Status=True)
    context['testimonials'] = testimonial
    
    carousel = Carousel.objects.filter(Status=True)
    context['carousels'] = carousel
    
    aboutus = AboutUs.objects.filter(Status=True).filter(Auser__username = 'admin').first()
    context['aboutus'] = aboutus


    return render(request,'Homepage/index.html',context)


def aboutus(request):
    context = {}

    office = Office.objects.all()
    context['offices'] = office
    
    aboutus = AboutUs.objects.filter(Status=True).filter(Auser__username = 'admin').first()
    context['aboutus'] = aboutus

    employees = Employee.objects.all()
    context['employees'] = employees

    count_employees = Employee.objects.all().count()
    context['count_employees'] = count_employees

    count_servicePoints = ServicePoint.objects.all().count()
    context['countSevice_point'] = count_servicePoints


    return render(request,'AboutUs/aboutus.html',context)

def services(request):
    context = {}

    office = Office.objects.all()
    context['offices'] = office

    service = CleanningService.objects.all()
    context['services'] = service

    testimonial = Testimonial.objects.filter(Status=True)
    context['testimonials'] = testimonial
    return render(request,'Services/services.html',context)

def prices(request):
    context = {}

    office = Office.objects.all()
    context['offices'] = office

    plan = CleaningPlan.objects.all()
    context['plans'] = plan
    return render(request,'Prices/price.html',context)

def teams(request):
    context = {}

    office = Office.objects.all()
    context['offices'] = office
    
    employees = Employee.objects.all()
    context['employees'] = employees
    
    return render(request,'Team/team.html',context)

def contacts(request):
    context = {}

    office = Office.objects.all()
    context['offices'] = office

    return render(request,'Contact/contact.html',context)

def washingPoints(request):
    context = {}

    office = Office.objects.all()
    context['offices'] = office

    servicePoints = ServicePoint.objects.all()
    context['servicePoints'] = servicePoints
    return render(request,'WashingPoints/washingPoints.html',context)

def blog(request):
    return render(request,'Blog/blog.html')

def blogDetails(request):

    return render(request,'Blog/blogDetails.html')


