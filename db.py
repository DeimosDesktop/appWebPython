#Importar clases del ORM
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Creo las instancias para definir la BBDD
server = create_engine("sqlite:///Database/tareas.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=server)
session = Session()
Base = declarative_base()
