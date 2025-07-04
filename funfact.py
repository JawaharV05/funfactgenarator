import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Fun Fact Generator", page_icon="💡")
st.title("💡 Fun Fact Generator")
st.write("Enter a topic and get an interesting, lesser-known fact!")

topic = st.text_input("🔎 Enter a topic (e.g., space, music, food)")

if topic.strip() == "":
    st.info("Please enter a topic above to generate a fun fact.")
elif st.button("Generate Fun Fact"):
    with st.spinner("Generating a fun fact..."):
        try:
            prompt = f"Give me one interesting and lesser-known fun fact about {topic} in one or two sentences."

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=100
            )

            fact = response.choices[0].message.content.strip()

            st.success("Here's your fun fact! 🤯")
            st.markdown(f"""
            <div style='
                background-color: #f9f9f9;
                padding: 15px;
                border-left: 5px solid #f39c12;
                font-size: 20px;
                font-style: italic;
                margin-top: 10px;
            '>
                “{fact}”
            </div>
            """, unsafe_allow_html=True)

            st.code(fact, language='text')
        except Exception as e:
            st.error(f"Error: {e}")
