from collections import namedtuple

from flask import Blueprint, render_template

from github3 import gh

dash = Blueprint('dashboard',
                 __name__,
                 template_folder='../templates/dashboard')


def parse_info(json_data):
    """
    Takes the
    :param json_data:
    :return:
    """
    return json_data['_json_data']


def make_example_data():
    Repository = namedtuple('Repository', 'author name')

    repos = [
        Repository(author='m1yag1',
                   name='simple-flask-heroku'),
        Repository(author='m1yag1',
                   name='ox-sprint'),
        Repository(author='openstax',
                   name='biglearn-sparfa-server')
    ]

    example_data = []

    for r in repos:
        repository = gh.repository(r.author, r.name)
        example_data.append(repository)

    return example_data


@dash.route('/', methods=['GET'])
def dashboard():
    dash_data = make_example_data()

    return render_template('dashboard.html', data=dash_data)
