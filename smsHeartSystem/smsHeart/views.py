from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse

# Create your views here.
from .forms import PatientForm

def home(request):

    form = PatientForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save();


    return render_to_response("index.html",
                              locals(),
                              context_instance=RequestContext(request))


def about(request):
    return HttpResponse("About page is ready");