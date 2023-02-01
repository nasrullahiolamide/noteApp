# Note App
This is a command line note taking app that implements CRUD with `requests` module in python
The app consume the api `"https://63a52acf821953d4f2c41d5e.mockapi.io/api/v1/"`

## End points
`GET /notes` : to fetch all notes
`POST /notes` : to create a new note
`PUT /notes/:id` to edit a note content
`DELETE /notes/:id` to delete a note from storage


### Usage 
- clone the repository to your PC
- navigate into the directory or open the directory in the terminal
- type python3 note.py <command> args
        
            For create-note: python3 note.py create-note note-content
            For update-note: python3 note.py update-note id note-content
            For delete-note: python3 note.py delete-note id 
            For fetch-note: python3 note.py fetch-note


_The project is a capstone project for **The Python Backend Growth Tracker** by Bahdcoder_