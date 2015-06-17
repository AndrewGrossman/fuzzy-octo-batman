

# ZF Django Résumé Exercise

ZF Django Résumé Exercise is an application geared towards reviewing and showing off some various Django skills. 

This project has the following basic app that did not come with the Django edge template:

* Resume (An app for inputting a user's job history and displaying that history in a résumé format)

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

## Design Decisions

The Django Edge template seemed like a good choice for some of the basics, including not reinventing the signup/login wheel.

I felt that only a single model for job positions was needed to represent the business case. If one user maintained multiple résumés, a resume model would have been added to support that.

Django's generic CBV's provide a decent enough set of tools to make a classic web CRUD site for this case. A more modern and perhaps optimal site might have used AJAX requests and perhaps a client-side framework.

Given how resumes are structured, I opted to remove the day part of the employment start and end dates. The database records should probably have the end of the month rather than the beginning for end dates, but it does not make a difference in terms of what this application currently does. 

I would have liked to get the start date and end date fields on the same line on the position form, but that incantation was becoming an overly difficult task for something of this magnitude. I also might have added having a user start on the position adding page, rather than on the blank resume display.

