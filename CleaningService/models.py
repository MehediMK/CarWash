from django.db import models
from django.contrib import admin
from django.db.models.fields import URLField
from django.contrib.auth.models import User


# start service
class CleanningService(models.Model):
    SName = models.CharField(max_length=150,blank=False,verbose_name='Service Name')
    SDesc = models.TextField(max_length=350,blank=False,verbose_name='Description')
    SPrice = models.DecimalField(max_digits=5,decimal_places=2,blank=False,verbose_name='Service Price')
    SIcon = models.CharField(max_length=50,blank= True,default='flaticon-car-wash',verbose_name='Icon Class Name')
    SImage = models.ImageField(upload_to='serviceimage',blank=True,verbose_name='Service Image')

    def __str__(self):
        return self.SName
    
    def shotdesc(self):
        return self.SDesc[:100]


@admin.register(CleanningService)
class CustomeCleaning(admin.ModelAdmin):
    list_display = ('id', 'SName','SPrice')
    search_fields = ('id','SName','SPrice')
    list_display_links = ('id', 'SName')
    
# # end service area
CPSTATUS = (('BC','BASIC CLEANING'),('PC','PREMIUM CLEANING'),('COMPLEX CLEANING','COMPLEX CLEANING'))
class CleaningPlan(models.Model):
    CPName = models.CharField(max_length=100,blank=False,verbose_name='Cleaning Plan Name')
    CPPrice = models.DecimalField(max_digits=5,decimal_places=2,blank=False,verbose_name='Price')
    CPItems = models.ManyToManyField(CleanningService,verbose_name='Cleaning Items')
    CPStatus = models.CharField(max_length=60,blank=False,choices=CPSTATUS,default=CPSTATUS,verbose_name='Plan Status')
    CPFeatured = models.BooleanField(default=False,verbose_name='Featured')

    def __str__(self):
        return self.CPName

@admin.register(CleaningPlan)
class CustomeCleaning(admin.ModelAdmin):
    list_display = ('id', 'CPName','CPPrice','CPStatus','CPFeatured')
    search_fields = ('id', 'CPName','CPPrice','CPStatus','CPFeatured')
    list_display_links = ('id', 'CPName')
    list_editable = ('CPPrice','CPStatus','CPFeatured')

# Start ServicePoint
class ServicePoint(models.Model):
    SPName = models.CharField(max_length=100,blank=False,verbose_name='Shop Name')
    SPAddress = models.CharField(max_length=200,blank=False,verbose_name='Shop Address')
    SPPhone = models.CharField(max_length=16,blank=True,verbose_name='Phone Number')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.SPName    

@admin.register(ServicePoint)
class CustomeServicePoint(admin.ModelAdmin):
    list_display = ('id', 'SPName','SPAddress','SPPhone','active')
    search_fields = ('id', 'SPName','SPAddress','SPPhone','active')
    list_display_links = ('id', 'SPName')
    list_editable = ('SPAddress','SPPhone','active')
# End ServicePoint

class Employee(models.Model):
    EName = models.CharField(max_length=50,blank=False,verbose_name='Employee Name')
    Position = models.CharField(max_length=30,blank=False)
    Phone = models.CharField(max_length=16)
    ProfilePic = models.ImageField(upload_to='EProfilePic')
    Twitter = URLField(verbose_name='Twitter Profile URL')
    Facebook = URLField(verbose_name='Facebook Profile URL')
    Linkedin = URLField(verbose_name='Linkedin Profile URL')
    Instagram = URLField(verbose_name='Instagram Profile URL')

    def __str__(self):
        return self.EName
    
@admin.register(Employee)
class CustomeEmployee(admin.ModelAdmin):
    list_display = ('id', 'EName','Position','Phone')
    search_fields = ('id', 'EName','Position','Phone')
    list_display_links = ('id', 'EName')
    list_editable = ('Position','Phone')


class Testimonial(models.Model):
    CName = models.CharField(max_length=40,verbose_name='Client Name',blank=False)
    CProfession = models.CharField(max_length=70, blank=True,verbose_name='Client Profession')
    CImage = models.ImageField(upload_to='ClientImage',default='profile.png',verbose_name='Client Image')
    CComment = models.TextField(max_length=300,blank=False,verbose_name='Client Comment')
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.CName

    def comment(self):
        return self.CComment[:100]


@admin.register(Testimonial)
class CustomeTestimonial(admin.ModelAdmin):
    list_display = ('id','CName','CProfession','CComment','Status')
    search_fields = ('CName','CProfession','Status')
    list_display_links = ('id','CName')
    list_editable = ('CProfession','Status')


class Carousel(models.Model):
    Catitle = models.CharField(max_length=100,verbose_name='Title',blank=False)
    CaSubTitle = models.CharField(max_length=150,verbose_name='Subtitle',blank=False)
    CaImage = models.ImageField(upload_to='carousel',verbose_name='Image',default='carousel.jpg')
    CaDesc = models.TextField(max_length=300,verbose_name='Description',blank=False)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Catitle

    def desc(self):
        return self.CaDesc[:100]


@admin.register(Carousel)
class CustomeCarousel(admin.ModelAdmin):
    list_display = ('id','Catitle','CaSubTitle','Status')
    search_fields = ('Catitle','CaSubTitle','Status')
    list_display_links = ('id','Catitle')
    list_editable = ('CaSubTitle','Status')



class AboutUs(models.Model):
    Auser = models.OneToOneField(User,on_delete=models.CASCADE,default='1')
    Atitle = models.CharField(max_length=100,verbose_name='Title',blank=False)
    SItem = models.ManyToManyField(CleanningService,verbose_name='Service Items',blank=False)
    AImage = models.ImageField(upload_to='carousel',verbose_name='Image(H:650px,W:600px)',default='carousel.jpg')
    ADesc = models.TextField(max_length=300,verbose_name='Description',blank=False)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Atitle

    def desc(self):
        return self.ADesc[:150]


@admin.register(AboutUs)
class CustomeAboutUs(admin.ModelAdmin):
    list_display = ('id','Auser','Atitle','Status')
    search_fields = ('Auser','Atitle','Status')
    list_display_links = ('id','Auser')
    list_editable = ('Atitle','Status')


class Office(models.Model):
    Ouser = models.OneToOneField(User,on_delete=models.CASCADE,default='1')
    Office_name = models.CharField(max_length=100,verbose_name='Office Name',blank=True)
    Office_location = models.CharField(max_length=100,verbose_name='Office Location',blank=True)
    Day_time = models.CharField(max_length=100,blank=False,verbose_name='Office Day and Time')
    Number = models.CharField(max_length=15,blank=True,verbose_name='Quick Contact Number')
    Email = models.EmailField()
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Day_time

admin.site.register(Office) 
