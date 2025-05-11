from datetime import datetime

import pymongo
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("new web request")

    client = pymongo.MongoClient("mongo-mongo", 27017)
    print("client", client)
    db = client.test
    print("db", db)
    print("db.name", db.name)
    posts = db.posts
    print("posts", posts)

    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }
    post_id = posts.insert_one(post).inserted_id

    return f"hello from disco!!! inserted post with id {post_id}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
