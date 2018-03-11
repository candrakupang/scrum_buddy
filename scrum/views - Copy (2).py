from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from scrum.forms import UserForm, UserProfileForm,StoryForm
from scrum.models import Project,Story



def addstory(request,projectID):
	try:
		p = Project.objects.get(id=projectID)
	except Project.DoesNotExist:
		p = None
	
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
	return render(request, 'scrum/board.html', context_dict)			
			
def index(request):
	context_dict = {}
	form = StoryForm()
	context_dict['form'] = form
	return render(request, 'scrum/index.html', context_dict)
	
def qwerty(request):
	print("---------------------")
	return HttpResponse("test ajax")
	
def board(request,projectID):
	context_dict = {}
	if projectID == "0":
		p = Project.objects.all()[:1].get()
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
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request,'scrum/register.html',{'user_form': user_form,'profile_form': profile_form,'registered': registered})
	
	
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return render(request, 'scrum/index.html')
			else:
				return HttpResponse("Your scrum account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'scrum/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return render(request, 'scrum/index.html')