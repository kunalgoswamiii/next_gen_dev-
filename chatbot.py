# Function to process user input and generate responses
def chatbot_response(user_input):
    # Convert input to lowercase for easier comparison
    user_input = user_input.lower()

    # Use if-else statements to determine the response based on user input
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help you!"
    elif "your name" in user_input or "who are you" in user_input:
        return "I am a simple chatbot designed to help with basic queries."
    elif "what can you do" in user_input or "help" in user_input:
        return ("I can answer basic questions and assist with general information. "
                "Try asking me about the weather, news, or anything you like.")
    elif "weather" in user_input:
        return "I can't provide real-time weather updates, but you can check weather websites or apps."
    elif "goodbye" in user_input or "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"


# Main function to run the chatbot
def main():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")

    # Run an infinite loop to keep the conversation going
    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user wants to exit the conversation
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a nice day!")
            break

        # Get the chatbot's response
        response = chatbot_response(user_input)
        print("Chatbot:", response)


# Entry point of the program
if __name__ == "__main__":
    main()
