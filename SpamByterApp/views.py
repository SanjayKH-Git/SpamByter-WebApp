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
        print(sp_phno,type(sp_phno[0]))
        print(phno,type(phno))
        #check if  exist in SpamUser Model
        if phno in sp_phno:
            #Punish
            print("Bomb to this Spam User ")
            os.system("printf '"+phno+"\n10\n' | ./static/Bomber/Tsunami.sh")
            return HttpResponse("<script>alert('Bombing to this Spam User... ');</script>")
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