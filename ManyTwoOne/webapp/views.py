from django.shortcuts import render
from .models import Team
# Create your views here.
def teamslist(request):
	items = Team.objects.all()
	return render(request,'MyApp/Teamplayers.html',{'items':items})
