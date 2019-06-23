from flask import Flask, session, redirect, url_for, request
# from flask import escape
# escape will probably be necessary later on.
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
    if request.method == 'GET':
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template('show_rooms.html', room=room)
        else:
            # Is this really neccessary?
            render_template('you_are_dead.html')
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)

        return redirect(url_for("game"))
        # y = next_room

app.debug = True
app.secret_key = "Höghults grustag"


if __name__ == "__main__":
    app.run()
