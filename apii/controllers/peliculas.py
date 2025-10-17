import os
from flask import Blueprint, request, jsonify
from services.service import pelicula
pelicula_bp = Blueprint("pelicula_bp, __name__")

from config.config import get_db_session

service = pelicula (get_db_session)

pelicula_bp = Blueprint("pelicula_bp, __name__")



@pelicula_bp.route("pelicula", methods=["GET"])
def get_pelicula():

    pEñicula= service.listar_pelicula()
    return jsonify([{"id": l.id, "name": l.name} for l in pelicula]), 200 

@pelicula_bp.route("/pelicula/<int:id>", methods=["GET"]) 
def obtener_pelicula_por_ID(pelicula_id):

    pelicula = service.obtener_pelicula(pelicula_id)
    if pelicula:
        return jsonify({"id": pelicula.id, "name": pelicula.name}), 200 
    return jsonify({"error": "pelicula no encontrado"}), 404 



@pelicula_bp.route("\pelicula", methods=["POST"])
def create_pelicula():
    
    data=request.get_json()
    name=data.get("name")
    if not name:
        return jsonify({"error": "El nombre es obligatorio"}), 400 
    band = service.crear_banda(name)
    return jsonify({"id": band.id, "name": band.name}), 201 


@pelicula_bp.route("/pelicula/<int:id>", methods=["PUT"])
def actualizar_pelicula(pelicula_id):

    data=request.get_json()
    name=data.get("name")
    pelicula=service.actualizar_pelicula(pelicula_id, name)

    if pelicula:
        return jsonify({"id": pelicula_id, "name": pelicula.name}), 200
    return jsonify({"error": "pelicula no encontrado"}), 404


@pelicula_bp.route("/pelicula/<int:id>", methods=["DELETE"])
def eliminar_pelicula(pelicula_id):
    
    pelicula = service,eliminar_pelicula(pelicula_id)
    if pelicula:
        return jsonify({"message": "pelicula eliminado"}), 200
    return jsonify({"error": "pelicula no encontrado"}), 404