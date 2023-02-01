#!/usr/bin/python3
import requests

# api
base_url = "https://63a52acf821953d4f2c41d5e.mockapi.io/api/v1/"

# Fetch all notes
def fetch_notes():
    response = requests.get(base_url + '/notes/')
    if response.status_code == 200:
        print('Notes retrieved successfully')
        return response.json()
    else:
        print('Failed to retrieve notes')

# Delete note
def delete_note(id):
    response = requests.delete(base_url + '/notes/' + str(id))
    if response.status_code == 200:
        print('Notes with id {} deleted successfully'.format(id))
        return response.json()
    else:
        print('Failed to delete notes')

# create new note
def create_note(content):
    data = {"content": content}
    response = requests.post(base_url + '/notes/', json=data)
    if response.status_code == 201:
        print('Note with content "{}" has been successfully created!'.format(content))
    else:
        print(response.status_code)
        print('Failed to create note')

# update note content
def update_note(id, content):
    data = {"content":content}
    response = requests.put(base_url + '/notes/' + str(id), json=data)
    if response.status_code == 200:
        print('Note with id {} updated with "{}" successfully'.format(id, content))
    else:
        print('Failed to update')


# fetch a particular note
def get_a_note(id):
    response = requests.get(base_url + '/notes/')
    if response.status_code == 200:
        for i in response.json():
            if i['id'] == str(id):
                print(i['content'])
    else:
        print('not found')
        print(response.status_code)
