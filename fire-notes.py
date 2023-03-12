import fire
import requests

def fetch_notes():
    return requests.get("http://localhost:8000/notes").json()


def create_note(content: str):
    return requests.post("http://localhost:8000/notes", params={"content": content}).json()


def delete_note(note_id: int):
    return requests.delete(f"http://localhost:8000/notes/{note_id}").json()


def update_note(note_id: int, content: str):
    return requests.put(f"http://localhost:8000/notes/{note_id}", params={"content": content}).json()

if __name__ == "__main__":
    fire.Fire()