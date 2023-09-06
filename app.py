from flask import Flask, make_response, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

    content = render_template("frontend.html")
    response = make_response(content)
    
    # Check value of cookie
    visitor = request.cookies.get("visitor")

    if visitor and visitor.lower() == "wizard":
        response.headers["Ancient-Rat-Rambles"] = (
        "With your wizardly aura, the rat's gaze shifts, "
        "and it releases its grip on the bars. Its whiskers twitch, " 
        "eyes locking onto yours, gleaming with recognition and power. "
        "A realization dawns within you: "
        "the truth was always present, a spark, a bitter taste, a headache."
        "Having fulfilled its purpose, the rat returns to its vigil state, "
        "paws embracing the bars once more, as if nothing had just occured. "
        "But as a true wizard of enchanted elixirs, "
        "you have unraveled one of many truths: date_flag{D0nk3r0Sha11N0tB3Shugg3d}."
        )
        return response
    
    if visitor and visitor.lower() == "rat":
        response.headers["Ancient-Rat-Rambles"] = (
        "The rat's eyes widen like twin moons, beholding a humongous being among its kind. "
        "It emits a triumphant sequence: 'chirp chirp chorp squeee.' The ancient echoes "
        "unravel the secret, but alas, you are no true rat, and the dialect of rodents "
        "eludes your ears."
        )
        return response
    
    else:
         response.headers["Ancient-Rat-Rambles"] = (
        "The rat gazes at you with wide eyes, its delicate paws clutched around the imprisoning bars.  "
        "Its teeth, worn and resolute, seem to resonate with the unspoken knowledge. Yet, it hesitates, "
        "aware that the secrets it guards are only meant for those who possess the essence of a true wizard."
        )

    # Set cookie to normal value
    response.set_cookie("visitor", value="human")


    return response