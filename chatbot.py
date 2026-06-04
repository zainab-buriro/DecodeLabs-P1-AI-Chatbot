# DecodeLabs - Project 1: Rule-Based Chatbot

print("🤖 Chatbot: Hello! I am the DecodeLabs AI assistant. You can chat with me.")
print("(Type 'exit' or 'bye' to close the chatbot)\n")

# 1. This loop keeps the chatbot running continuously
while True:
    # Taking input from the user and converting it to lowercase for easy matching
    user_input = input("You: ").lower().strip()

    # 2. Exit Command (If user wants to quit)
    if user_input == "exit" or user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a great day ahead. 🚀")
        break  # This will stop the loop and close the chatbot

    # 3. Greetings
    elif user_input == "hi" or user_input == "hello" or user_input == "hey":
        print("🤖 Chatbot: Hello! How can I help you today?")

    # 4. Asking how the bot is doing
    elif "how are you" in user_input or "how is it going" in user_input:
        print("🤖 Chatbot: I am doing great, thank you! How are you doing?")

    # 5. Asking about DecodeLabs
    elif "decodelabs" in user_input:
        print("🤖 Chatbot: DecodeLabs is an awesome place where we learn foundational AI concepts! 🧠")

    # 6. Asking about the project
    elif "project" in user_input or "task" in user_input:
        print("🤖 Chatbot: This is Project 1: A Rule-Based Chatbot built using control flow and logic.")

    # 7. Default Response (If the chatbot doesn't understand)
    else:
        print("🤖 Chatbot: I'm sorry, I did not understand that. Could you please rephrase?")