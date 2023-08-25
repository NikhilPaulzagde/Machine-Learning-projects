from django.shortcuts import render,HttpResponse
import joblib
# Create your views here.

model=joblib.load('static/rf_model')


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


def login(request):
    return render(request,"login.html")

def registration(request):
    return render(request,"registration.html")

def prediction(request):
    if request.method=="POST":
        age=int(request.POST.get('age'))
        sex=int(request.POST.get('sex'))
        bmi=int(request.POST.get('bmi'))
        children=int(request.POST.get('children'))
        smoker=int(request.POST.get('smoker'))
        region=int(request.POST.get('region'))

        print(age,sex,bmi,children,smoker,region)

        pred=model.predict([[age,sex,bmi,children,smoker,region]])[0]
        print(pred)

        output={
            "output":round(pred)
        }
        return render(request,"prediction.html",output)


    else:
        return render(request,"prediction.html")

