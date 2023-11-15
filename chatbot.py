import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = 'keys'

def generate_response(prompt, chat_history):
    input_text = f"{chat_history}\nUser: {prompt}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=150,
        temperature=0.7,
    )
    
    
    ai_response = response.choices[0].text.strip()
    
    updated_chat_history = f"{chat_history}User: {prompt}\nAI: {ai_response}\n"

    return ai_response, updated_chat_history

def main():
    st.title("Chatbot")
    chat_history = ""

    # Streamlit text area for user input
    user_input = st.text_area("Write below")

    if st.button("Send"):
        ai_response, chat_history = generate_response(user_input, chat_history)
        # Display AI response
        st.text_area("AI Response", value=ai_response, height=100)

if __name__ == "__main__":
    main()
