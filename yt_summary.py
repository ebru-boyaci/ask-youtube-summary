import streamlit as st
from langchain.document_loaders import YoutubeLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import TokenTextSplitter
from htmlTemplates import css, bot_template, user_template


# OpenAI API Key
openai_api_key = "OPEN_API_KEY"
llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-3.5-turbo-16k", temperature=0.3)

# Summarize the YouTube video
def get_youtube_summary(url):
    loader = YoutubeLoader.from_youtube_url(url, language="en")
    transcript = loader.load()
    splitter = TokenTextSplitter(model_name="gpt-3.5-turbo-16k", chunk_size=10000, chunk_overlap=100)
    chunks = splitter.split_documents(transcript)
    summarize_chain = load_summarize_chain(llm=llm, chain_type="refine", verbose=True)
    summary = summarize_chain.run(chunks)
    return summary

# Ask a question and get a response
def ask_question(question, summary):
    if not isinstance(question, str) or not isinstance(summary, str):
        raise ValueError("Both question and summary need to be strings.")
    combined_text = question + "\n\n" + summary
    response = llm.generate(combined_text)
    return response

# User input and bot response
def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


# Show chat history
def show_chat_history():
    for chat in st.session_state.chat_history:
        st.text(chat)

# Main function
def main():
    st.title("YouTube Video Summary and Q&A App")

    youtube_url = st.text_input("Enter the YouTube URL")
    submit_button = st.button("Submit and Get Summary")

    if submit_button and youtube_url:
        with st.spinner('Loading the video transcript and summary...'):
            transcript = YoutubeLoader.from_youtube_url(youtube_url, language="en").load()
            st.session_state.transcript = transcript
            st.subheader("Video Transcript:")
            st.text_area("Transcript", transcript, height=150)

            summary = get_youtube_summary(youtube_url)
            st.session_state.summary = summary
            st.subheader("Video Summary:")
            st.text_area("Summary", summary, height=100)

    # Chat with the bot
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with AxonFlow ChatBot 🤖")
    user_question = st.text_input("Ask a question about your transcript:")
    if user_question:
        handle_userinput(user_question)

if __name__ == "__main__":
    main()
