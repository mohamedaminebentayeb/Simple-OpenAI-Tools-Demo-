import streamlit as st
import openai
openai.organization = "org-cek3Dtba4Wvd4Ce0wXOgU8Vs"

openai.api_key = "your_api_key"
def count_words(sentence):
    words = sentence.split()
    return len(words)


st.set_page_config(page_title="OpenAI Tools demonstration", layout="wide")

st.sidebar.title("Options")
option = st.sidebar.selectbox("Select an option", ["Generate Text","Summarize", "Translate", "Analyze Sentiment" ])

st.title("OpenAI Tools demonstration")

text = st.text_area("Enter the text:")

if option == "Translate":
    target_language = st.selectbox("Select the target language", ["French", "Spanish", "German"])
if option == "Generate Text":
    textlen = st.text_area("Enter the text lenght:")

if st.button("Perform Action"):
    result = ""
    if option == "Generate Text":
        parameters = {
                "engine": "text-davinci-003",
                "prompt": 'Generate a text  with {} word about : "{}"'.format(textlen,text),
                "max_tokens":1000,  # Adjust the number of tokens for desired translation length
                "temperature": 0.5,  # Adjust the temperature for controlling randomness
                "top_p": 1.0,  # Adjust the top-p value for diversity in output
                "frequency_penalty": 0.0,  # Adjust the frequency penalty for diversity in output
                "presence_penalty": 0.0  # Adjust the presence penalty for diversity in output
            }

        response = openai.Completion.create(**parameters)
        result = response.choices[0].text.strip()

    if option == "Summarize":
        word_count = int(count_words(text)*0.6)
        parameters = {
                 "engine": "text-davinci-003",
                 "prompt": 'resume the following text : "{}"'.format(text),
                "max_tokens": word_count,  # Adjust the number of tokens for desired translation length
                "temperature": 0.5,  # Adjust the temperature for controlling randomness
                "top_p": 1.0,  # Adjust the top-p value for diversity in output
                "frequency_penalty": 0.0,  # Adjust the frequency penalty for diversity in output
                "presence_penalty": 0.0  # Adjust the presence penalty for diversity in output
            }

        response = openai.Completion.create(**parameters)
        result = response.choices[0].text.strip()
        

    elif option == "Translate":

        parameters = {
                "engine": "text-davinci-003",
                "prompt": 'Traduit le text suivant mot par mot  "{}" : "{}"'.format(target_language, text),
                "max_tokens": 1000,  # Adjust the number of tokens for desired translation length
                "temperature": 0.5,  # Adjust the temperature for controlling randomness
                "top_p": 1.0,  # Adjust the top-p value for diversity in output
                "frequency_penalty": 0.0,  # Adjust the frequency penalty for diversity in output
                "presence_penalty": 0.0  # Adjust the presence penalty for diversity in output
            }


        response = openai.Completion.create(**parameters)
        result = response.choices[0].text.strip()
        

    elif option == "Analyze Sentiment":
        # Call the OpenAI API for sentiment analysis
        parameters = {
                "engine": "text-davinci-003",
        "prompt": 'detect  my feeling "{}"'.format(text),
    "max_tokens": 1000,  # Adjust the number of tokens for desired translation length
    "temperature": 0.5,  # Adjust the temperature for controlling randomness
    "top_p": 1.0,  # Adjust the top-p value for diversity in output
    "frequency_penalty": 0.0,  # Adjust the frequency penalty for diversity in output
    "presence_penalty": 0.0  # Adjust the presence penalty for diversity in output
        }

        response = openai.Completion.create(**parameters)
        result = response.choices[0].text.strip()
        

    # Display the result
    st.text_area("Result:", value=result, height=200)

# Run the app
if __name__ == "__main__":
    st.set_option("deprecation.showPyplotGlobalUse", False)
