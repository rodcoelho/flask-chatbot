#!/usr/bin/env python3

from flask import Flask, render_template, request, session, json

import os, sqlite3

import orm

app = Flask(__name__)

connection = sqlite3.connect('db/entries.db')
cursor = connection.cursor()


@app.route('/', methods=["GET", "POST"])
def index():
    h1 = 'Home'
    title = 'Flask-Twitter'
    tweets = orm.get_all_tweets()
    tweets = tweets[::-1]
    return render_template('index.html', tweets=tweets)

@app.route('/showSignUp', methods=["GET", "POST"])
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=["GET", "POST"])
def signUp():
    _name = request.form['inputName']
    if _name:
        return json.dumps({'html':'<span>All fields good!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/user', methods=["GET", "POST"])
def lookup():
    h1 = 'Tweets'
    title = 'Flask-Twitter'
    _name = request.form['inputName']
    session['_name'] = _name
    # check if user exists, if not create account, either way return userID
    pk = orm.check_if_user_exists(_name)
    # get all tweets from db
    tweets = orm.get_all_tweets()
    tweets = tweets[::-1]
    return render_template('user.html', h1=h1, title=title, _name=_name, tweets=tweets)


@app.route('/tweets', methods=["GET", "POST"])
def tweets():
    h1 = 'Tweets'
    title = 'Flask-Twitter'
    _name = session['_name']
    # check if user exists, if not create account, either way return userID
    pk = orm.check_if_user_exists(_name)
    # get the new tweet
    _tweet = request.form['inputName']
    bot_input = chatterbot.get_response(_tweet)
    # post the new tweet
    orm.post_tweet(_tweet, bot_input, pk)
    # get all tweets from db
    tweets = orm.get_all_tweets()
    tweets = tweets[::-1][::-1]
    return render_template('tweets.html', h1=h1, title=title, _name=_name, tweets=tweets)


app.secret_key = 'canyoukeepasecret'

if __name__ == '__main__':
    ####################################################################################################
    ########################################### CHATBOT LOAD ###########################################
    ####################################################################################################
    from chatterbot import ChatBot

    linkedin = 'https://www.linkedin.com/in/rodcoelho/'
    github = 'https://github.com/rodcoelho'
    new = 2

    from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

    chatterbot = ChatBot(
        'ChatBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.BestMatch',
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter'
        ],
        database='db/database.sqlite3',
        filters=["chatterbot.filters.RepetitiveResponseFilter"]
    )

    # how to train the bot to respond
    chatterbot.set_trainer(ListTrainer)
    linkedin_list = ['CV', 'Resume', 'cv', 'resume', 'linkedin', 'Linkedin']
    github_list = ['Git', 'git', 'github', 'Github', 'projects']

    for words in linkedin_list:
        chatterbot.train([words, linkedin])
    for words in github_list:
        chatterbot.train([words, github])
    chatterbot.train([
        "Who is Rod?",
        linkedin])
    chatterbot.train([
        "What is the best bootcamp?",
        "Byte Academy, is that even a question...?"])

    chatterbot.set_trainer(ChatterBotCorpusTrainer)
    chatterbot.train("chatterbot.corpus.english.greetings")
    chatterbot.train("chatterbot.corpus.english.conversations")
    def openwebsite(link):
        os.system('python -mwebbrowser {}'.format(link))
    def clearmemory():
        os.system('rm database.sqlite3')
        os.system('clear')

    ####################################################################################################
    ########################################### CHATBOT LOAD ###########################################
    ####################################################################################################

    app.run(debug=True)
    session['SECRET_KEY'] = 'canyoukeepasecret'

