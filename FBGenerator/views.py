from django.http import HttpResponse
from django.shortcuts import render


def fibonacci(num):
    if num <= 0:
        return "Enter a valid Number"
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, num):
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series




def home(request):
    finalAns=0
    data={}
    try:
        if request.method=="POST":
            n1=int(request.POST['num1'])
           
            finalAns=fibonacci(n1)
            data={
              'n1':n1,
             
               'output':finalAns
          }
    except:
        pass    
    return render(request,"home.html",data)