#-------------------------------------------------------------------------------
# Name:        Modulo Otro
# Purpose:     Sacarle nota a Daza 2(.(w/4))
#
# Author:      Alguien diferente
#
# Created:     19/09/1999
# Copyright:   (TM) ays 2021(?)
# Licence:     <uranus>
#-------------------------------------------------------------------------------

#importe de librerias
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

URI = 'postgres://hoxwkmyfqupeab:c48a884b0095d4d7094b2543608cc2d10c58209a3370355bba9da6477a1c5f16@ec2-174-129-18-210.compute-1.amazonaws.com:5432/d1hi9b9fumoerc'

from Interfaz import db

#definicion tabla usuario
class usuario(db.Model):
    __tablename__ = 'usuario'
    __table_args__ = (
        db.CheckConstraint("nom_usu ~* '^[A-Za-z0-9._%-]+$'"),
        )
    id_usu = db.Column(db.Integer, primary_key=True, nullable=False)
    nom_usu = db.Column(db.String(200), unique=True, nullable=False)
    contra_usu = db.Column(db.String(200), nullable=False)
    realizo = db.relationship('rutina',
        backref=db.backref('realizada', lazy='dynamic'))

    def __init__(self, nom: str, passs: str):
        '''
        Objeto en base de datos usuario
        Parametros:
            nom (str): Cadeda unica que identifica al usuario
            pass (str): Clave del usuario para poder acceder a su registro
        '''
        self.nom_usu = nom
        self.contra_usu = passs

    def __repr__(self) -> str:
        '''
        Representacion en forma de cadena que retornara al solicitar un usuario
        Retorno:
            Cadena de caracteres con el nombre unico del usuario
        '''
        return '<Usuario %r>' % self.nom_usu

#definicion tabla usuario
class rutina(db.Model):
    __tablename__ = 'rutina'
    id_rut = db.Column(db.Integer, primary_key=True, nullable=False)
    nom_rut = db.Column(db.String(200), nullable=False)
    date_rut = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    inter_rut = db.Column(db.Integer, nullable=False)
    repos_rut = db.Column(db.Integer, nullable=False)
    total_rut = db.Column(db.Integer, nullable=False)
    esper_rut = db.Column(db.Integer, nullable=False)

    def __init__(self, nom: str, date: str, inter: int, repos: int, total: int, esper: int):
        '''
        Objeto en base de datos rutina
        Parametros:
            documente manperra D:<
        '''
        self.nom_rut = nom
        self.date_rut = date
        self.inter_rut = inter
        self.repos_rut = repos
        self.total_rut = total
        self.esper_rut = esper

    def __repr__(self) -> str:
        '''
        documente manperra D:<
        Retorno:
            documente manperra D:<
        '''
        return '<Rutina %r hecha %r>' % (self.nom_rut, self.date_rut)
