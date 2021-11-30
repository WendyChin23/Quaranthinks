from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import(get_object_or_404,render,HttpResponseRedirect)
from .forms import AccountUserForm, GradeForm
from django.core.mail import send_mail, BadHeaderError
from tech import settings  
from django.urls import reverse_lazy
from django.contrib import messages


from appdev.models import *
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request,'index.html')

class About(View):
    def get(self, request):
        return render(request,'about.html')

class Blogsingle(View):
    def get(self, request):
        return render(request,'blog-single.html')

class Blog(View):
    def get(self, request):
        return render(request,'blog.html')

class Team(View):
    def get(self, request):
        return render(request,'team.html')

class Contact(View):
    def get(self, request):
        return render(request,'contact.html',{})

    def post(self, request):
        conform = ContactForm(request.POST)
        if request.method == "POST": 
            if conform.is_valid():
                name = request.POST.get("name")
                subject = request.POST.get("subject")
                email = request.POST.get("email")
                message = request.POST.get("message")

                conform = ContactMessage(name = name, subject = subject, email = email, message = message) 
                conform.save()
                send_mail(name,message,email,[settings.EMAIL_HOST_USER], fail_silently = False,)
                return render(request, 'contact.html', {'name': name})
            else:
                print(form.errors)
                pok = "Not send message"
                return HttpResponse(pok)          

