from transformers import pipeline, Conversation

# Load the GPT-2 model for text generation
chatbot = pipeline("text-generation", model="gpt2")

def get_response(user_input, conversation_history=None):
    if conversation_history:
        conversation_history.append(user_input)
        response = chatbot(conversation_history)
    else:
        response = chatbot(user_input)
    return response[0]['generated_text']

def chat():
    print("ChatGPT: Hello! I'm ChatGPT. How can I assist you today?")
    conversation_history = Conversation()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatGPT: Goodbye! Have a great day.")
            break
        
        response = get_response(user_input, conversation_history)
        
        print("ChatGPT:", response)
        conversation_history.append_user_input(user_input)
        conversation_history.append_generated_output(response)

if __name__ == "__main__":
    chat()

