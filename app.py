from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame, time #new sound stuff to test



ai_list =["aigirl.jpeg", "aiguy.jpeg","aiwoman,jpeg","aiwoman8.jpeg","aiguy11.jpeg","aiwoman12.jpeg"]

real_list =["realguy.jpeg","almondreal.webp","realguy3.jpeg","reallady7.jpeg","realman9.jpeg","realguy10.jpeg"]

pygame.mixer.init()

global scorevar
scorevar = 0


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
        pygame.mixer.music.load('static/ding.mp3')
        pygame.mixer.music.play()
 
    elif answer == "real":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
    return render_template("2.html")

@app.route("/3/<answer>")
def aior3(answer):
    global scorevar
    if answer == "ai": #handles previous pages' logic/ Page 2 answer
        scorevar = scorevar + 1
        pygame.mixer.music.load('static/ding.mp3')
        pygame.mixer.music.play()
 
    elif answer == "real":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
    return render_template("3.html")

@app.route("/4/<answer>")
def aior4(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 3 answer
        scorevar = scorevar + 1
        pygame.mixer.music.load('static/ding.mp3')
        pygame.mixer.music.play()
 
    elif answer == "ai":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
    return render_template("4.html")

@app.route("/5/<answer>")
def aior5(answer):
    global scorevar
    if answer == "ai": #handles previous pages' logic/ Page 4 answer
        scorevar = scorevar + 1
        pygame.mixer.music.load('static/ding.mp3')
        pygame.mixer.music.play()
 
    elif answer == "real":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
    return render_template("5.html")

@app.route("/6/<answer>")
def aior6(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 5 answer
        scorevar = scorevar + 1
        pygame.mixer.music.load('static/ding.mp3')
        pygame.mixer.music.play()
 
    elif answer == "ai":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
    return render_template("6.html")

@app.route("/7/<answer>")
def aior7(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 6 answer
        scorevar = scorevar + 1
        pygame.mixer.music.load('static/ding.mp3')
        pygame.mixer.music.play()
 
    elif answer == "ai":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
    return render_template("7.html")

@app.route("/8/<answer>")
def aior8(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 7 answer
        scorevar = scorevar + 1
        pygame.mixer.music.load('static/ding.mp3')
        pygame.mixer.music.play()
 
    elif answer == "ai":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
    return render_template("8.html")

@app.route("/9/<answer>")
def aior9(answer):
    global scorevar
    if answer == "ai": #handles previous pages' logic/ Page 8 answer
        scorevar = scorevar + 1
        pygame.mixer.music.load('static/ding.mp3')
        pygame.mixer.music.play()
 
    elif answer == "real":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
    return render_template("9.html")

@app.route("/10/<answer>")
def aior10(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 9 answer
        scorevar = scorevar + 1
        pygame.mixer.music.load('static/ding.mp3')
        pygame.mixer.music.play()
 
    elif answer == "ai":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
    return render_template("10.html")

@app.route("/11/<answer>")
def aior11(answer):
    global scorevar
    if answer == "real": #handles previous pages' logic/ Page 10 answer
        scorevar = scorevar + 1
        pygame.mixer.music.load('static/ding.mp3')
        pygame.mixer.music.play()
 
    elif answer == "ai":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
    return render_template("11.html")

@app.route("/12/<answer>")
def aior12(answer):
    global scorevar
    if answer == "ai": #handles previous pages' logic/ Page 11 answer
        scorevar = scorevar + 1
        pygame.mixer.music.load('static/ding.mp3')
        pygame.mixer.music.play()
 
    elif answer == "real":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
    return render_template("12.html")

@app.route("/score/<answer>")
def score(answer):
    global scorevar
    if answer == "ai":
            scorevar = scorevar + 1
            pygame.mixer.music.load('static/ding.mp3')
            pygame.mixer.music.play()
 
    elif answer == "real":
        pygame.mixer.music.load('static/buzzer.mp3')
        pygame.mixer.music.play()
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