class Members(View):
    def get(self, request):
        return render(request,'members.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            check_user = AccountUser.objects.filter(username=username, password=password)
            check_admin = Admin.objects.filter(username='admin', password='admin')

            if check_user:
                request.session['usern'] = username
                if AccountUser.objects.filter(username=username).count()>0: 
                    return redirect('appdev:clientdashboard_view')

            if check_admin:
                request.session['admin'] = 'admin'
                if Admin.objects.filter(username='admin').count()>0:    
                    return redirect('appdev:accountdashboard_view')

            else:
                return HttpResponse('not valid')
        else:   
            return render(request,"signup.html")

class Portfolio(View):
    def get(self, request):
        return render(request,'portfolio-details.html')

class Rewards(View):
    def get(self, request):
        return render(request,'rewards.html')

class Services(View):
    def get(self, request):
        return render(request,'services.html')

class Signup(View):
    def get(self, request):
        return render(request,'signup.html')

        
class AdminDashboard(View):
    def get(self, request):
        return render(request,'admindashboard.html')

class ClientDashboard(View):
    def get(self, request):
        if 'usern' in request.session:
            current_user = request.session['usern']
            userdetails = AccountUser.objects.filter(username=current_user)
            

            context = {'userdetails':userdetails,
                       }
        return render(request,'client.html', context)

class ClientHome(View):
    def get(self, request):
        return render(request,'clienthome.html')    

class Donation(View):
    def get(self, request):
        return render(request,'donationpage.html')          
        
class ClientGrades(View):
    def get(self, request):
        if 'usern' in request.session:
            current_user = request.session['usern']
            userdetails = AccountUser.objects.filter(username=current_user)
            usergrades = Grade.objects.filter(username=current_user)

            context = {'usergrades':usergrades,
                        'userdetails':userdetails,
                        }
        return render(request,'clientgrades.html', context)

class ClientVouchers(View):
    def get(self, request):
        if 'usern' in request.session:
            current_user = request.session['usern']
            userdetails = AccountUser.objects.filter(username=current_user)
            check_gvoucher = Grade.objects.filter(username=current_user, midterm__range=(4.0,4.5))
            check_evoucher = Grade.objects.filter(username=current_user, midterm__range =(4.6, 5.0))
            
            if check_gvoucher:
                check_vouchers = GeneralVoucher.objects.filter(gv_code=12345)       
            else:                   
                check_vouchers = None

            if check_evoucher:
                check_evouchers = ExclusiveVoucher.objects.filter(ev_code=14554)
            else:
                check_evouchers = None  
                

        
                
            context = {'check_vouchers':check_vouchers,
                        'userdetails':userdetails,
                        'check_evouchers':check_evouchers}      
        return render(request,'clientvouchers.html', context)           

class AdminPage(View):
    def get(self, request):
        return render(request,'adminpage.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            check_admin = Admin.objects.filter(username=username, password=password)

            if check_admin:
                request.session['admin'] = username
                if Admin.objects.filter(username=username).count()>0:   
                        return redirect('appdev:accountdashboard_view')
            else:   
                return HttpResponse('not valid')
        else:   
            return render(request,"signup.html", context)

class Testimonial(View):
    def get(self, request):
        return render(request,'testimonials.html')

        

class GradesView(View):
    def get(self, request):
        if  request.session.get('usert'):
            current_user = request.session['admin']
            usert = request.session.get('usert')
            graded = Grade.objects.filter(username=usert)

        #   #kani nalang kuwang para mu connect
        #    usert = request.session.get('usert')
        #    grades = Grade.objects.filter(username=usert)
        #    graded = Grade.objects.all()
        
        # # if 'admin' in request.session:
        # #   #current_admin = request.session['admin']
        # #   grades = Grade.objects.all()
            # context = {
            #   'grades' : grades,
            #    #name that we want to use        
            #   }  
        else:
            return HttpResponse('not valid')     
            return render(request,'grades.html', {'graded':graded})


class AccountDashboardView(View):
    def get(self, request):
        
        if 'admin' in request.session:
            current_admin = request.session['admin']
            accountadmin = Admin.objects.filter(username=current_admin)
            accountuser = AccountUser.objects.all()
            
        # kani nalang kuwang para mu connect
        
        
                # form = AccountUserForm(request.POST or None)
                # if form.is_valid(): # di sha mu pass
                #   project_id = form.cleaned_data['username'].id
                #   request.session['usert'] = project_id
                    
                #   return redirect('appdev:grades_view')
                # else:
                #   return HttpResponse('NOT VALID')    
            # accountgrade = Grade.objects.all()
            # accountevoucher = ExclusiveVoucher.objects.all()
            # accountgvoucher = GeneralVoucher.object.all()
            #accountuser = AccountUser.objects.all()
                # else:
                #   return HttpResponse('NOT VALID')
        context = {
                'accountadmin' : accountadmin, #name that we want to use
                'accountuser' : accountuser,
        }
        return render(request,'Accountuser.html', context)

    def post(self, request):
        if request.method == 'POST':
            # if request.method == 'POST':
            if 'BtnGrades' in request.POST:
                student = request.POST.get("username")
                check_grade = AccountUser.objects.get(username=student)

                if check_student:
                    request.session['usert'] = student
                    request.session.modified = True
                    if AccountUser.objects.filter(username=student).count()>0:
                        return redirect('appdev:grades_view')

            if 'BtnUpdate' in request.POST:
                print('update button clicked')
                Uid = request.POST.get("Uid-Uid")                                                                                                                                                                                                                                                                                                                                            
                fname = request.POST.get("first-name")
                lname = request.POST.get("last-name")
                Email = request.POST.get("email-email")             
                Address = request.POST.get("address-address")
                Age = request.POST.get("age-age")
                Birthdate = request.POST.get("birth-date")
                Username = request.POST.get("user-name")
                Password = request.POST.get("pass-word")
                
                update_user = AccountUser.objects.filter(uid = Uid).update(first_name = fname, last_name = lname, address = Address,
                email = Email, age = Age, birthdate = Birthdate, username = Username, password = Password )
                print(update_user)
                print('user updated')
            
            elif 'BtnDelete' in request.POST:
                print('delete button clicked')
                Uid = request.POST.get("Uuid-Uid")
                user = AccountUser.objects.filter(uid=Uid).delete()

        return redirect('appdev:accountdashboard_view')


class Signup(View):
    # def get(self, request):
    #     return render(request, 'student.html')

    # def post(self, request):
    #     form = StudentForm(request.POST)
    #     if form.is_valid():
    #         studentid = request.POST.get("course_id")
    #         coursesname = request.POST.get("course_name")

    #         form = Course(course_id = courseid, course_name = coursesname)
    #         form.save()

    #         return redirect('myapp1:dashboard_view')

    #     else:
    #         print(form.errors)
    #         return HttpResponse('not valid')

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):        
        form = AccountUserForm(request.POST)        
        # fname = request.POST.get("firstname")
        # print(fname)
        # lname = request.POST.get("lastname")
        # print(lname)
        if form.is_valid():
            # try:
            fname = request.POST.get("first_name")
            Uid = request.POST.get("uid")            
            lname = request.POST.get("last_name")
            Email = request.POST.get("email")
            Address = request.POST.get("address")
            Age = request.POST.get("age")
            Birthdate = request.POST.get("birthdate")
            Username = request.POST.get("username")
            Password = request.POST.get("password")
            form = AccountUser(uid = Uid, first_name = fname, last_name = lname, email = Email, address = Address, age = Age,
             birthdate = Birthdate, username = Username, password=Password)
            print('clicked')
            form.save() 

            #return HttpResponse('Student record saved!')           
            return redirect('appdev:members_view')
            # except:
            #   raise Http404
        else:
            print(form.errors)
            return HttpResponse('not valid')    
    #def post(self, request):

        # if request.method == "POST":  
        #   if 'btnRegister' in request.POST:
        #       Uform = AccountUserForm(request.POST)           
        #       if Uform.is_valid():
        #           print('clicked')
        #           user = Uform.save()

        #           user.refresh_from_db()
        #           # print('clicked')
        #           # fname = user.profile.first_name = request.POST.get("first_name")
        #           # lname = user.profile.last_name = request.POST.get("last_name")
        #           # email = user.profile.email = request.POST.get("email")
        #           # address = user.profile.address = request.POST.get("address")
        #           # age = user.profile.age = request.POST.get("age")
        #           # bdate = user.profile.birthdate = request.POST.get("birthdate")
        #           # user.save()           
        #           # username = request.POST.get("username")
        #           # password = request.POST.get("password1")

        #           # form = AccountUser(first_name = fname, last_name = lname, email = email, address = address, age = age,
        #           # birthdate = bdate)
        #           # form.save()

        #           return HttpResponse('Student record saved!')
        #           return redirect('appdev:members_view')
        #       else:   
        #           return HttpResponse('not valid')
        # #             form = AccountUserForm()
        # # context = {'form':form} 

        # # return render(request,"signup.html", context)
                
    

        