from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

# Create your models here.  


class User(AbstractUser):
	g = [('M','Male'),('F','Female'),('O','Others'),('SelectGender','---Select Gender---')]
	gender = models.CharField(default='SelectGender',choices=g,max_length=30)
	age = models.IntegerField(default=18)
	mobile_no = models.CharField(max_length=10)
	dob = models.DateField(null=True)
	pid_no=models.CharField(max_length=10,blank=True) 
	address_line1=models.CharField(max_length=200)
	address_line2=models.CharField(max_length=200)
	city=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	country=models.CharField(max_length=30)
	profile = models.ImageField(upload_to='profiles/',default='default.png')
	r = [(0,'guest'),(1,'user'),(2,'police')]
	role = models.IntegerField(choices=r,default=0)

class RoleRqst(models.Model):
	t=[(1,'user'),(2,'police')]
	uname= models.CharField(max_length=30)
	roletype = models.PositiveIntegerField(choices=t)
	proof = models.ImageField(upload_to='proof/',blank=True)
	is_checked=models.BooleanField(default=0)
	uid= models.OneToOneField(User,on_delete=models.CASCADE)

class AddCase(models.Model):
	case_title=models.CharField(max_length=20)
	case_date=models.DateField(auto_now_add=True)
	location=models.CharField(max_length=30)
	description=models.CharField(max_length=300)
	crime_proof=models.ImageField(blank=True)
	s=[(1,'In Progress'),(2,'Solved'),(3,'Pending'),(4,'Closed'),(5,'Applied')]
	update_status=models.IntegerField(choices=s,default=5)
	c=models.ForeignKey(User,on_delete=models.CASCADE)

class AddCriminal(models.Model):
	criminal_name=models.CharField(max_length=30)
	address_line1=models.CharField(max_length=200)
	address_line2=models.CharField(max_length=200)
	city=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	country=models.CharField(max_length=30)
	mobile_no = models.CharField(max_length=10)
	email=models.EmailField(max_length=50)
	g = [('M','Male'),('F','Female'),('O','Others'),('S','Select Gender')]
	gender = models.CharField(choices=g,default='S',max_length=15)
	dob = models.DateField(null=True)
	height=models.IntegerField(default=5)
	weight=models.IntegerField(default=35)
	identification=models.CharField(max_length=200)
	full_details=models.CharField(max_length=300,blank=True)
	criminal_photo=models.ImageField(blank=True)
	criminal_id=models.IntegerField(unique=True)

class AddCrime(models.Model):
	t=[('Rape','Rape'),('Dowry','Dowry'),('Petty Crime','Petty Crime'),('Taxi Scam','Taxi Scam'),('Arms Trafficking','Arms Trafficking'),('Domestic Violence','Domestic Violence'),('Illegal Drug Trade','Illegal Drug Trade'),('s','----Select----')]
	crime_type=models.CharField(max_length=50,choices=t,default='s')
	crime_date=models.DateField(blank=True)
	law=models.CharField(max_length=50)
	description=models.CharField(max_length=200)

class ComplaintBox(models.Model):
	p_name=models.CharField(max_length=100)
	p_email=models.EmailField(max_length=100)
	p_complaint=models.CharField(max_length=1000)
