from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'Hello World','number':7}
    return render(request,'app03/index.html',context_dict)

def other(request):
    return render(request,'app03/other.html')

def relative(request):
    return render(request,'app03/rel_url_temp.html')
