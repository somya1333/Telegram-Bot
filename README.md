# Telegram-Bot



How to get the client.json file from dialogflow API?
  1. Login into dialogflow console¶
  2. Create a new agent or import a pre-built agent
  3. From settings page of agent, open the service account of your project in Google Cloud Console
  4. Create a new service account for your project. Download private key for the service account in a JSON file
  5. Install Python Client for Dialogflow

How to create a Conversational Bot?

  import dialogflow_v2 as dialogflow
  dialogflow_session_client = dialogflow.SessionsClient()
  PROJECT_ID = "Put the Project-ID here"
  
  This code segment links your dialogflow client to you application
  Enable small talks in your API console to enable the small talks
  We used gnewsclient for getting the news links for required domain
