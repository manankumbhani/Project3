"""A simple flask web app"""
from flask import Flask

from app.controllers.aaa_controller import AAAController
from app.controllers.calcWeb_controller import calcWebController
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.history_controller import HistoryController
from app.controllers.oop_controller import OOPController
from app.controllers.separation_controller import separationController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/history", methods=['GET'])
def history_get():
    return HistoryController.get()

@app.route("/oop", methods=['GET'])
def oop_get():
    return OOPController.get()

@app.route("/aaa", methods=['GET'])
def aaa_get():
    return AAAController.get()

@app.route("/calcWeb", methods=['GET'])
def calcWeb_get():
    return calcWebController.get()

@app.route("/separation", methods=['GET'])
def separation_get():
    return separationController.get()

