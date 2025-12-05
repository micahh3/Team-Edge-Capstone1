from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
# import playsound

ai_list =["aigirl.jpeg", "aiguy.jpeg","aiwoman,jpeg","aiwoman8.jpeg","aiguy11.jpeg","aiwoman12.jpeg"]

real_list =["realguy.jpeg","almondreal.webp","realguy3.jpeg","reallady7.jpeg","realman9.jpeg","realguy10.jpeg"]

# initialval = 0
# scorevar = initialval
# pagenum = 7
#Keep checking when scorevar changes; thats when you know user got correct answer. Inside the loop, if changed == true; Play sound to notify the user got the correct answer. 
global scorevar
# def addscore(score):
#     scorevar += score
# playsound(the path) # add in the path for the file and then replace all lines that manually add it to play the sound 

@app.route("/")
def index():
    global scorevar
    scorevar = 0
    return render_template("index.html")

@app.route("/1")
def aior1():
    return render_template("1.html")

@app.route("/2/<answer>")
def aior2(answer):
    global scorevar
    if answer == "ai": #handles previous pages' logic/ Page 1 answer
        scorevar = scorevar + 1
    return render_template("2.html")

@app.route("/3/<answer>")
def aior3(answer):
    global scorevar
    if answer == "ai": #handles previous pages' logic/ Page 2 answer
        scorevar = scorevar + 1
    return render_template("3.html")

@app.route("/4/<answer>")
def aior4(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 3 answer
        scorevar = scorevar + 1
    return render_template("4.html")

@app.route("/5/<answer>")
def aior5(answer):
    global scorevar
    if answer == "ai": #handles previous pages' logic/ Page 4 answer
        scorevar = scorevar + 1
    return render_template("5.html")

@app.route("/6/<answer>")
def aior6(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 5 answer
        scorevar = scorevar + 1
    return render_template("6.html")

@app.route("/7/<answer>")
def aior7(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 6 answer
        scorevar = scorevar + 1
    return render_template("7.html")

@app.route("/8/<answer>")
def aior7(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 6 answer
        scorevar = scorevar + 1
    return render_template("8.html")

@app.route("/9/<answer>")
def aior9(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 6 answer
        scorevar = scorevar + 1
    return render_template("9.html")

@app.route("/10/<answer>")
def aior10(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 6 answer
        scorevar = scorevar + 1
    return render_template("10.html")

@app.route("/11/<answer>")
def aior11(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 6 answer
        scorevar = scorevar + 1
    return render_template("11.html")

@app.route("/12/<answer>")
def aior12(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 6 answer
        scorevar = scorevar + 1
    return render_template("12.html")

@app.route("/score/<answer>")
def score(answer):
    global scorevar
    if answer == "ai":
            scorevar = scorevar + 1
    return render_template("score.html",scorevar = scorevar) #find way to print finalscore on html page

@app.route("/aboutmyproject")
def aboutme():
    return render_template("aboutmyproject.html")


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