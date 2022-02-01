#############################################
## Visita mirpas.com para más información. ##
#############################################

#Importar las clases necesarias unicamente
from flask import Flask, render_template, request, url_for, redirect
import db
from models import Tarea

#Inicializa el servidor local
app = Flask(__name__)

#Función para la página principal
@app.route("/")
def saludo():
    tareas = db.session.query(Tarea).all()
    for t in tareas:
        print(t)
    return render_template("index.html", lista_tareas = tareas)
    
@app.route("/crear-tarea", methods=["post"])
def crear():
    tarea = Tarea(contenido=request.form['contenido_tarea'], hecha=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for('saludo'))

if __name__ == "__main__":
    db.Base.metadata.create_all(db.server)
    app.run(debug=True)

