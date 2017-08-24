from flask import Blueprint, render_template

dash = Blueprint('dashboard',
                 __name__,
                 template_folder='../templates/dashboard')


@dash.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

