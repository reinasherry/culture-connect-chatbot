from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI(title="Culture Connect Chatbot")

#Input model
class UserInput(BaseModel):
    message: str

# Example cultural knowledge base
cultural_tips = {
    "food": "In many Arab families, refusing food can be seen as impolite. It's better to accept at least a small portion.",
    "silence": "In Japan, silence during a conversation can mean respect, while in the US it may feel uncomfortable.",
    "eye contact": "In Western cultures, eye contact shows confidence, but in some Asian cultures it may be seen as disrespectful.",
    "greeting": "In France, people often greet with cheek kisses, while in the US a handshake or hug is more common."
}

@app.get("/")
def home():
    return {"message": "Welcome to Culture Connect Chatbot! Send a POST request to /chat with your message."}

@app.post("/chat")
def chat(user_input: UserInput):
    text = user_input.message.lower()

    # Check if any keyword matches
    for keyword, tip in cultural_tips.items():
        if keyword in text:
            return {"response": tip}

    # Default response if no keyword is found
    return {"response": "I don't have cultural info on that yet. Try asking about food, silence, eye contact, or greeting."}

# This allows running with: python main.py
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)