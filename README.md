# Telegram-Bot

What is a Telegram Bot?
Bots are third-party applications that run inside Telegram. Users can interact with bots by sending them messages, commands and inline requests. You control your bots using HTTPS requests to Telegram Bot API.

Telegram Bots are special accounts that do not require an additional phone number to set up. These accounts serve as an interface for code running somewhere on your server.

# Registering a telegram Bot

![image](https://user-images.githubusercontent.com/44311116/118290690-553ccd00-b4f4-11eb-882f-5e55fb7dd675.png)

Use the BotFather for registering a new Bot

# Setting up the Project
1. Setup a Python Virtual Environment
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them.

Create a Project Folder.
Run following command to create a new virtual environment inside your project folder:

python -m venv myvenv
After running above command, a folder named myvenv will get created in your project folder.

Activate the virtual environment by running following command:
For ubuntu and mac users:
  source myvenv/bin/activate
For windows users:
  myvenv\Scripts\activate
  
# Generate Public URL for Webhook using ngrok.io

ngrok is a free tool that allows us to tunnel from a public URL to our application running locally.

Download ngrok.
Unzip it.
Run ngrok from command line (from the location where executable is stored)
./ngrok http 8443
Copy the HTTPS Forwarding URL

# How to get the client.json file from dialogflow API?
  1. Login into dialogflow console¶
  2. Create a new agent or import a pre-built agent
  3. From settings page of agent, open the service account of your project in Google Cloud Console
  4. Create a new service account for your project. Download private key for the service account in a JSON file
  5. Install Python Client for Dialogflow

# How to create a Conversational Bot?

  import dialogflow_v2 as dialogflow
  dialogflow_session_client = dialogflow.SessionsClient()
  PROJECT_ID = "Put the Project-ID here"
  
  This code segment links your dialogflow client to you application
  Enable small talks in your API console to enable the small talks
  We used gnewsclient for getting the news links for required domain
