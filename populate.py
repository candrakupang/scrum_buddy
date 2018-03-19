import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrum_buddy.settings')

import django

django.setup()

from scrum.models import Project, Story, Sprint


def populate():
	projects = [
		{"name": "n", "description":"d", "address":"a", "status":"s", "longitude":3, "latitude":3},
		{"name": "n2", "description":"d2", "address":"a2", "status":"s2", "longitude":4, "latitude":5} ]

	for project, p_data in projects.items():
		p = add_project(p_data["name"],p_data["description"],p_data["address"],p_data["status"],p_data["longitude"],p_data["latitude"])	
		
def add_project(name, description, address, status, longitude, latitude):
    p.name = name
    p.description = description
    p.address = address
    p.status = status
    p.longitude = longitude
    p.latitude = latitude
    p.save()
    return p


if __name__ == '__main__':
    print("Starting Scrum population script...")
    populate()