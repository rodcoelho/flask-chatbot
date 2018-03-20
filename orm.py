import sqlite3

connection = sqlite3.connect('db/entries.db')
cursor = connection.cursor()

#add user
# cursor.execute("""
# INSERT INTO users(name, password)
# VALUES ('{}','{}');
#     """.format('rodrigo', 'swordfish'))


def check_if_user_exists(_name):
    connection = sqlite3.connect('db/entries.db')
    cursor = connection.cursor()

    #check if user exists
    cursor.execute("""
                SELECT * FROM users WHERE name = '{}'
                            ;
                                """.format(_name))
    info = cursor.fetchall()
    if len(info) == 0:
        # if user does not exist, create an account for them
        cursor.execute("""
        INSERT INTO users(name)
        VALUES ('{}');
             """.format(_name))
        connection.commit()

    # return userID
    cursor.execute("""
                    SELECT pk FROM users WHERE name = '{}'
                                ;
                                    """.format(_name))
    pk = cursor.fetchone()
    return pk


def get_tweets_if_any(pk):
    connection = sqlite3.connect('db/entries.db')
    cursor = connection.cursor()

    # get all tweets with userID
    cursor.execute("""
                    SELECT pk, tweet, response FROM tweets WHERE userID = '{}'
                                ;
                                    """.format(pk))
    tweets = cursor.fetchall()
    return tweets


def get_all_tweets():
    connection = sqlite3.connect('db/entries.db')
    cursor = connection.cursor()

    # get all tweets with userID
    cursor.execute("""
                        SELECT TWEETS.tweet, USERS.name, TWEETS.response FROM tweets INNER JOIN users on users.pk = tweets.userID;
                                        """.format())
    tweets = cursor.fetchall()
    return tweets


def post_tweet(words, botresponse, userID):
    connection = sqlite3.connect('db/entries.db')
    cursor = connection.cursor()
    cursor.execute("""
            INSERT INTO tweets(userID,tweet,response)
            VALUES ("{}","{}","{}");
                 """.format(str(userID[0]), str(words), str(botresponse)))
    connection.commit()

