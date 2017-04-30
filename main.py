from flask import Flask, request, render_template, redirect, url_for
from datamanager import *

app = Flask(__name__)


@app.route("/story", methods=["GET"])
def create_story():
    return render_template("form.html")


@app.route("/story", methods=["POST"])
def story_add():
    stories = open_from_database()
    new_stories = []
    new_stories.insert(0, generate_id(stories))
    form_elements = [
                    "story_title",
                    "user_title",
                    "acceptance_criteria",
                    "business_value",
                    "estimation_h",
                    "status"
                    ]
    for name in form_elements:
        new_stories.append(request.form[name])
    stories.append(new_stories)
    write_to_database(stories)
    return redirect(url_for("list_handler"))


@app.route("/list", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def list_handler():
    stories = open_from_database()
    form_table_headers = [
                        "#ID",
                        "Story Title",
                        "User Title",
                        "Acceptance Criteria",
                        "Business Value",
                        "Estimation",
                        "Status",
                        "Edit",
                        "Delete"
                        ]
    return render_template("list.html", stories=stories, form_table_headers=form_table_headers)

'''
@app.route("/delete_story", methods=["POST"]):
'''


if __name__ == '__main__':
    app.run(debug=True)
