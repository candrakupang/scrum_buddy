import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrum_buddy.settings')

import django

django.setup()

from scrum.models import Project, Story, Sprint

def populate():
    print('Populating Database...')
    print('----------------------\n')

    add_project('1', 'WarZone', 'Android Game', 'Glasgow', 'On Progress', '-4.251806', '55.864237')
    add_story('1','1', 'As player I want to drive tanks\nPoint : 3\nPriority : High', 'Tanks', '200px','50px', '200px', '100px', 'sticky-note-green-theme', '3', 'high')
    add_story('1', '2', 'As player I want to fly planes\nPoint : 3\nPriority : High', 'Planes', '60px', '50px', '200px',
              '100px', 'sticky-note-pink-theme', '3', 'high')
    add_story('1', '3', 'As player I want to ride motorcycles\nPoint : 2\nPriority : Medium', 'Motorcycles', '200px', '320px', '200px',
              '100px', 'sticky-note-blue-theme', '2', 'high')
    add_story('1', '4', 'As player I want to defend a base\nPoint : 4\nPriority : Low', 'Defend Base', '60px',
              '320px', '200px', '100px', 'sticky-note-pink-theme', '4', 'high')

    add_sprint('1','1','1','1st','01/04/2018','07/04/2018','15/04/2018')
    add_sprint('1','2','2','2nd','08/04/2018','14/04/2018','15/04/2018')
    add_sprint('1','3','3','3rd','15/04/2018','21/04/2018','30/04/2018')
    add_sprint('1','4','4','4th','21/04/2018','28/04/2018','30/04/2018')	
def add_project(id, name, description, address, status, longitude, latitude):
    p, created = Project.objects.get_or_create(id=id, name=name, description=description, address=address, status=status, longitude=longitude, latitude=latitude)
    return p

def add_story(project_id, id, text, header, top, left, width, height, theme, point, priority):
    s, created = Story.objects.get_or_create(project_id=project_id,id=id, text=text, header=header, top=top, left=left, width=width, heigth=height, theme=theme, point=point, priority=priority)
    return s

def add_sprint(project_id, story_id, id, iteration, startDate, endDate, releaseDate):
    sp, created = Sprint.objects.get_or_create(project_id=project_id, story_id=story_id, id=id,
                                               iteration=iteration, startDate=startDate, endDate=endDate, releaseDate=releaseDate)
    return sp


populate()
print('... database complete.')
print('----------------------\n')