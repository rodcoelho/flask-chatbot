#!/usr/bin/env python3

from flask import Flask, render_template, request, session, json
app = Flask(__name__)

import sqlite3

import orm

connection = sqlite3.connect('db/twitter.db')
cursor = connection.cursor()


@app.route('/', methods=["GET", "POST"])
def index():
    h1 = 'Home'
    title = 'Flask-Twitter'
    tweets = orm.get_all_tweets()
    print(tweets)

    tweets = tweets[::-1]
    return render_template('index.html', tweets=tweets)

@app.route('/showSignUp', methods=["GET", "POST"])
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=["GET", "POST"])
def signUp():
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
    tweets = orm.get_tweets_if_any(pk)
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
    # post the new tweet
    orm.post_tweet(_tweet, pk)
    # get all tweets from db
    tweets = orm.get_tweets_if_any(pk)
    tweets = tweets[::-1]
    return render_template('tweets.html', h1=h1, title=title, _name=_name, tweets=tweets)



app.secret_key = 'poop'

if __name__ == '__main__':
    app.run(debug=True)
    session['SECRET_KEY'] = 'poop'

