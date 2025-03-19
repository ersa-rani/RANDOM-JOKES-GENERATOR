import streamlit as st
import requests

def get_random_joke():
    """Fetch a random joke from the FastAPI backend."""
    try:
        response = requests.get("https://joke-api-nine.vercel.app/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"**{joke_data['setup']}**\n\n*{joke_data['punchline']}*"
        else:
            return "⚠️ Failed to fetch a joke. Please try again later!"
    except requests.exceptions.RequestException as e:
        st.error(f"���️ Failed to connect to the API: {e}")
        return "��� Why did the programmer quit his job?\n\nBecause he didn't get arrays!"
    

def main():
    st.set_page_config(page_title="Random Joke Generator", page_icon="😂", layout="centered")
    
    st.title("🎭 Random Joke Generator")
    st.write("Click the button below to get a random joke and brighten your day! 😆")
    
    with st.container():
        if st.button("Tell me a joke! 😂"):
            joke = get_random_joke()
            st.success(joke)
    
    st.divider()
    
    st.markdown(
        """
        <div style='text-align:center; font-size:14px;'>
            <p>Jokes from <a href='http://127.0.0.1:8000/random_joke' target='_blank'>FastAPI Backend</a> 🤖</p>
            <p>Developed by <a href='https://github.com/ersa-rani' target='_blank'>Ersa Rani</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
