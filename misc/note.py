from flask import render_template

def create_note(content):
    return render_template("note.html", content=content)