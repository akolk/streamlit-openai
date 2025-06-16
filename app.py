import streamlit as st
import streamlit_openai

if "chat" not in st.session_state:
    kadasterserver = streamlit_openai.RemoteMCP(
        server_label="kadasterserver",
        server_url="https://labs.test.kadaster.nl/mcp/server",
    )

    st.session_state.chat = streamlit_openai.Chat(
        mcps=[kadasterserver]
    )
    
st.session_state.chat.run()
