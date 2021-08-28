from flask import Flask

def create_app():

    app = Flask(__name__)

    #Import a module/component using its blueprint handler variable
    from myapp.student_details.views import mod as student_module

    #Register blueprint(s)
    app.register_blueprint(student_module)

    return app