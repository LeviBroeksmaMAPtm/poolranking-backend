from chalice import Chalice
import json

app = Chalice(app_name="poolranking-backend")

standings = [
    {
        "player": "Martijn",
        "wins": 0,
        "losses": 0,
        "image": "/players/martijn.png",
    },
    {
        "player": "Wim",
        "wins": 0,
        "losses": 1,
        "image": "/players/wim.png",
    },
    {
        "player": "Mark",
        "wins": 0,
        "losses": 0,
        "image": "/players/mark.png",
    },
    {"player": "Leeroy", "wins": 0, "losses": 0},
    {
        "player": "Levi",
        "wins": 1,
        "losses": 0,
        "image": "/players/levi.png",
    },
    {
        "player": "Marieke",
        "wins": 0,
        "losses": 0,
        "image": "/players/marieke.png",
    },
    {
        "player": "Dennis",
        "wins": 0,
        "losses": 0,
        "image": "/players/dennis.jpg",
    },
    {
        "player": "Koen",
        "wins": 0,
        "losses": 0,
        "image": "/players/koen.png",
    },
    {
        "player": "Floris",
        "wins": 0,
        "losses": 0,
        "image": "/players/floris.jpg",
    },
    {
        "player": "Rick",
        "wins": 0,
        "losses": 0,
        "image": "/players/rick.jpg",
    },
    {
        "player": "Gregor",
        "wins": 0,
        "losses": 0,
        "image": "/players/gregor.jpg",
    },
    {
        "player": "Angelo",
        "wins": 0,
        "losses": 0,
        "image": "/players/angelo.png",
    },
    {
        "player": "Jaap",
        "wins": 0,
        "losses": 0,
        "image": "/players/jaap.png",
    },
    {
        "player": "Audrey",
        "wins": 0,
        "losses": 0,
        "image": "/players/audrey.png",
    },
    {
        "player": "Steven",
        "wins": 0,
        "losses": 0,
        "image": "/players/steven.png",
    },
    {
        "player": "Anton",
        "wins": 0,
        "losses": 0,
        "image": "/players/anton.png",
    },
    {
        "player": "Bart",
        "wins": 0,
        "losses": 0,
        "image": "/players/bart.png",
    },
    {
        "player": "Bert",
        "wins": 0,
        "losses": 0,
        "image": "/players/bert.png",
    },
    {
        "player": "Frank",
        "wins": 0,
        "losses": 0,
        "image": "/players/frank.jpg",
    },
    {
        "player": "Giovanni",
        "wins": 0,
        "losses": 0,
        "image": "/players/giovanni.png",
    },
    {
        "player": "Guido",
        "wins": 0,
        "losses": 0,
        "image": "/players/guido.png",
    },
    {
        "player": "Tessel",
        "wins": 0,
        "losses": 0,
        "image": "/players/tessel.png",
    },
    {
        "player": "Nuno",
        "wins": 0,
        "losses": 0,
        "image": "/players/nuno.png",
    },
    {
        "player": "Susan",
        "wins": 0,
        "losses": 0,
        "image": "/players/susan.jpg",
    },
    {
        "player": "Luc",
        "wins": 0,
        "losses": 0,
        "image": "/players/luc.jpg",
    },
]


@app.route("/", cors=True)
def index():
    message = "This is an API written for the MAPtm Pool Rankings."
    return json.dumps(message)


@app.route("/get-ranking", cors=True)
def get_ranking():
    return_list = sorted(
        standings, key=lambda k: (k["wins"] - k["losses"]), reverse=True
    )
    return return_list


@app.route("/update_score/{id}", methods=["PUT"], cors=True)
def update_score(id, win, loss):
    # here there needs to be looped through the standings list and see which player matches id
    # if the match is found, update wins and losses with the received value.
    # when player has won, we receive (id: "id", win: row.wins + 1, losses: row.losses)
    # when player has lost, we receive (id: "id", win: row.wins, losses: row.losses + 1)
    # after this has been updated, revised ranking should be returned`
    message = "Here you will be able to send the new scores"
    return json.dumps(message)
