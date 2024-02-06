import streamlit as st
import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["api_key"]
# user_input = st.text_input("그리고 싶은 그림은?")
# st.button("눌러")
st.title("나는 이미지 생성기 입니다.")

with st.form("form"):
    user_input = st.text_input("그리고 싶은 그림은?")
    size = st.selectbox("size", ['1024x1024','512x512','256x256'])
    submit = st.form_submit_button("submit")


if submit and user_input:

    gpt_prompt = [
        {
            "role": "system",
            "content": "Imagine the detail appeareance of the input.Response it shortly around 15 words",
        }
    ]

    gpt_prompt.append({"role": "user", "content": user_input})


    client = OpenAI()
    with st.spinner("waiting for ChatGPT ..."):
        gpt_response = client.chat.completions.create(
            model="gpt-4",
            messages=gpt_prompt,
        )
        dalle_prompt = gpt_response.choices[0].message.content
        st.write("dalle-e prompt:", dalle_prompt)\
        

    with st.spinner("waiting for ChatGPT ..."):
        dalle_response = client.images.generate(
                model='dall-e-3',
                prompt = dalle_prompt,
                size = '1024x1024'
        )

    st.image(dalle_response.data[0].url)