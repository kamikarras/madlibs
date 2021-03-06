"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("player")
    play_game = request.args.get("game")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           player=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Shows madlib form"""

    play_game = request.args.get("game")

    player = request.args.get("player")

    if play_game == "no":
        return render_template("goodbye.html",
                               player=player)
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    noun = request.args.get("noun")
    person = request.args.get("person")
    color = request.args.get("color")
    adjective = request.args.get("adjective")
    game_type_lunch = request.args.get("game_type_lunch")
    game_type_spooky = request.args.get("game_type_spooky")
    return render_template(
        "madlib.html",
        noun=noun,
        person=person,
        color=color,
        adjective=adjective,
        game_type_spooky=game_type_spooky,
        game_type_lunch=game_type_lunch
    )





if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
