from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def paypal_return(request):
    args = {'post': request.post, 'get': request.GET}
    return render(request, 'paypal/paypal_return.html', args)

def paypal_cancel(request):
    args = {'post': request.Post, 'get': request.GET}
    return render(request, 'paypal/paypal_cancel.html', args)
