from flask import Flask, make_response, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

    content = render_template("frontend.html")
    response = make_response(content)

    # Check value of cookie
    visitor = request.cookies.get("visitor")

    if visitor == "wizard":
        response.headers["Ancient-Rat-Rambles"] = (
        "With your wizardly aura, the rat's gaze shifts, "
        "and it releases its grip on the bars. Its whiskers twitch, " 
        "eyes locking onto yours, gleaming with recognition and power. "
        "A realization dawns within you: "
        "the truth was always omnipresent, a spark within. "
        "Having fulfilled its purpose, the rat returns to its vigil, "
        "paws embracing the bars once more. It rattles them, "
        "as if to erase the revelation, as if nothing had occurred. "
        "But as a true wizard, you have unraveled the guarded enigma: flag {dddddd}."
        )
        return response
    
    if visitor == "rat":
        response.headers["Ancient-Rat-Rambles"] = (
        "The rat's eyes widen like twin moons, beholding a humongous being among its kind. "
        "It emits a triumphant sequence: 'chirp chirp chorp squeee.' The ancient echoes "
        "unravel the secret, but alas, you are no true rat, and the dialect of rodents "
        "eludes your ears."
        )
        return response
    
    # Set cookie to normal value
    response.set_cookie("visitor", value="human")

    response.headers["Ancient-Rat-Rambles"] = (
    "The rat gazes at you with its wide eyes, its delicate paws clutched around the imprisoning bars.  "
    "Its teeth, worn and resolute, seem to resonate with the unspoken knowledge. Yet, it hesitates, "
    "aware that the secrets it guards are only meant for those who possess the essence of a true wizard."
    )

    return response