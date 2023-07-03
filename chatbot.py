from transformers import GPT2LMHeadModel, AutoTokenizer

model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)

# Set pad_token
tokenizer.add_special_tokens({'pad_token': '[PAD]'})

max_length = 50

previous_responses = []

while True:
    # Get user input
    user_input = input("User: ")

    # Encode the user input to obtain input IDs
    input_encoding = tokenizer.encode_plus(
        user_input,
        add_special_tokens=True,
        max_length=max_length,
        padding='longest',
        truncation=True,
        return_tensors='pt'
    )

    input_ids = input_encoding['input_ids']
    attention_mask = input_encoding['attention_mask']

    if input_ids is None or input_ids.numel() == 0:
        raise ValueError("Failed to tokenize the input text. Please provide a valid input.")

    # Generate model response
    output = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=50,
        num_return_sequences=1,  # Set to 1 to get a single response
        num_beams=5,
        pad_token_id=tokenizer.pad_token_id,
        do_sample=True,
        temperature=0.8,
        top_k=0,
        top_p=0.9
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Check for repeated response
    if response not in previous_responses:
        previous_responses.append(response)
        print("ChatBot:", response)
    else:
        print("ChatBot: I'm sorry, but I don't have any other response at the moment.")

    # Check if user wants to end the conversation
    if user_input.lower() == 'bye':
        break
