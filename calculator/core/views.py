from django.shortcuts import render, redirect
from .models import History

# Create your views here.

def index(request):
    # return HttpResponse("Hello World")
    if (request.method=='POST'):
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if "add" in request.POST:  
            result = int(num1)+int(num2)
            operator="+"
        elif "sub" in request.POST:  
            result = int(num1)-int(num2)
            operator="-"
        elif "mul" in request.POST:  
            result = int(num1)*int(num2)
            operator="*"
        elif "div" in request.POST:  
            result = float(num1)/float(num2)
            operator="/"
        else:
            result = "Wrong inputs"
        op_dict = operator
        
        history = History.objects.create(num1 = num1, num2 = num2, op = op_dict, result = result)
        history.save()
        
        context = {"result": result}
        
        return render(request, 'index.html', context)
    
    else:
        data = History.objects.all()[::-1]
        data_dict = {
            "entry": data
        }
        return render(request, 'index.html', data_dict)