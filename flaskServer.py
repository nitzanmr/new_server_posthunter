from flask import Flask, request, jsonify, render_template
# from postgres_insert import connect_db, get_data_from_db, add_data
from datetime import datetime
from flask_socketio import SocketIO
from flask_cors import CORS
import json

# conn = connect_db() # TODO check if it is setting correctly
app = Flask(_name_)
CORS(app, resources={r"*": {"origins": "*"}})
app.config['SECRET_KEY'] = 'posthunter1!'
socketio = SocketIO(app)


# @sock.route('/')
# def handle_connect():
#     print('New connection established')


@app.route('/')
def index():
    return 'SUCCESS TO CONNECT TO BACKEND SERVER'
    #return render_template('index.html')


# tweet_id = int 
# username = string name of company
# standart_link = tweeter/companyname
# status_link = url standart 
# analytics_link = ###

def read_tweets_from_file():
    try:
        with open('tweets.txt', 'r') as file:
            tweets = json.load(file)
        return tweets
    except FileNotFoundError:
        return []

@app.route('/storeTweet', methods=['POST'])
def write_tweet_to_file():
    try:
        tweet = request.json
        tweets = read_tweets_from_file()
        tweets.append(tweet)
        with open('tweets.txt', 'w') as file:
            file.write(json.dumps(tweets))  # Convert the JSON object to a string
        print('Tweet written to file successfully.')
        return json.dumps(tweet)  # Return the JSON object as a response
    except Exception as e:
        print('Error writing to file:', str(e))
        return json.dumps({'error': str(e)}), 500  # Return an error response with 500 status code
    
@app.route('/getTweets', methods=['GET'])    
def read_tweet_to_file():
    try:
        with open('tweets.txt', 'r') as file:
            content = file.read()
            print('content from file: ', content)
            return content
    except Exception as e:
        print('Error writing to file:', str(e))
        return e
    
    
# @app.route('/tweets', methods=['POST'])
# def add_tweet():
#     try:
#         tweet = request.json
#         tweet['timestamp'] = datetime.now().isoformat()
#         add_data(conn, tweet)
#         result = get_data_from_db(conn, tweet['tweet_id'])
#         emit('reported_tweets', result)
#         return jsonify(result), 201
#     except Exception as ex:
#         return "Error adding tweet: " + ex, 406


# @app.route('/tweets/<int:tweet_id>', methods=['GET'])
# def get_tweet(tweet_id):
#     # conn = connect_db()
#     data = get_data_from_db(conn, tweet_id)
#     return data


if _name_ == '_main_':
    app.run(port=81)
    socketio.run(app)