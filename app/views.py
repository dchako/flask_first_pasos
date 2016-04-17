from flask import Flask, jsonify, request, render_template
from app import app

@app.route("/")
def home():
    return "Hellos from Flask"

@app.route("/home")
def home_2():
    return render_template('home.html', name="Saludos")

@app.route("/texto/<Saludos>")
def Saludos(Saludos=None):
    return render_template('saludos.html', name=Saludos)
