# ChatBot using GPT-2

## Description
This project implements a ChatBot using the GPT-2 language model. The ChatBot engages in interactive conversations with users, providing responses based on the input text. It utilizes the GPT-2 model for language generation and the Hugging Face `transformers` library for model loading, tokenization, and generation.

The ChatBot uses the GPT-2 model to generate responses by conditioning on the user's input. It employs the AutoModelForCausalLM and AutoTokenizer classes from the `transformers` library to load the pre-trained GPT-2 model and tokenizer.

To prevent the ChatBot from providing repetitive responses, the code keeps track of previous responses and checks for duplicates before displaying a response. This helps ensure a more engaging and diverse conversation experience.

## Requirements
- Python 3.x
- transformers library (`pip install transformers`)

## Usage
1. Install the required dependencies by running the following command: pip install transformers
2. Run the provided script to start the ChatBot: python chatbot.py
3. Enter your input text to start a conversation with the ChatBot.

4. The ChatBot will generate and display a response based on your input.

5. Continue the conversation by entering additional input text.

6. To end the conversation, enter "bye".

## Example Conversation
User: Hi, how are you doing?
ChatBot: I'm doing well, thank you. How about you?

User: I'm good too. What have you been up to?
ChatBot: I've been learning and conversing with users like you. It's quite exciting!

User: That's great. Do you have any hobbies?
ChatBot: Although I don't have physical hobbies, I enjoy engaging in meaningful conversations and providing assistance.

User: Interesting. Can you tell me a joke?
ChatBot: Sure! Why don't scientists trust atoms? Because they make up everything!

User: Haha, that's a good one. Thanks!
ChatBot: You're welcome! If you have any more questions or need further assistance, feel free to ask.

User: Bye
ChatBot: Goodbye! Take care and have a great day!


Feel free to experiment with different inputs and have engaging conversations with the ChatBot!

## Acknowledgments
This project utilizes the GPT-2 model and the `transformers` library provided by Hugging Face. Special thanks to the Hugging Face team for their contributions to the NLP community.

## License
This project is licensed under the [MIT License](LICENSE).
