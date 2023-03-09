# Notes CLI app
This is an basic CLI application that makes an API call to an API running on localhost with some dummy data.

I created the API using **FastAPI**, and I consumed it using the in-built **requests** library

To run this project locally, you need to have python installed.

### Installing Dependencies
>You need to have [git](https://git-scm.com/) inistalled to clone the repository

To clone the repo, run
`git clone https://github.com/datalordstephen/notes-cli-app.git
`

To change directory, run
`cd notes-cli-app`

I made use of the inbuilt **argparse** library to parse arguments from the command line. It comes downloaded with **python3**, so it dosen't need to be downloaded.

To download **FastAPI** with pip, run
`pip install fastapi
`

You'll also need to download an [ASGI server](https://asgi.readthedocs.io/en/latest/), I made use of uvicorn as used in the **FastAPI** [documentation](https://fastapi.tiangolo.com/).
`pip install "uvicorn[standard]"
`

### Running the project
The server needs to be run first. To do that, run
`uvicorn notes-api:app`

The `cli` tool can carry out 4 operations: **fetch all notes**, **create a new note**, **update an existing note**, and **delete a note**.

To **fetch** all dummy notes, run `py notes.py fetch-notes`.

To **create** a new note, run `py notes.py create-note "content"` where *content* should be the content of the note to be created.

To **update** an existing note, run `py notes.py update-note <id> "content"` where *id* is the id of the note you want to update, and *content* is the new content you want to overwrite the note with.

To **delete** a note, run `py notes.py delete-note <id>` where *id* is the id of the note to be deleted.


>Happy testing! :)


