from sqlalchemy import Column, Integer, String, Boolean
import db

class Tarea(db.Base):
    __tablename__="Tarea"
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)

    def __init__(self, contenido, hecha):
        self.contenido = contenido
        self.hecha = hecha
    
    def __str__(self):
        return "Se ha creado la tabla Tareas en la BBDD"
