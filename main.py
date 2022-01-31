from flask import Flask, render_template, request, url_for, redirect
import db
from models import Tarea

app = Flask(__name__)

@app.route("/")
def saludo():
    tareas = db.session.query(Tarea).all()
    for t in tareas:
        print(t)
    return render_template("index.html", lista_tareas = tareas)

if __name__ == "__main__":
    db.Base.metadata.create_all(db.server)
    app.run(debug=True)
