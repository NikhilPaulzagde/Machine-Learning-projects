from django.shortcuts import render
from .utils import predict_diabetes



def home(request):
    return render(request,"home.html")


def predict(request):
    return render(request,"predict.html")


def result(request):
    if request.method == 'GET':
        Pregnancies = float(request.GET['n1'])
        Glucose = float(request.GET['n2'])
        BloodPressure = float(request.GET['n3'])
        SkinThickness = float(request.GET['n4'])
        Insulin = float(request.GET['n5'])
        BMI = float(request.GET['n6'])
        DiabetesPedigreeFunction = float(request.GET['n7'])
        Age = float(request.GET['n8'])

        result1 = predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

        return render(request, "predict.html", {"result2": result1})