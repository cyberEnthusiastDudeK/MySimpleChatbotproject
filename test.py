import random

# Define a list of possible user greetings and chatbot responses
greetings = ["hello", "hi", "hey", "howdy", "hola"]
responses = ["Hello!", "Hi there!", "Hey!", "How can I assist you today?", "Hola!"]

# Define a function to generate chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive matching

    if user_input in greetings:
        return random.choice(responses)
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "I'm not sure how to respond to that."

# Define a list of common GST-related questions and corresponding responses
gst_questions = [
    "What is GST?",
    "How is GST calculated?",
    "What are the GST rates in India?",
    "How do I register for GST?",
    "When should I file my GST returns?",
    "Is GST applicable to my business?",
]

gst_responses = [
    "GST (Goods and Services Tax) is an indirect tax levied on the supply of goods and services in India.",
    "GST is calculated as a percentage of the value of the goods or services supplied. The formula is: GST Amount = (GST Rate / 100) * Value of Goods/Services.",
    "GST rates in India vary depending on the type of goods or services. It includes 5%, 12%, 18%, and 28% rates, as well as some items that are exempt from GST.",
    "You can register for GST through the GST portal by providing the necessary documents and information about your business.",
    "GST returns should be filed monthly, quarterly, or annually, depending on your business turnover and type.",
    "GST is generally applicable to most businesses in India, with some exceptions and exemptions based on turnover and the nature of the business.",
]

# Define a function to generate GST chatbot responses
def gst_advisory_response(user_input):
    user_input = user_input.lower()

    for question in gst_questions:
        if question.lower() in user_input:
            return random.choice(gst_responses)

    return "I'm sorry, I couldn't understand your question. Please ask a GST-related question, and I'll do my best to provide information."

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
        response = current_chatbot(user_input)
        print("Bot:", response)
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
