from django.shortcuts import render,redirect
from CrimeReportingSystem.forms import UserRegistrationForm,CaseupdateForm,ChangepassForm,UserupdateForm1, UserupdateForm2,RoleR,RoleUp,AddcaseForm,AddcriminalForm1,AddcriminalForm2,ComplaintForm,AddcrimeForm
from CrimeReportingSystem.models import User,RoleRqst,AddCase,AddCriminal,ComplaintBox,AddCrime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here. 
def home(request):
	return render(request,'html/home.html')

def aboutus(request):
	return render(request,'html/aboutus.html')

def contactus(r):
    return render(r,'html/contactus.html')

def login_page(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(request,username=username,password=password)

		if not user:
			messages.add_message(request,messages.WARNING,'invalid username/password')
			return render(request,'html/login.html')
		else:
			login(request,user)
		# 	messages.add_message(request,messages.INFO,f'Welcome {user.username}')
			return redirect('/dash')
	return render(request,'html/login.html')
 
def register(r):
	if r.method == "POST":
		p=UserRegistrationForm(r.POST)
		if p.is_valid():
			p.save()
			return redirect('/login')
			password1=r.POST.get('password1')
			password2=r.POST.get('password2')

			user=authenticate(r,password1=password1,password2=password2)
			if not user:
				messages.add_message(r,messages.WARNING,'passwords are not matching, please enter password correctly...')
				return render(r,'html/register.htmlm',{'u':p})

	p=UserRegistrationForm()
	return render(r,'html/register.html',{'u':p})

@login_required
def profile(r):
	return render(r,'html/profile1.html')

@login_required
def dashboard(r):
	return render(r,'html/dashboard.html')

@login_required
def rolereq(request):
	if request.method== "POST":
		k =RoleR(request.POST,request.FILES)
		if k.is_valid():
			s=k.save(commit=False)
			s.uname= request.user.username
			s.uid_id= request.user.id
			s.save()
			return redirect('/dash')
	k=RoleR()
	return render(request,'html/rolereq.html',{'a':k})

@login_required
def permissions(request):
	ty=User.objects.all()
	a=RoleRqst.objects.all()
	c,rr=[],{}
	for b in a:
		c.append(b.uid_id)
	for j in ty:
		if j.is_superuser==1 or j.id not in c:
			continue
		else: 
			d=RoleRqst.objects.get(uid_id=j.id)
			rr[j.id]=j.username,d.roletype,j.role,j.id
	e=rr.values()
	return render(request,'html/givepermissions.html',{'q':e})

@login_required
def giveper(request,k):
	r=User.objects.get(id=k)
	m=RoleRqst.objects.get(uid_id=k)
	if request.method == "POST":
		k=RoleUp(request.POST,instance=r)
		if k.is_valid():
			k.save()
			m.is_checked=1
			m.save()
			return redirect('/permission')
	k= RoleUp(instance=r)
	return render(request,'html/acceptpermissions.html',{'y':k})

@login_required
def addcase(request):
	if request.method=="POST":
		d=AddcaseForm(request.POST,request.FILES) 
		if d.is_valid():
			a=d.save(commit=False)
			a.c_id=request.user.id
			a.save()
			return redirect('/dash') 
	d=AddcaseForm()
	return render(request,'html/addcase.html',{'e':d})

@login_required
def mycase(request):
	s={}
	d=AddCase.objects.all()
	r=User.objects.all()
	for i in r:
		s[i.id]=i.id,i.username
	print(s)
	z=list(s.values())
	e,o={},{}
	for h in d:
		for w in z:
			if h.c_id == w[0]:
				o[h.id]=h.c_id,h.case_title,h.case_date,w[1],h.update_status,h.id
	k = AddCase.objects.filter(c_id=request.user.id)
	m=o.values()
	print(m)
	return render(request,'html/casedetails.html',{'y':m,'b':k})

@login_required
def updatecase(request,si):
	# t=AddCase.objects.get(c_id=si)
	t=AddCase.objects.get(id=si)
	if request.method == "POST":
		a=CaseupdateForm(request.POST,instance=t)
		if a.is_valid():
			a.save()
			return redirect('/mycase')
	a=CaseupdateForm(instance=t)
	return render(request,'html/updatecase.html',{'us':a})

@login_required
def deletecase(re,u):
	# data=AddCase.objects.get(c_id=u)
	data=AddCase.objects.filter(id=u)
	if re.method=="POST":
		data.delete()
		return redirect('/mycase')
	return render(re,'html/deletecase.html',{'sd':data})

@login_required
def addcriminal(request):
	if request.method=="POST":
		d=AddcriminalForm1(request.POST,request.FILES) 
		w=AddcriminalForm2(request.POST,request.FILES) 
		if d.is_valid() and w.is_valid():

			a=d.save(commit=False)
			a.c_id=request.user.id
			b=w.save(commit=False)
			a.save()
			b.save()
			return redirect('/dash') 
	d=AddcriminalForm1()
	w=AddcriminalForm2()
	return render(request,'html/addcriminal.html',{'e':d,'q':w})

@login_required
def criminalsreport(request):
	c=AddCriminal.objects.all()
	return render(request,'html/criminaldetails.html',{'s':c})

@login_required
def editcriminal(request,e):
	s=AddCriminal.objects.get(id=e)
	if request.method == "POST":
		a=AddcriminalForm1(request.POST,instance=s)
		b=AddcriminalForm2(request.POST,instance=s)
		if a.is_valid() and b.is_valid():
			a.save()
			b.save()
			return redirect('/criminalreport')
	a=AddcriminalForm1(instance=s)
	b=AddcriminalForm2(instance=s)
	return render(request,'html/editcriminal.html',{'u':a,'x':b})


@login_required
def delcriminal(request,d):
	data=AddCriminal.objects.get(id=d)
	if request.method=="POST":
		data.delete()
		return redirect('/criminalreport')
	return render(request,'html/delcriminal.html',{'sd':data})

@login_required
def addcrime(request):
	if request.method=="POST":
		d=AddcrimeForm(request.POST,request.FILES) 
		if d.is_valid():
			a=d.save(commit=False)
			a.c_id=request.user.id
			a.save()
			return redirect('/dash') 
	d=AddcrimeForm()
	return render(request,'html/addcrime.html',{'e':d})

def crimereport(request):
	c=AddCrime.objects.all()
	return render(request,'html/crimedetails.html',{'s':c})

def crimeref(request):
	return render(request,'html/crimereference.html')


@login_required
def emreport(request):
	s=User.objects.all()
	g = {}
	for x in s:
		if x.is_superuser or x.role == 1 or x.role == 0:
			continue
		else:
			g[x.id] = x.username,x.pid_no,x.mobile_no,x.email,x.id
	# s=User.objects.filter(id=request.user.role)
	# if s == 2:
	return render(request,'html/empdetails.html',{'d':s,'p':g.values()})

@login_required
def empview(request,w):
	t=User.objects.get(id=w)
	# t=User.objects.all()
	return render(request,'html/empview.html',{'s':t})


@login_required
def delemp(request,q):
	data=User.objects.get(id=q)
	if request.method=="POST":
		data.delete()
		return redirect('/empreport')
	return render(request,'html/delemp.html',{'sd':data})


@login_required
def usreport(request):
	d=User.objects.all()
	t = {}
	for z in d:
		if z.is_superuser or z.role == 2:
			continue
		else:
			t[z.id] = z.username,z.city,z.mobile_no,z.id,z.age
	# if user.role==1:
	# 	return render(request,'html/userrepdetails.html',{'s':d})
	return render(request,'html/userrepdetails.html',{'s':d,"p":t.values()})

@login_required
def userview(request,id):
	t=User.objects.get(id=id)
	# t=User.objects.all()
	return render(request,'html/userview.html',{'s':t})


@login_required
def deluser(request,p):
	data=User.objects.get(id=p)
	if request.method=="POST":
		data.delete()
		return redirect('/userreport')
	return render(request,'html/deluser.html',{'sd':data})




@login_required
def changepass(request):
 	if request.method=="POST":
 		c=ChangepassForm(user=request.user,data=request.POST)
 		if c.is_valid():
 			c.save()
 			return redirect('/login')

 	c=ChangepassForm(user=request)
 	return render(request,'html/changepassword.html',{'t':c})

@login_required
def updateprofile(request):
	if request.method == "POST":
		u=UserupdateForm1(request.POST,request.FILES,instance=request.user)
		n =UserupdateForm2(request.POST,request.FILES,instance=request.user)
		if u.is_valid() and n.is_valid():
			u.save()
			n.save()
			messages.success(request,"Profile photo updated Successfully")
			return redirect('/myprofile')
	u=UserupdateForm1(instance=request.user)
	n=UserupdateForm2(instance=request.user)
	return render(request,'html/updateprofile.html',{'us':u,'r':n})


def complaint(req):
	if req.method=="POST":
		data=ComplaintForm(req.POST)
		if data.is_valid():
			subject='Confirmation_Complaint'
			body="thank you for complaint"+req.POST['p_name']
			receiver=req.POST['p_email']
			sender=settings.EMAIL_HOST_USER
			send_mail(subject,body,sender,[receiver])
			data.save()
			messages.success(req,"Successfully sent to your mail "+receiver)
			return redirect('/')
	form=ComplaintForm()
	return render(req,'html/complaint.html',{'c':form})


	
# def crud(request):
# 	if request.method=="POST":
# 		c=UserRegistrationForm(request.POST)
# 		if c.is_valid():
# 			c.save()
# 			return render(request,'html/actions.html',{'o':c})
# 	c=UserRegistrationForm()
# 	return render(request,'html/actions.html',{'o':c})


# def deletedata(req,id):
#  	c=UserRegistration.objects.get(id=id)
#  	c.delete()
#  	return redirect('/crud')
