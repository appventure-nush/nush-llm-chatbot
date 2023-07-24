# nush-llm-chatbot

## HOWTO

Running of the prototype webpage requires the setup of a python environment and the construction of the
vector database.

Step 0: API KEY
Create a file called "apikey" under /llamaindex directory. The only contents in the file should be
the openai api key. The apikey is also present under the teams development folder in the same /llamaindex directory, 
copying the file over also works.

Step 1: Setup python environment
Environment package managers like pipenv or anaconda are recommended, these environment
managers ensure that isolated python workspaces are created and packages installed do not interfere with the packages
of another environment. There are many tutorials online on how to download and setup a package environment.

The requirements.txt file required to download relevant packages has already been provided. Navigate
to the root directory and run this command (ensure the correct python environment is active):
```
pip install -r requirements.txt
```
Now just have to wait for the packages to complete downloading.

Step 2: Setup vector database
This step only has to be done once, and caches all the vectors in the folder /llamaindex/storage/ for the model to
refer to. There are two options, one is to run the file and the other is to copy the already created file from teams.

Simply run /llamaindex/vector_indices.py via the editor or through the command line as shown:
```
python llamaindex/vector_indices.py
```
This should create a storage folder if it does not already exist.
Alternatively, the file /llamaindex/storage/ from Teams can be copied over and placed in the same directory locally.

Step 3:
Run app.py either through the editor or through command line console:
```
python -m frontend.app
```

The output should display something like:
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5601
 * Running on http://172.20.10.10:5601
Press CTRL+C to quit
```
The IP address that the server is running on might vary, but opening the displayed address in a web browser will
open up the app.
Once the webpage is opened, the first time executing the application might be met with some buffer period as the 
huggingface model might have to be downloaded and initialised for the first time.



## TODO
- [x] convert pdf files to document
- [ ] setup gitignore for OpenAI API keys
- [x] implement basic llamaindex following tutorial https://gpt-index.readthedocs.io/en/latest/guides/tutorials/building_a_chatbot.html 
- [x] test llamaindex with converted html files
- [x] frontend development

