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


@app.route("/story_delete", methods=["POST"])
def delete_story():
    stories = open_from_database()
    id_of_story = request.form["delete_button"]
    for story in stories:
        if story[0] == id_of_story:
            stories.remove(story)
    write_to_database(stories)
    return redirect(url_for("list_handler"))


@app.route("/story/<id_of_story>", methods=["POST"])
def edit_story(id_of_story=None):
    '''
        Fills in the data from the database when clicked on the edit button
    '''
    stories = open_from_database()
    id_of_story = request.form["edit_button"]
    edited_story = []
    for editstory in stories:
        if editstory[0] == id_of_story:
            for item_in_row in editstory:
                edited_story.append(item_in_row)
    return render_template("form.html", id_of_story=id_of_story, edited_story=edited_story)


@app.route("/edit", methods=["POST"])
def update_story():
    '''
        Fills in the data to the database from the edit page
    '''
    stories = open_from_database()
    id_of_story = request.form["edit"]
    for story in stories:
        if story[0] == id_of_story:
            stories.remove(story)
    edited_story = [id_of_story]
    form_elements = [
                    "edited_story_title",
                    "edited_user_title",
                    "edited_acceptance_criteria",
                    "edited_business_value",
                    "edited_estimation_h",
                    "edited_status"
                    ]
    for element in form_elements:
        edited_story.append(request.form[element])
    stories.append(edited_story)
    write_to_database(stories)
    return redirect(url_for("list_handler"))


if __name__ == '__main__':
    app.run(debug=True)
