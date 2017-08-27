import logging
from collections import namedtuple

from flask import Blueprint, render_template

from github3 import gh, GitHubError

__logs__ = logging.getLogger(__name__)


dash = Blueprint('dashboard',
                 __name__,
                 template_folder='../templates/dashboard')


def make_example_data():
    """
    Temoporary utility to generate example data while trying to figure out
    how I want the widgets to look like.

    :return: example_data
    """
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
        try:
            repository = gh.repository(r.author, r.name)
            example_data.append(repository)
        except GitHubError:
            __logs__.error('The example data was unable to be loaded. The free'
                             'API limit was probably reached.')

    return example_data


@dash.route('/', methods=['GET'])
def dashboard():
    dash_data = make_example_data()
    return render_template('dashboard.html', data=dash_data)
