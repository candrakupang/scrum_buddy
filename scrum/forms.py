from django import forms
from django.contrib.auth.models import User
from scrum.models import UserProfile,Project,Story,Sprint

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')
		
class StoryForm(forms.ModelForm):
	text = forms.CharField(max_length=128)
	header = forms.CharField(max_length=20)
	top = forms.CharField(max_length=6)
	left = forms.CharField(max_length=6)
	width = forms.CharField(max_length=6)
	heigth = forms.CharField(max_length=6)
	theme = forms.CharField(max_length=30)
	id = forms.IntegerField()

	class Meta:
 # Provide an association between the ModelForm and a model
		model = Story
		exclude = ('project',)	

class ProjectForm(forms.ModelForm):	
	id = forms.IntegerField()
	name = forms.CharField(max_length=30)
	description = forms.CharField(max_length=200)
	address = forms.CharField(max_length=30)
	longitude = forms.FloatField()
	latitude = forms.FloatField()
	STATUS_1 = 'New'
	STATUS_2 = 'On Progress'
	STATUS_3 = 'Finish'
	STATUS_CHOICES = (
		(STATUS_1, u"New"),
		(STATUS_2, u"On Progress"),
		(STATUS_3, u"Finish")
	)
	status = forms.ChoiceField(choices=STATUS_CHOICES)

	class Meta:
 # Provide an association between the ModelForm and a model
		model = Project
		fields = ('id','name','description','address','status','longitude','latitude',)	
		
class SprintForm(forms.ModelForm):
	id = forms.IntegerField()
	iteration = forms.CharField(max_length=30)
	startDate = forms.CharField(widget=forms.TextInput(attrs={'class':'startDate'}))
	endDate = forms.CharField(widget=forms.TextInput(attrs={'class':'endDate'}))
	releaseDate = forms.DateField(widget=forms.TextInput(attrs={'class':'releaseDate'}))
	def __init__(self, *args, **kwargs):
		myproject = kwargs.pop("prj")
		super(SprintForm, self).__init__(*args, **kwargs)
		self.fields['story'] = forms.ModelChoiceField(Story.objects.filter(project = myproject))

	class Meta:
 # Provide an association between the ModelForm and a model
		model = Sprint
		exclude = ('project',)