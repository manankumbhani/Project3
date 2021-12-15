from app.controllers.controller import ControllerBase
from flask import render_template

class separationController(ControllerBase):
    @staticmethod
    def get():
        return render_template('Separation.html')

