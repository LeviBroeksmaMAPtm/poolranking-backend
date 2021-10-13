from chalice import Chalice
import json
import psycopg2

app = Chalice(app_name="poolranking-backend")


@app.route("/", cors=True)
def index():
    message = "This is an API written for the MAPtm Pool Rankings."
    return json.dumps(message)


@app.route("/get-ranking", cors=True)
def get_ranking():
    return_list = sorted(
        standings_to_return, key=lambda k: (k["wins"] - k["losses"]), reverse=True
    )
    return return_list


@app.route("/get_player_by_id/{id}", cors=True)
def get_single_player(id):
    for row in standings:
        if(row['id'] == id):
            print(row)


@app.route("/update_score/{id}", methods=["PUT"], cors=True)
def update_score(id):
    # here there needs to be looped through the standings list and see which player matches id
    # if the match is found, update wins and losses with the received value.
    # when player has won, we receive (id: "id", win: row.wins + 1, losses: row.losses)
    # when player has lost, we receive (id: "id", win: row.wins, losses: row.losses + 1)
    # after this has been updated, revised ranking should be returned

    body = app.current_request.json_body
    wins = body['wins']
    losses = body['losses']

    # connect to DB
    con = psycopg2.connect(
        database="poolranking",
        user="postgres",
        password="Funky213.")

    # cursor
    cur = con.cursor()

    # execute query for fetch all
    cur.execute("select id, player, wins, losses, image from scores")

    # add data from DB to variable
    standings = cur.fetchall()

    standings_to_return = []

    # creating list from tupels
    for row in standings:
        row = {
            "id": row[0],
            "player": row[1],
            "wins": row[2],
            "losses": row[3],
            "image": row[4],
        }
        standings_to_return.append(row)

    try:
        cur = con.cursor()
        for row in standings_to_return:
            if(wins != row['wins']):
                cur.execute("UPDATE scores SET wins = %s WHERE id = %s", (wins, int(body['id'])))

            if (losses != row['losses']):
                cur.execute("UPDATE scores SET losses = %s WHERE id = %s", (losses, int(body['id'])))
        con.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return json.dumps("Succes")