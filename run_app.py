# import streamlit as st
# from transformers import pipeline


# summarizer = pipeline('summarization')

# st.set_page_config(page_title="Summarizer", page_icon=':robot:')

# # st.image('./images/Logo.jpg', width=180)

# st.title("Text summarizer")

# article = st.text_area("Input Text for summarization")

# submit_button = st.button('Generate summary')

# if submit_button:
#     response = summarizer(article, max_length=130, min_length=30, do_sample=False)
#     # st.write(response.text)
#     st.write(response[0]['summary_text'])
#     # pass


import streamlit as st
from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline('summarization')

st.set_page_config(page_title="Summarizer", page_icon='🤖')
st.title("Text Summarizer")

# Input text
article = st.text_area("Input Text for Summarization", height=300)

# Submit button
submit_button = st.button('Generate Summary')

# Generate and show summary
if submit_button:
    if article.strip():
        response = summarizer(article, max_length=130, min_length=30, do_sample=False)
        st.subheader("Summary")
        st.write(response[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
