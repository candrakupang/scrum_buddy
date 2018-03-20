from django.test import TestCase
from django.core.urlresolvers import reverse
from scrum.models import Project, Story, Sprint


"""		Helper Method for add project		"""
def add_project(id, name, description, address, status, longitude, latitude):
	p, created = Project.objects.get_or_create(id=id, name=name, description=description, address=address, status=status, longitude=longitude, latitude=latitude)
	return p

	
class ScrumMethodTests(TestCase):
	
	def test_project_creation(self):
		"""		ensure project creation run perfectly		"""
		print(" ======  test create project  ======  ")
		project = Project(name='test project', description='desc', address='address', status='status', longitude=4, latitude=5)
		project.save()
		self.assertEqual((project.name == 'test project'), True)
		self.assertEqual((project.description == 'desc'), True)
		self.assertEqual((project.address == 'address'), True)
		self.assertEqual((project.status == 'status'), True)
		self.assertEqual((project.longitude == 4), True)
		self.assertEqual((project.latitude == 5), True)		
	
		"""		ensure story creation run perfectly		"""
		print(" ======  test create story  ======  ")
		story = Story(project=project, text='text', header='header', top='top', left='left', width='width', heigth='heigth', theme='theme', point='point', priority='priority')
		story.save()
		self.assertEqual((story.project == project), True)
		self.assertEqual((story.text == 'text'), True)
		self.assertEqual((story.header == 'header'), True)
		self.assertEqual((story.top == 'top'), True)
		self.assertEqual((story.left == 'left'), True)
		self.assertEqual((story.width == 'width'), True)
		self.assertEqual((story.heigth == 'heigth'), True)
		self.assertEqual((story.theme == 'theme'), True)
		self.assertEqual((story.point == 'point'), True)
		self.assertEqual((story.priority == 'priority'), True)
		
		"""		ensure sprint creation run perfectly		"""
		print(" ======  test create sprint  ======  ")
		sprint = Sprint(project=project,story=story,iteration='iteration', startDate='startDate', endDate='endDate', releaseDate='releaseDate')
		sprint.save()
		self.assertEqual((sprint.iteration == 'iteration'), True)
		self.assertEqual((sprint.startDate == 'startDate'), True)
		self.assertEqual((sprint.endDate == 'endDate'), True)
		self.assertEqual((sprint.releaseDate == 'releaseDate'), True)

	def test_load_index_page(self):
		"""		ensure index page can be loaded successfully		"""
		print(" ======  test load index page  ======  ")
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
	
	def test_load_user_story_page(self):
		"""		ensure user story page can be loaded successfully		"""
		print(" ======  test load user story page  ======  ")
		add_project(1,'test project', 'desc', 'address', 'status', 4, 5)
		response = self.client.get(reverse('userstory', args=[1]))
		num_projects =len(response.context['projects'])
		self.assertEqual(num_projects , 1)		
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['stories'], [])
		
	def test_load_project_page(self):
		"""		ensure project page can be loaded successfully		"""
		print(" ======  test load project page  ======  ")
		response = self.client.get(reverse('project'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['projects'], [])
		
	def test_load_sprint_page(self):
		"""		ensure sprint page can be loaded successfully		"""
		print(" ======  test load sprint page  ======  ")
		add_project(1,'test project', 'desc', 'address', 'status', 4, 5)
		response = self.client.get(reverse('sprint', args=[1]))
		num_projects =len(response.context['projects'])
		self.assertEqual(num_projects , 1)
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['sprints'], [])
		
	def test_load_backlog_page(self):
		"""		ensure back log page can be loaded successfully		"""
		print(" ======  test load back log page  ======  ")
		add_project(1,'test project', 'desc', 'address', 'status', 4, 5)
		response = self.client.get(reverse('backlog', args=[1]))
		num_projects =len(response.context['projects'])
		self.assertEqual(num_projects , 1)
		self.assertEqual(response.status_code, 200)	
		
	def test_load_geospatial_page(self):
		"""		ensure geospatial page can be loaded successfully		"""
		print(" ======  test load geospatial page  ======  ")
		response = self.client.get(reverse('geospatial'))
		self.assertEqual(response.status_code, 200)	