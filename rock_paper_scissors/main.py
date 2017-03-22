import flask
from random import randint


app = flask.Flask(__name__, static_url_path='')
app.secret_key = "dj4390ksjvvcsdfj4f0kc"

moves = ['rock', 'paper', 'scissors']

def choose_random_move():
    return moves[randint(0, len(moves)-1)]

def get_winner(my_move, their_move):
    if my_move == their_move:
        return "draw"

    if my_move == 'rock':
        if their_move == 'scissors':
            return "me"
        else:
            return "them"

    if my_move == 'scissors':
        if their_move == 'rock':
            return "them"
        else:
            return "me"

    if my_move == 'paper':
        if their_move == 'rock':
            return "me"
        else:
            return "them"


@app.route("/")
def index():
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('login'))
    else:
        return flask.render_template('make_move.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' in flask.session:
        return flask.redirect(flask.url_for('index'))

    try:
        username = flask.request.form['username']
        username.strip()
        if len(username) == 0:
            return flask.render_template('login.html')
        else:
            flask.session['username'] = username
            return flask.redirect(flask.url_for('index'))
    except Exception as e:
        print(e)
        return flask.render_template('login.html')

@app.route("/logout", methods=['GET'])
def logout():
    flask.session.pop('username', None)
    return flask.redirect(flask.url_for('login'))

@app.route("/make_move", methods=['POST'])
def make_move():
    if not 'username' in flask.session:
        return flask.redirect(flask.url_for('login'))

    user_move = flask.request.form['move']
    print("user made move " + user_move)

    my_move = choose_random_move()
    turn_winner = get_winner(my_move, user_move)

    return flask.render_template('move_made.html',
        user_move=user_move,
        my_move=my_move,
        winner=turn_winner)

if __name__ == "__main__":
    app.run()
