from flask import Flask, render_template, request
from flask.json import jsonify
import os
from llama_index import SimpleDirectoryReader, VectorStoreIndex, StorageContext

app = Flask(__name__)

# versions of the chatbot (different version for each module)
# ensure that the version name matches the file path of the source documents
versions = ["PC3131", "CS2131"]

@app.route("/chat", methods=['POST'])
def chat():
    user_response = request.json

    response = f"you sent {user_response}: <insert chatbot response>"

    return jsonify(response=response)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        version = request.form['version']
        if version not in versions:
            return "nuh-uh", 400
    else:
        # default settings
        version = 'PC3131'

    # do something to load appropriate llamaindex files for the version of the chatbot


    return render_template("index.html", versions=versions, selected_version=version)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5601, debug=True)
