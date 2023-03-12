from fastapi import FastAPI

app = FastAPI()
notes = [
    {"id": 1, "content": "This is a simple project I quickcly whipped up to practice APIs"},
    {"id": 2, "content": "Made by Stephen Adegbokun"},
    {"id": 3, "content": "It's a CRUD API with a separate script that consumes it"},
    {"id": 4, "content": "Feel free to play with the script and experiment :)"}
]


@app.get("/notes")
def return_all():
    return {"notes": notes}


@app.post("/notes")
def new_note(content: str):
    notes.append({
        "id": notes[-1]["id"] + 1,
        "content": content
    })
    return {"status": 200, "message": "successfully added note!"}


@app.put("/notes/{note_id}")
def update_note(note_id: int, content: str):
    if notes[-1]["id"] >= note_id:
        notes[note_id - 1]["content"] = content
        return {"message": f"successfully updated note number {note_id}"}
    return {"message": f"Number of entries({len(notes)}) isn't up to {note_id}."}


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    global notes
    if len(notes) >= note_id:
        notes.pop(note_id - 1)

        # updating indexes of note objects in the list
        notes = [{"id": id+1, "content": note["content"]}
                 for id, note in enumerate(notes)]
        return {"message": f"successfully deleted note number {note_id}"}
    return {"message": f"Number of entries({len(notes)}) isn't up to {note_id}."}
