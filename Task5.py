print("🤖 ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").strip().lower()

    if user == "hello":
        print("Bot: Hello! Welcome!")

    elif user == "how are you":
        print("Bot: I'm fine. Thanks for asking!")

    elif user == "your name":
        print("Bot: My name is ChatBot.")

    elif user == "help":
        print("Bot: You can say 'hello', 'how are you', 'your name', 'thank you', or 'bye'.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")