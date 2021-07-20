from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from CrimeReportingSystem.models import User,RoleRqst,AddCase,AddCriminal,ComplaintBox,AddCrime
# from django.forms.widgets import NumberInput
 


class UserRegistrationForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=['username','email']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"enter email",
			"required":True,
			}),

		}    
 
class RoleR(forms.ModelForm):
	class Meta:
		model = RoleRqst
		fields= ["uname","roletype","proof"]
		widgets={
		"uname":forms.TextInput(attrs={"class":"form-control my-2","readonly":True}),
		"roletype":forms.Select(attrs = {"class": "form-control my-2",}),
		"proof":forms.ClearableFileInput(attrs={"class":"form-control"}),

		}

class RoleUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","role"]
		widgets={
		"username": forms.TextInput(attrs={"class":"form-control","readonly":True,}),
		"role":forms.Select(attrs={"class":"form-control"}),
		}


class AddcaseForm(forms.ModelForm):
	class Meta:
		model=AddCase
		fields=["case_title","location","crime_proof","description"]
		widgets={
		"case_title":forms.TextInput(attrs={"class":"form-control","placeholder":"case title"}),
		"location":forms.TextInput(attrs={"class":"form-control","placeholder":"location of crime"}),
		"crime_proof":forms.ClearableFileInput(attrs={"class":"form-control",}),
		"description":forms.Textarea(attrs={'rows':4,"class":"form-control","placeholder":"describe the incident here"}),
		}
		

class CaseupdateForm(forms.ModelForm):
	class Meta:
		model=AddCase
		fields=["update_status","case_title","location","description"]
		widgets={
		"update_status":forms.Select(attrs={"class":"form-control"}),
		"case_title":forms.TextInput(attrs={"class":"form-control","readonly":True,}),
		"location":forms.TextInput(attrs={"class":"form-control","readonly":True,}),
		# "crime_proof":forms.ClearableFileInput(attrs={"class":"form-control","readonly":True,}),
		"description":forms.Textarea(attrs={'rows':4,"class":"form-control","readonly":True,}),
		}


class AddcriminalForm1(forms.ModelForm):
	class Meta:
		model=AddCriminal
		fields=["criminal_id","criminal_name","address_line1","address_line2","city","state","country","identification"]
		widgets={
		"criminal_id":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter criminal_id",
			}),
		"criminal_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter criminal_name",
			}),
		"address_line1":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Door Number",
			}),
		"address_line2":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter street name/flat name/village",
			}),
		"city":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter City",
			}),
		"state":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter State",
			}),
		"country":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Country",
			}),
		"identification":forms.Textarea(attrs={"rows":3,
			"class":"form-control",
			"placeholder":"Enter Features of criminal",
			}),
		}


class AddcriminalForm2(forms.ModelForm):
	class Meta:
		model=AddCriminal
		fields=["mobile_no","email","gender","dob","criminal_photo","height","weight","full_details"]
		widgets={
		"mobile_no":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter mobile number",
			}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter email Id",}),
		"gender":forms.Select(attrs={"class":"form-control","placeholder":"Select Gender"}),
		"dob":forms.NumberInput(attrs={'type':'date',
			"class":"form-control",
			"placeholder":"Enter dob of the criminal"}),
		
		"criminal_photo":forms.ClearableFileInput(attrs={
			"class":"form-control",
			}),
		"height":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Height of the criminal",
			}),
		"weight":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Weight of the criminal",
			}),
		"full_details":forms.Textarea(attrs={"rows":3,"class":"form-control",
			"placeholder":"Enter few more details about criminal",
			}),		
		}

class AddcrimeForm(forms.ModelForm):
	class Meta:
		model=AddCrime
		fields=["crime_type","crime_date","law","description"]
		widgets={
		"crime_type":forms.Select(attrs={
			"class":"form-control",
			}),
		"crime_date":forms.NumberInput(attrs={'type':'date',
			"class":"form-control",
			}),
		"law":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter law",
			}),
		"description":forms.Textarea(attrs={"rows":3,"class":"form-control",
			"placeholder":"describe.."}),
		}

class UserupdateForm1(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","email","age","gender","mobile_no","profile"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Emailid",
			}),
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Update Your Age",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Select Your Gender",
			}),
		"mobile_no":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"enter your mobile number"
			}),
		
		}

class UserupdateForm2(forms.ModelForm):
	class Meta:
		model = User
		fields = ["pid_no","dob","city","state","country"]
		widgets = {
		"pid_no":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"if you are police enter your id number"
			}),
		"city":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter city"
			}),
		"state":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter state",
			}),
		"country":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter country",
			}),
		"dob":forms.NumberInput(attrs={
			"type":"date",
			"class":"form-control",
			"placeholder":"enter dob"
			}),
		}
 
class ChangepassForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter old password"
		}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter new password"
		}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Confirm password"
		}))

	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']

class ComplaintForm(forms.ModelForm):
	class Meta:
		model=ComplaintBox
		fields="__all__"



