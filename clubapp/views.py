from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getresources(request):
    resource_list = Resource.objects.all()
    return render( request, 'clubapp/resources.html', {'resource_list' : resource_list})

def getmeetings(request):
    meeting_list = Meeting.objects.all()
    return render( request, 'clubapp/meetings.html', {'meeting_list' : meeting_list})

def getminutes(request):
    minute_list = MeetingMinutes.objects.all()
    return render( request, 'clubapp/minutes.html', {'minute_list' : minute_list})

def getevents(request):
    event_list = Event.objects.all()
    return render( request, 'clubapp/events.html', {'event_list' : event_list})

def meetingdetails(request, id):
    meet = get_object_or_404( Meeting, pk = id )
    
    try:
        minutes = get_object_or_404( MeetingMinutes, meeting = id )
    except:
        minutes = None
        
    context = {
        'meet' : meet,
        'minutes' : minutes
    }
    return render( request, 'clubapp/meetdetails.html', context = context )

def loginmessage(request):
    return render(request, 'clubapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'clubapp/logoutmessage.html')

@login_required
def newMeeting(request):
    form = MeetingForm
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'clubapp/newmeeting.html', {'form': form})