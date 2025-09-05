Culture Connect Chatbot 🌍

A FastAPI-powered web application that provides cultural communication tips for cross-cultural interactions, covering greetings, eye contact, silence, and food customs across different regions.

Features:

Interactive chat interface with visual suggestions

Cultural knowledge base covering four key areas:

Food customs and etiquette

Eye contact norms across cultures

Silence in conversation

Greeting traditions

Responsive design with modern UI

Real-time typing indicators


You must first have these prerequisites:

Python 3.7+
FastAPI
Uvicorn 
Installation:

Clone or download the project files
Install the required dependencies:
pip install fastapi uvicorn
Run the application:
python main.py
Open index.html in your web browser or navigate to http://localhost:8001
Usage
-Type your question about cultural differences in the chat input
-Click on one of the suggestion buttons for quick queries
-The bot will respond with culturally relevant information

Example questions:

"What should I know about food customs?"
"How important is eye contact in different cultures?"
"Tell me about greeting traditions"

API Reference:

POST /chat:

Sends a message to the chatbot and receives a cultural tip response.
Request Body:
json
{
  "message": "string"
}
Response:
json
{
  "response": "string"
}
Project Structure:

├── index.html          
├── main.py            
└── README.md          
