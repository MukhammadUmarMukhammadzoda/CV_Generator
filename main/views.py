from django.shortcuts import render,redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io



# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        previus_work = request.POST.get("previus_work", "")
        skills = request.POST.get("skills", "")

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school,
                          university=university, previus_work=previus_work, skills=skills)
        profile.save()
        userprofile = Profile.objects.all().last()

        template = loader.get_template('resume.html')
        html = template.render({'user_profile':userprofile})
        options ={'page-size':'Letter', 'encoding':"UTF-8"}
        pdf = pdfkit.from_string(html,False,options)
        response = HttpResponse(pdf,content_type='application/pdf')
        response['Content-Disposition'] ='attachment'
        filename = userprofile.name + "resume.pdf"
        return response

    return render(request, 'index.html',{})


