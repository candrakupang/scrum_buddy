from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render,redirect
from scrum.forms import UserForm, UserProfileForm,StoryForm,ProjectForm,SprintForm
from scrum.models import Project,Story,Sprint
from django.http import JsonResponse
from django.core import serializers

def getstory(request):
	projectID = request.GET.get("id", "")
	try:
		p = Project.objects.get(id=projectID)
	except Project.DoesNotExist:
		p = None
	s = Story.objects.filter(project = p)
	data = serializers.serialize("json", s)
	return HttpResponse(data, content_type='application/json')

def getsprint(request):
	sprintID = request.GET.get("id", "")
	try:
		s = Sprint.objects.get(id=sprintID)
	except Sprint.DoesNotExist:
		s = None
	data = serializers.serialize('json', [s,])
	return HttpResponse(data, content_type='application/json')

def getproject(request):
	projectID = request.GET.get("id", "")
	if projectID == "0":
		p = Project.objects.all()
		data = serializers.serialize("json", p)
	else:
		p = Project.objects.get(id=projectID)
		data = serializers.serialize('json', [ p, ])
	return HttpResponse(data, content_type='application/json')	
	
def xstory(request):
	storyID = request.POST.get("id", "")
	try:
		s = Story.objects.get(id=storyID)
	except Story.DoesNotExist:
		s = None
	
	if s:	
		Story.objects.filter(id=storyID).delete()
	return HttpResponse("Ok")

def xproject(request):
	projectID = request.POST.get("id", "")
	try:
		p = Project.objects.get(id=projectID)
	except Project.DoesNotExist:
		p = None
	if p:	
		Project.objects.filter(id=projectID).delete()
	return HttpResponse("Ok")
	
def geospatial(request):
	return render(request, 'scrum/geospatial.html')

def xsprint(request):
	sprintID = request.POST.get("id", "")
	try:
		s = Sprint.objects.get(id=sprintID)
	except Sprint.DoesNotExist:
		s = None
	if s:	
		Sprint.objects.filter(id=sprintID).delete()
	return HttpResponse("Ok")
	
def index(request):
	context_dict = {}
	form = ProjectForm()
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			p = form.save(commit=False)
			if request.POST.get("id", "") != "0":
				p.id = request.POST.get("id", "")
			p.save();
			return HttpResponseRedirect(reverse('index'))
	form = ProjectForm()
	context_dict['projects'] = Project.objects.all()
	context_dict['form'] = form
	return render(request, 'scrum/index.html', context_dict)

def project(request):
	context_dict = {}
	form = ProjectForm()
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			p = form.save(commit=False)
			if request.POST.get("id", "") != "0":
				p.id = request.POST.get("id", "")
			p.save();
			return HttpResponseRedirect(reverse('project'))
	form = ProjectForm()
	context_dict['projects'] = Project.objects.all()
	context_dict['form'] = form
	return render(request, 'scrum/project.html', context_dict)
	
def sprint(request,projectID):
	context_dict = {}
	if projectID == "0":
		p = None
	else:
		p = Project.objects.get(id=projectID)
	form = SprintForm(prj=p)
	if request.method == 'POST':
		form = SprintForm(request.POST,prj=p)
		if form.is_valid():
			if p:
				s = form.save(commit=False)
				s.project = p
				if request.POST.get("id", "") != "0":
					s.id = request.POST.get("id", "")
				s.save();
				return HttpResponseRedirect(reverse('sprint', args=[projectID]))
	form = SprintForm(prj=p)
	context_dict['projects'] = Project.objects.all()
	context_dict['stories'] = Story.objects.filter(project = p)
	context_dict['sprints'] = Sprint.objects.filter(project = p)
	context_dict['prj'] = p
	context_dict['form'] = form
	return render(request, 'scrum/sprint.html', context_dict)

def backlog(request,projectID):
	context_dict = {}
	if projectID == "0":
		p = None
	else:
		p = Project.objects.get(id=projectID)
	context_dict['projects'] = Project.objects.all()
	context_dict['stories'] = Story.objects.filter(project = p)
	context_dict['prj'] = p
	return render(request, 'scrum/backlog.html', context_dict)
	
def board(request,projectID):
	context_dict = {}
	if projectID == "0":
		p = None
	else:
		p = Project.objects.get(id=projectID)
	form = StoryForm()	
	if request.method == 'POST':
		form = StoryForm(request.POST)
		if form.is_valid():
			if p:
				story = form.save(commit=False)				
				story.project = p
				if request.POST.get("id", "") != "0":
					story.id = request.POST.get("id", "")
				story.save()
	context_dict['form'] = form
	context_dict['projects'] = Project.objects.all()
	context_dict['stories'] = Story.objects.filter(project = p)
	context_dict['prj'] = p
	return render(request, 'scrum/board.html', context_dict)	
	
def register(request):
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			return render(request,'scrum/login.html',{'user_form': user_form})	
		else:
			return render(request,'scrum/register.html',{'user_form': user_form,'error':'Username is already exists'})	
	else:
		user_form = UserForm()
		return render(request,'scrum/register.html',{'user_form': user_form})
	
	
def user_login(request):
	context_dict = {}
	user_form = UserForm()
	context_dict['user_form'] = user_form
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your scrum account is disabled.")
		else:						
			context_dict['error'] = "Incorrect Username or Password"			
			return render(request, 'scrum/login.html', context_dict)
	else:
		return render(request, 'scrum/login.html', context_dict)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))