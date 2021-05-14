# Telegram-Bot

What is a Telegram Bot?
Bots are third-party applications that run inside Telegram. Users can interact with bots by sending them messages, commands and inline requests. You control your bots using HTTPS requests to Telegram Bot API.

Telegram Bots are special accounts that do not require an additional phone number to set up. These accounts serve as an interface for code running somewhere on your server.

# Registering a telegram Bot

Use the BotFather for registering a new Bot
![image](https://user-images.githubusercontent.com/44311116/118290690-553ccd00-b4f4-11eb-882f-5e55fb7dd675.png)

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
