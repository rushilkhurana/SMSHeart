from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse

# Create your views here.
from .forms import GreenZone_Form, YellowZone_Form, RedZone_Form

def index(request):

 # This is uniform submission by using 'save' button on the top of page
  if request.method =='POST':

    if 'greenZone_form' in request.POST:
      greenZone_form = GreenZone_Form(request.POST, prefix='greenZone')

      if greenZone_form.is_valid():
        save_it = greenZone_form.save(commit=False)
        save_it.save()
      yellowZone_form = YellowZone_Form(prefix='yellowZone')
      redZone_form = RedZone_Form(prefix='redZone')

     # form submit successful and direct to another page
    elif 'yellowZone_form' in request.POST:
      yellowZone_form = YellowZone_Form(request.POST, prefix='yellowZone')

      if yellowZone_form.is_valid():
        save_it = yellowZone_form.save(commit=False)
        save_it.save()
      greenZone_form = GreenZone_Form(prefix='greenZone')
      redZone_form = RedZone_Form(prefix='redZone')
    elif 'redZone_form' in request.POST:
      redZone_form = RedZone_Form(request.POST, prefix='redZone')

      if redZone_form.is_valid():
        save_it = redZone_form.save(commit=False)
        save_it.save()
      greenZone_form = GreenZone_Form(prefix='greenZone')
      yellowZone_form = YellowZone_Form(prefix='yellowZone')
    return HttpResponse('/thanks/')

  else:
    greenZone_form = GreenZone_Form(prefix='greenZone')
    yellowZone_form = YellowZone_Form(prefix='yellowZone')
    redZone_form = RedZone_Form(prefix='redZone')

    return render_to_response("index.html",
                                  locals(),
                                  context_instance=RequestContext(request))

def login(request):
    return render_to_response("login.html", locals(), context_instance=RequestContext(request));

def addNewText(request):
    #get context from the request
    context = RequestContext(request)

    #Check if it's a HTTP POST
    if request.method =='POST':
        form =GreenZone_Form(request.POST or None)

    #Check the form is valid or not
    if form.is_valid():
        #save the greenzone form to the database
        form.save(commit=True)

        #now call the index() view, and user will be shown the homepage
        return index(request)
    else:
        #if the request was not a POST, display the form to enter details
        form = GreenZone_Form

    return render_to_response('/addNewText', {'form': form}, context)


def submit_yellowZoneForm(request):

    # 'yellowZone_form' is the name of the submit buttons in yellow_zone form section
    if 'yellowZone_form' in request.POST:
        yellowZone_form = YellowZone_Form(request.POST, prefix='yellowZone')

    if yellowZone_form.is_valid():
        yellowZone_form.save()

        # form submit successful and direct to another page
        return HttpResponse('/YellowZone/')

    else:
        form = YellowZone_Form()

    return render_to_response("index.html",
                                  locals(),
                                  context_instance=RequestContext(request))

def submit_greenZoneForm(request):

    # 'yellowZone_form' is the name of the submit buttons in yellow_zone form section
    if 'greenZone_form' in request.POST:
        greenZone_form = GreenZone_Form(request.POST, prefix='greenZone')

    if greenZone_form.is_valid():
        greenZone_form.save()

        # form submit successful and direct to another page
        return HttpResponse('/GreenZone/')

    else:
        form = GreenZone_Form()

    return render_to_response("index.html",
                                  locals(),
                                  context_instance=RequestContext(request))

def submit_redZoneForm(request):

    # 'yellowZone_form' is the name of the submit buttons in yellow_zone form section
    if 'redZone_form' in request.POST:
        redZone_form = RedZone_Form(request.POST, prefix='redZone')

    if redZone_form.is_valid():
        redZone_form.save()

        # form submit successful and direct to another page
        return HttpResponse('/RedZone/')

    else:
        form = RedZone_Form()

    return render_to_response("index.html",
                                  locals(),
                                  context_instance=RequestContext(request))