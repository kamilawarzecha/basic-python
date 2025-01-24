from flask import Flask, render_template, request, Response

app = Flask(__name__)

movies = {
    "favourite": ["A New Hope", "Empire Strikes Back", "Return of the Jedi",
                  "The Force Awakens", "Jaws", "Predator", "Mad Max",
                  "Back to the Future", "2001: A Space Odyssey", "Robocop",
                  "The Hitchhiker's Guide to the Galaxy", "Doctor Who",
                  "Aliens", "Alien", "Terminator", "Blade Runner", "Matrix"],

    "hated": ["The Phantom Menace", "Attack of the Clones", "Star Trek",
              "Alien Resurrection", "Twilight"]

}

@app.route('/movies', methods=['GET', 'POST'])
def view_movies():
    if request.method == "GET":
        return render_template("zadanie6_formularz.html")
    elif request.method == "POST":
        title = request.form['title']
        if title in movies['favourite']:
            return render_template("zadanie6_formularz.html", message="favourite")
        elif title in movies['hated']:
            return render_template("zadanie6_formularz.html", message="hated")
        else:
            return render_template("zadanie6_formularz.html", message="no such movie!")




if __name__ == "__main__":
    app.run(debug=True)
