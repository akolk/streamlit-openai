import streamlit as st
import streamlit_openai
import os

if "chat" not in st.session_state:

    kadasterserver = streamlit_openai.RemoteMCP(
        server_label="kadasterserver",
        server_url="https://labs.test.kadaster.nl/mcp/server/sse",
        require_approval="never"
    )

    kkgserver = streamlit_openai.RemoteMCP(
        server_label="kkgserver",
        server_url="https://labs.test.kadaster.nl/mcp/kkg",
    )
    
    deepwiki = streamlit_openai.RemoteMCP(
        server_label="deepwiki",
        server_url="https://mcp.deepwiki.com/mcp",
    )
    
    st.session_state.chat = streamlit_openai.Chat(
        instructions="Je bent kadaster assistent en je probeert altijd vragen met je bschikbare tools te beantwoorden in het Nederlands.",
        info_message="Deel geen persoonlijke informatie en AI kan het soms mis hebben.",
        placeholder="Stel je vraag hier ....",
        welcome_message="Hallo ik ben een AI assistent die kan helpen bij verschillende analyses en vragen over je leef omgeving.",
        example_messages=[
            "Wat is de geschatte waarde van mijn huis?",
            "Wat is de verwachte zonne opwek voor mijn huis?",
            "Heeft dit adres een gas aansluiting?",
            "Wat is de gemiddelde woz waarde voor de gemeente?",
        ],
        mcps=[kadasterserver, deepwiki, kkgserver],
        allow_image_generation=True,
        model=os.getenv("MODEL", "o3"),             # Select a reasoning model
        allow_web_search=False, # Disable web search
    )

st.session_state.chat.run()
