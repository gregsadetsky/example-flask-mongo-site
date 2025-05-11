from datetime import datetime

import pymongo
from flask import Flask

app = Flask(__name__)

# assumes that the
# https://github.com/letsdiscodev/example-mongo
# repo has been deployed as a separate Disco project
client = pymongo.MongoClient("mongo-mongo", 27017)


@app.route("/")
def hello_world():
    print("new web request")

    db = client.test
    posts = db.posts

    post = {
        "author": "Mike",
        "text": "A new blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.now(),
    }
    post_id = posts.insert_one(post).inserted_id

    return f"hello from disco!!! inserted post into Mongo with id {post_id}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
