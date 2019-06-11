from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere


app = Flask(__name__)


@app.route("/")
def index():
    # This is used to "setup" the session with starting values.
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))


@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get("room_name")
    # return "Hollywood"
    # return room_name
    return render_template("show_rooms.html", room_name=room_name)

app.debug = True
app.secret_key = "Höghults grustag"

if __name__ == "__main__":
    app.run()
