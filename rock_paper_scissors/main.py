import flask
import random


app = flask.Flask(__name__, static_url_path='')

moves = ['rock', 'paper', 'scissors']

def choose_random_move():
    return moves[random.randint(0, len(moves)-1)]

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
    return flask.send_from_directory("html/", 'index.html')

@app.route("/make_move", methods=['POST'])
def make_move():
    user_move = flask.request.form['move']
    print("user made move " + user_move)

    our_move = choose_random_move()
    turn_winner = get_winner(our_move, user_move)

    return flask.render_template('move_made.html',
        user_move=user_move,
        our_move=our_move,
        winner=turn_winner)

if __name__ == "__main__":
    app.run()
