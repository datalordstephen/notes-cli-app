import requests
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

# creating parser 
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)

# adding subparsers to ask for different inputs depending on the action chose
subparsers = parser.add_subparsers(dest='subcommand')

# adding the 'fetch-notes' subparser
parser_fetch = subparsers.add_parser('fetch-notes')

# adding the 'create-note' subparser and required 'content' argument
parser_create = subparsers.add_parser('create-note')
parser_create.add_argument('content', help="content to add to the new note", type=str)

# adding the 'update-note' subparser and required 'content' and 'id' arguments
parser_update = subparsers.add_parser('update-note')
parser_update.add_argument('id', help="id of the note to update", type=int)
parser_update.add_argument('content', help="content to update the file with", type=str)

# adding the 'delete-note' subparser and the 'id' argument
parser_delete = subparsers.add_parser('delete-note')
parser_delete.add_argument('id', help="id of the note to update", type=int)

args = parser.parse_args()

if args.subcommand == "create-note":
    r = requests.post("http://127.0.0.1:8000/notes", params={"content": args.content})
    print(r.json())

elif args.subcommand == "fetch-notes":
    r = requests.get("http://127.0.0.1:8000/notes")
    print(r.json())
elif args.subcommand == "delete-note":
    r = requests.delete(f"http://127.0.0.1:8000/notes/{args.id}")
    print(r.json())
else:
    r = requests.put(
        f"http://127.0.0.1:8000/notes/{args.id}", params={"content": args.content})
    print(r.json())

