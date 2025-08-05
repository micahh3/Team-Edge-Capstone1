from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

ai_list =["aigirl.jpeg", "aiguy.jpeg","aiwoman"]

real_list =["realguy.jpeg","almondreal.webp","realguy3.jpeg"]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/1")
def aior1():
    score = 0
    return render_template("1.html", score = score)

@app.route("/2")
def aior2():
    return render_template("2.html")

@app.route("/3")
def aior3():
    return render_template("3.html")

@app.route("/4")
def aior4():
    return render_template("4.html")

@app.route("/5")
def aior5():
    return render_template("5.html")

@app.route("/6")
def aior6():
    return render_template("6.html")

@app.route("/7")
def aior7():
    return render_template("7.html")

@app.route("/score")
def score():
    return render_template("score.html")


#scamming pages lolololololololol maybe put cashapp so they actually give me money
@app.route("/scam1.html")
def scamC():
    return render_template("scam1.html")

@app.route("/scam2.html")
def scamD():
    return render_template("scam2.html")
# main driver function
if __name__ == '__main__':
    app.run(debug=True)