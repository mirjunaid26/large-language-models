import random

# Sample Shakespearean data
shakespeare_data = [
    "To be, or not to be: that is the question",
    "All the world's a stage, and all the men and women merely players",
    "To thine own self be true",
    "What's in a name? That which we call a rose by any other name would smell as sweet",
    "To sleep, perchance to dream",
    "Out, out, brief candle! Life's but a walking shadow, a poor player that struts and frets his hour upon the stage",
    "O Romeo, Romeo! wherefore art thou Romeo?",
    "Parting is such sweet sorrow",
    "All that glisters is not gold",
    "Double, double toil and trouble; Fire burn and caldron bubble",
    "Brevity is the soul of wit"
]

def shakespeare_chatbot():
    print("Shakespearean Chatbot: Hark! What dost thou seeketh?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Shakespearean Chatbot: Fare thee well, good sir/madam!")
            break
        
        response = random.choice(shakespeare_data)
        print("Shakespearean Chatbot:", response)

if __name__ == "__main__":
    shakespeare_chatbot()

