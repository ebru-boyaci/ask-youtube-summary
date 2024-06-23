# YouTube Video Summary and Q&A App

This application utilizes the power of AI to provide summaries of YouTube videos and answer questions related to the content of these videos. It's built using Streamlit for the web interface, LangChain for processing and summarizing video transcripts, and OpenAI's GPT models for generating responses to user queries.

## Features

- **YouTube Video Transcription and Summary**: Automatically transcribe and summarize the content of a YouTube video.
- **Interactive Q&A**: Ask questions and get answers based on the video's summary.
- **Streamlit Web Interface**: Easy-to-use interface for interacting with the application.

## Installation

To run this application, you will need Python 3.8 or later. Follow these steps to set up the environment:

1. Clone the repository to your local machine.
2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:
   - **Windows**:
     ```sh
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```sh
     source venv/bin/activate
     ```
4. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To run the application, use the following command:

```sh
streamlit run yt_summary.py
```


## How to Use

1. Enter the URL of the YouTube video you want to summarize.
2. Click the "Submit and Get Summary" button to view the video's transcript and summary.
3. Ask questions related to the video content in the provided input field to get answers based on the summary.

## Configuration

Before using the application, you need to set the `OPEN_API_KEY` variable in the script to your OpenAI API key. This key is required for accessing the GPT model for generating summaries and answering questions. 👋🏻👋🏻👋🏻👋🏻
