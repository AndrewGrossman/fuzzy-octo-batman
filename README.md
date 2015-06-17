

# ZF Django Resume Exercise

ZF Django Resume Exercise is an application geared towards reviewing and showing off some various Django skills. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic app that did not come with the Django edge template:

* Resume (An app for inputting a user's job history and displaying that history in a resume format)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv resume_exercise`
    2. `$ . resume_exercise/bin/activate`

Before installing all dependencies, you may need to install gcc and the Python development package (Python.h, etc...). Installing the dependencies may require building Pillow.

Install all dependencies:

    pip install -r requirements.txt

The git repository comes with a ready database. Feel free to delete it (src/db.sqlite3) and run migrations for a fresh database:

    python manage.py migrate

This project made use of the [Django Edge template](http://django-edge.readthedocs.org/), as well as [Django Crispy Forms](http://django-crispy-forms.readthedocs.org/), and the [Bootstrap themed Django DateTime Widget](https://github.com/asaglimbeni/django-datetime-widget).

