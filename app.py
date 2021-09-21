from flask import Flask, render_template, request, sessions, redirect, url_for
from data import *
# from constants import *

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    project_list = get_proj_list()
    return render_template("index.html", projects=project_list, home_active=True,
                           projects_active=False, resume_active=False, twitter=TWITTER,
                           github=GITHUB, linkedin=LINKED_IN, logo_url=LOGO_PATH,
                           bg_url=BG_PATH)


@app.route("/projects", methods=["GET", "POST"])
def projects():
    project_list = get_proj_list()
    return render_template("projects.html", projects=project_list, home_active=False,
                           projects_active=True, resume_active=False, twitter=TWITTER,
                           github=GITHUB, linkedin=LINKED_IN, logo_url=LOGO_PATH,
                           bg_url=BG_PATH)


@app.route("/resume", methods=["GET", "POST"])
def resume():
    project_list = get_proj_list()
    return render_template("resume.html", projects=project_list, home_active=False,
                           projects_active=False, resume_active=True, twitter=TWITTER,
                           github=GITHUB, linkedin=LINKED_IN, logo_url=LOGO_PATH,
                           bg_url=BG_PATH)


@app.route("/project-zoom", methods=["GET", "POST"])
def project_zoom():
    return render_template("project-zoom.html", twitter=TWITTER,
                           github=GITHUB, linkedin=LINKED_IN, logo_url=LOGO_PATH,
                           bg_url=BG_PATH)

@app.route("/blog", methods=["GET"])
def blog():
    return render_template("index.html") #temp

def load_project(which_project):
    return redirect(url_for("project_zoom"))


def get_proj_list():
    project_list = []
    for project in PROJECT_TITLE_LIST:
        project_list.append(PROJECT_DICT[project])
    return project_list

if __name__ == '__main__':
    app.run()

