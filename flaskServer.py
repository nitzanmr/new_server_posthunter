from flask import Flask, request, jsonify, render_template
from postgres_insert import connect_db, get_data_from_db, add_data
from datetime import datetime
from flask_socketio import SocketIO


conn = connect_db() # TODO check if it is setting correctly
app = Flask(__name__)
app.config['SECRET_KEY'] = 'posthunter1!'
socketio = SocketIO(app)


@sock.route('/')
def handle_connect():
    print('New connection established')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweets', methods=['POST'])
def write_tweet_to_file(tweet):
    try:
        with open('tweets.txt', 'w') as file:
            file.write(tweet)
        print('File written successfully.')
    except Exception as e:
        print('Error writing to file:', str(e))

@app.route('/tweets/<int:tweet_id>', methods=['GET'])    
def read_tweet_to_file(tweet_id):
    try:
        with open('tweets.txt', 'r') as file:
            content = file.read()
            return content
        print('File written successfully.')
    except Exception as e:
        print('Error writing to file:', str(e))

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


if __name__ == '__main__':
    app.run(port=81)
    socketio.run(app)
    