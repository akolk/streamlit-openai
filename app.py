import streamlit as st
import streamlit_openai

if "chat" not in st.session_state:

    kadasterserver = streamlit_openai.RemoteMCP(
        server_label="kadasterserver",
        server_url="https://labs.test.kadaster.nl/mcp/server",
    )

    cbsserver = streamlit_openai.RemoteMCP(
        server_label="cbsserver",
        server_url="https://labs.test.kadaster.nl/mcp/cbs",
    )
    
    thinkingserver = streamlit_openai.RemoteMCP(
        server_label="thinkingserver",
        server_url="https://labs.test.kadaster.nl/mcp/sequential-thinking",
    )
      
    st.session_state.chat = streamlit_openai.Chat(
        instructions="Je bent kadaster assistent en je probeert altijd vragen met je bschikbare tools te beantwoorden in het Nederlands.",
        info_message="Deel geen persoonlijke informatie en AI kan het soms mis hebben.",
        placeholder="Stel je vraag hier ....",
        welcome_message="Hallo ik ben een AI assistent die kan helpen bij verschillende analyses en vragen over je leef omgeving.",
        mcps=[kadasterserver, cbsserver, thinkingserver],
        allow_image_generation=False,
        model="o3",             # Select a reasoning model
        allow_web_search=False, # Disable web search
    )

st.session_state.chat.run()
