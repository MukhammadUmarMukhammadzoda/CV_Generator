from django.shortcuts import render
from .models import Profile
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previus_work= request.POST.get("previus_work","")
        skills = request.POST.get("skills","")

        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previus_work=previus_work,skills=skills)
        profile.save()
        
        
    
    return render(request,'index.html')



def resume(request,id):
    resume = Profile.objects.get(pk=id)
    print(resume.phone)
    
    return render(request,'resume.html',{'user_profile':resume})
    
    