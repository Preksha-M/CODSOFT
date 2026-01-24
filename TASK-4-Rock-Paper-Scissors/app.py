from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "rps_game"

@app.route("/", methods=["GET", "POST"])
def home():
    if "user_score" not in session:
        session["user_score"] = 0
        session["computer_score"] = 0

    user_choice = ""
    computer_choice = ""
    result = ""

    choices = ["Rock", "Paper", "Scissors"]

    if request.method == "POST":
        if "reset" in request.form:
            session["user_score"] = 0
            session["computer_score"] = 0
        else:
            user_choice = request.form["choice"]
            computer_choice = random.choice(choices)

            if user_choice == computer_choice:
                result = "It's a Tie 🤝"
            elif (
                (user_choice == "Rock" and computer_choice == "Scissors") or
                (user_choice == "Scissors" and computer_choice == "Paper") or
                (user_choice == "Paper" and computer_choice == "Rock")
            ):
                result = "You Win 🎉"
                session["user_score"] += 1
            else:
                result = "You Lose 😢"
                session["computer_score"] += 1

    return render_template(
        "index.html",
        user=user_choice,
        computer=computer_choice,
        result=result,
        user_score=session["user_score"],
        computer_score=session["computer_score"]
    )

if __name__ == "__main__":
    app.run(debug=True)
