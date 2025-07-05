from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import logout



# Create your views here.
def index(request):
    return render(request, 'index.html')

def jobs(request):
    return render(request, 'pages/jobs.html')

def pricing(request):
    return render(request, 'pages/pricing.html')

def resume(request):
    return render(request, 'pages/resume.html')

def makeresume(request):
    if request.method == 'POST':
        # Personal Information
        personal_info = PersonalInformation(
            first_name=request.POST.get('firstname'),
            middle_name=request.POST.get('middlename'),
            last_name=request.POST.get('lastname'),
            image=request.FILES.get('image'),
            designation=request.POST.get('designation'),
            address=request.POST.get('address'),
            email=request.POST.get('email'),
            phone_no=request.POST.get('phoneno'),
            summary=request.POST.get('summary')
        )
        personal_info.save()

        achievement_titles = request.POST.getlist('achieve_title')
        achievement_descriptions = request.POST.getlist('achieve_description')
        for title, description in zip(achievement_titles, achievement_descriptions):
            if title and description:  # Ensure neither is empty
                Achievement.objects.create(
                    personal_info=personal_info,
                    title=title,
                    description=description
                )

        # Experience
        experiences = request.POST.getlist('exp_title')
        organizations = request.POST.getlist('exp_organization')
        locations = request.POST.getlist('exp_location')
        start_dates = request.POST.getlist('exp_start_date')
        end_dates = request.POST.getlist('exp_end_date')
        exp_descriptions = request.POST.getlist('exp_description')
        for title, organization, location, start_date, end_date, description in zip(
                experiences, organizations, locations, start_dates, end_dates, exp_descriptions):
            if title and organization:
                Experience.objects.create(
                    personal_info=personal_info,
                    title=title,
                    organization=organization,
                    location=location,
                    start_date=start_date,
                    end_date=end_date,
                    description=description
                )

        # Education
        educations = request.POST.getlist('edu_school')
        degrees = request.POST.getlist('edu_degree')
        cities = request.POST.getlist('edu_city')
        edu_start_dates = request.POST.getlist('edu_start_date')
        graduation_dates = request.POST.getlist('edu_graduation_date')
        edu_descriptions = request.POST.getlist('edu_description')
        for school, degree, city, start_date, graduation_date, description in zip(
                educations, degrees, cities, edu_start_dates, graduation_dates, edu_descriptions):
            if school and degree:
                Education.objects.create(
                    personal_info=personal_info,
                    school=school,
                    degree=degree,
                    city=city,
                    start_date=start_date,
                    graduation_date=graduation_date,
                    description=description
                )

        # Projects
        projects = request.POST.getlist('proj_title')
        project_links = request.POST.getlist('proj_link')
        project_descriptions = request.POST.getlist('proj_description')
        for title, link, description in zip(projects, project_links, project_descriptions):
            if title and link:
                Project.objects.create(
                    personal_info=personal_info,
                    title=title,
                    link=link,
                    description=description
                )

        # Skills
        skills = request.POST.getlist('skill')
        for skill in skills:
            if skill:
                Skill.objects.create(
                    personal_info=personal_info,
                    skill=skill
                )

        # Redirect to a success page or back to the form
        return HttpResponse('success')  # Update this with your actual success page

    return render(request, 'pages/makeresume.html')  # Update with your actual template

def signup_page(request):
    if request.method == "POST":
        role = request.POST.get('role')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        # Role must be selected
        if not role:
            message = "Please select your role!"
            return render(request, "loginsystem/signup.html", {'msg': message})

        # Check if passwords match
        if password != cpassword:
            message = "Passwords do not match!"
            return render(request, "loginsystem/signup.html", {'msg': message})

        # Check if user already exists
        if UserMaster.objects.filter(email=email).exists():
            message = "User already exists!"
            return render(request, "loginsystem/signup.html", {'msg': message})

        # Create user and role-specific profile
        new_user = UserMaster.objects.create(role=role, email=email, password=password)

        if role == "Candidate":
            Candidate.objects.create(user_id=new_user, name=name)
        elif role == "Company":
            Company.objects.create(user_id=new_user, name=name)

        return redirect('login')  # or show success message
    else:
        return render(request, "loginsystem/signup.html")

    
def LogInUser(request):
            if request.method == "POST":
                if request.POST['role']=="Candidate":
                    email = request.POST['email']
                    password = request.POST['password']    
                    user = UserMaster.objects.get(email=email) 
                    if user:
                        if user.password == password and user.role=="Candidate":
                            can = Candidate.objects.get(user_id=user) #can = candidate
                            request.session['id']=user.id
                            request.session['email']=user.email
                            request.session['role']=user.role
                            request.session['name']= can.name
                            return redirect('index')
                            #return render(request,"candidate/index.html",{'user':user,'can':can})
                        else:
                            message = "Password doesn't Match!!"
                            return render(request,"loginsystem/login.html",{'msg':message})
                    else:
                        message = "User doesn't Exist!!"
                        return render(request,"loginsystem/login.html",{'msg':message})
                
                elif request.POST['role']=="Company":
                    email = request.POST['email']
                    password = request.POST['password']
    
                    user = UserMaster.objects.get(email=email) #just check email same or not

                    if user:
                        if user.password == password and user.role=="Company":
                            comp = Company.objects.get(user_id=user)
                            request.session['id']=user.id #comp = company
                            request.session['email']=user.email
                            request.session['role']=user.role
                            request.session['name']= comp.name

                            return redirect('index')
                    
                        else:
                            message = "Password doesn't Match!!"
                            return render(request,"loginsystem/login.html",{'msg':message})
                    else:
                        message = "User doesn't Exist!!"
                        return render(request,"loginsystem/login.html",{'msg':message})
                else:
                    message = "Select Role!!"   
                    return render(request,"loginsystem/login.html",{'msg':message})
            else:
                return render(request,"loginsystem/login.html")
            
def user_logout(request,pk):
    user = UserMaster.objects.get(pk=pk)
    logout(request)
    return redirect('/')

def post_job(request):
    return render(request, 'pages/post_job.html')

def myprofile(request):
    return render(request, 'pages/myprofile.html')


# Profile

def profile_page(request):
    if 'id' in request.session:
        name = request.session.get('name')
        email = request.session.get('email')
        role = request.session.get('role')

        print("Fetched from session:", name, email, role)  # debugging

        return render(request, 'profile.html', {
            'name': name,
            'email': email,
            'role': role,
        })
     
    else:
        return redirect('login')