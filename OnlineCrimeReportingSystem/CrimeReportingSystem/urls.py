from django.urls import path
from CrimeReportingSystem import views
from django.contrib.auth import views as ad

urlpatterns=[
    path('',views.home,name="hm"),
    path('aboutus/',views.aboutus,name="au"),
    path('contactus/',views.contactus,name="cu"),
    
    path('login/',views.login_page,name="lg"),
    path('register/',views.register,name="rg"),

    path('myprofile/',views.profile,name="profile"),
    path('changepassword/',views.changepass,name="chp"),
    path('logout/',ad.LogoutView.as_view(template_name='html/logout.html'),name="lgo"),
    path('dash/',views.dashboard,name="dsh"),

    path('rolerq/',views.rolereq,name='rr'),
    path('permission/',views.permissions,name='per'),
    path('gvp/<int:k>/',views.giveper,name='gvpr'),

    path('updatepro/',views.updateprofile,name="uppro"),
    path('filecase/',views.addcase,name="ac"),
    path('mycase/',views.mycase,name="mc"),
    path('updatecase/<int:si>/',views.updatecase,name="ucs"),
    path('deletecase/<int:u>/',views.deletecase,name="dc"),

    path('addcriminal/',views.addcriminal,name="cri"),
    path('criminalreport/',views.criminalsreport,name="crep"),
    path('edit/<int:e>/',views.editcriminal,name="ecri"),
    path('delcriminal/<int:d>/',views.delcriminal,name='dcri'),

    path('addcrime/',views.addcrime,name="adcr"),
    path('crimereport/',views.crimereport,name='crirep'),
    path('crimereference/',views.crimeref,name="crref"),

    path('empreport/',views.emreport,name="er"),
    path('delemp/<int:q>/',views.delemp,name="delemp"),
    path('viewemp/<int:w>/',views.empview,name="viewe"),
    path('userreport/',views.usreport,name="ur"),
    path('deluser/<int:p>/',views.deluser,name="delu"),
    path('viewuser/<int:id>/',views.userview,name="viewu"),

    path('reset/',ad.PasswordResetView.as_view(template_name="html/reset_password.html"),name="rst"),
    path('reset_done/',ad.PasswordResetDoneView.as_view(template_name="html/reset_password_done.html"),name="password_reset_done"),
    path('reset_cf/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name="html/reset_password_confirm.html"),name="password_reset_confirm"),
    path('reset_cmplt/',ad.PasswordResetCompleteView.as_view(template_name="html/reset_password_complete.html"),name="password_reset_complete"),
]