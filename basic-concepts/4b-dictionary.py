#!/usr/bin/python3

# Examples for dictionary
# Empty Dictionary
emp_dict = {}

# dictionary with integer keys
emp_dict = {100: 'Sanjeev', 101: 'Jassi'}
print(emp_dict)

# dictionary with mixed keys
emp_dict = {100: 'Sanjeev', 'skills': ['Python', 'AWS']}
print(emp_dict)

# using dict() function
emp_dict = dict({100: 'Sanjeev', 101: 'Jassi'})
print(emp_dict)

# Let's create emp_dict of this format
'''
{	
	'Employee ID':
	{	Name: 'string'
		Joined: 'yyyy-mm-dd'
		Title: 'string'
		Skills: [‘list’, ‘of’, ‘skills’]
		Project: {‘project_name’: ‘project description’}
	}
}
'''

# Initializing Employee
emp_dict = {
    100:
        {
            'name': "Sanjeev",
            'joined': "2017-08-14",
            'title': "Cloud Security Engineer",
            'skills': ['Python', 'AWS', 'AppSec'],
            'projects': {
                'CSPM implementation': 'Implement Cloud Security Posture for AWS'
            }
        },
    101:
        {
            'name': "Jassi",
            'joined': "2017-10-27",
            'title': "Cloud Security Manager",
            'skills': ['Python', 'AWS', 'AWS Security'],
            'projects': {
                'CSPM implementation': 'Implement Cloud Security Posture for AWS and Azure'
            }
        }
}

print(emp_dict)

# Get the type of emp_dict
print(type(emp_dict))

# get keys of a dictionary using keys()
emp_ids = emp_dict.keys()
print(emp_ids)

# Get values of a dictionary using values()
emp_details = emp_dict.values()
print(emp_details)

# get key and value both using items()
emps = emp_dict.items()
print(emps)

# Length of a dictionary (number of items) using len()
print(len(emp_dict))

# Iterate through a dictionary
for id in emp_dict.keys():
    print(f"Employee ID: {id}")
    print(f"\tEmployee Details: {emp_dict[id]}")

# Accessing elements from dictionary
# get vs [] for retrieving elements
# Sanjeev
print(emp_dict[100]['name'])

# ['Python', 'AWS', 'AppSec']
print(emp_dict[101].get('skills'))

# Try to access keys which doesn't exist
# None
print(emp_dict[100].get('mailid'))

# KeyError: 'location' Comment below line to execute other lines below
# print(emp_dict[101]['location'])

# Add one more employee to emp_dict using update()
new_emp = {
    102:
        {
            'name': "Rakesh",
            'joined': "2018-01-07",
            'title': "Business Analyst",
            'skills': ['Power BI', 'MBA', 'Marketing Expert'],
            'projects': {
                'Flexmind Marketing': 'Increase the membership my targeted marketing'
            }
        }
}

emp_dict.update(new_emp)
print(emp_dict)

# Update the existing value. Update title of emp_id: 100 as "Sr. Cloud Security Engineer"
emp_dict[100]['title'] = "Sr. Cloud Security Engineer"
print(emp_dict[100])

# Learn to delete
# pop, clear, del
# Pop employee id 101
emp_dict.pop(101, "Not found")
print(len(emp_dict))

# Delete the employee 102
del emp_dict[102]
print(len(emp_dict))

# Clear the dictionary
emp_dict.clear()
print(emp_dict)

# Delete the dictionary itself and printing it would throw an error
del emp_dict
# print(emp_dict)



