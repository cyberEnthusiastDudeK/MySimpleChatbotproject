import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# Function to determine sentiment based on user input
def get_sentiment_score(user_input):
    score = sia.polarity_scores(user_input)
    return score['compound']  # Using the compound score for overall sentiment


# ... (existing code)

# Function to train a basic model (you can replace this with a more sophisticated model)
def train_basic_model():
    # Sample data for training - replace this with your actual data
    conversations = [
        {"input": "What is GST?", "output": "GST is an indirect tax."},
        {"input": "How do I register for GST?", "output": "You can register through the GST portal."},
        # Add more conversational data here...
    ]

    return conversations


# ... (existing code)

# Main chat loop
print("Chatbot: Hello! Type 'goodbye' to exit. Type 'gst' to switch to GST Advisory Bot.")
current_chatbot = chatbot_response  # Start with the general chatbot
while True:
    user_input = input("You: ")

    if user_input.lower() == "goodbye":
        print("Chatbot: Goodbye!")
        break
    elif user_input.lower() == "gst":
        print("Switching to GST Advisory Bot.")
        current_chatbot = gst_advisory_response
        print("GST Advisory Bot: Hello! How can I help you with GST today? Type 'exit' to switch back.")
    elif user_input.lower() == "exit":
        print("Switching back to the general chatbot.")
        current_chatbot = chatbot_response
        print("Chatbot: Hello! Type 'goodbye' to exit. Type 'gst' to switch to GST Advisory Bot.")
    else:
        # Get sentiment score
        sentiment_score = get_sentiment_score(user_input)

        if sentiment_score > 0.5:
            # Generate a positive response
            response = "That's great to hear! How can I assist you further?"
        elif sentiment_score < -0.5:
            # Generate a negative response
            response = "I'm sorry to hear that. Let me know how I can help."
        else:
            # Generate a neutral response using the current chatbot function
            response = current_chatbot(user_input)

        print("Bot:", response)
