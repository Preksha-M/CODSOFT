from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        contact = {
            "name": request.form["name"],
            "phone": request.form["phone"],
            "email": request.form["email"],
            "address": request.form["address"]
        }
        contacts.append(contact)
        return redirect(url_for("index"))

    return render_template("index.html", contacts=contacts)

@app.route("/search", methods=["POST"])
def search():
    # Use get() with default empty string to avoid KeyError
    keyword = request.form.get("keyword", "").lower()
    
    filtered = [
        c for c in contacts
        if keyword in c["name"].lower() or keyword in c["phone"]
    ]
    return render_template("index.html", contacts=filtered)
    
@app.route("/delete/<int:id>")
def delete(id):
    contacts.pop(id)
    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        contacts[id]["name"] = request.form["name"]
        contacts[id]["phone"] = request.form["phone"]
        contacts[id]["email"] = request.form["email"]
        contacts[id]["address"] = request.form["address"]
        return redirect(url_for("index"))

    return render_template("index.html", contacts=contacts, edit_id=id)

if __name__ == "__main__":
    app.run(debug=True)
