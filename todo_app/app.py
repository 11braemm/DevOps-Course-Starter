from flask import Flask, render_template, request, redirect
from todo_app.data.ViewModel import ViewModel
from todo_app.data.trello_items import add_item, get_items, mark_item_as_done

from todo_app.flask_config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route("/")
    def index():
        items = get_items()
        item_view_model = ViewModel(items)
        return render_template("index.html", view_model=item_view_model)


    @app.route("/add-item", methods=["POST"])
    def login():
        new_item = request.form["title"]
        add_item(new_item)
        return redirect("/")


    @app.route("/complete-item/<item_id>", methods=["POST"])
    def complete_item(item_id):
        mark_item_as_done(item_id)
        return redirect("/")
    

    return app
