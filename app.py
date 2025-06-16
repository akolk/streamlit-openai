import streamlit as st
import streamlit_openai

if "chat" not in st.session_state:
    st.session_state.chat = streamlit_openai.Chat()
    st.session_state.chat._tools.append({
                    "type": "mcp",
                    "server_label": "KadasterServer",
                    "server_url": "https://labs.test.kadaster.nl/mcp/server",
                    "require_approval": "never"
                })
    st.session_state.chat._tools.append({
                    "type": "mcp",
                    "server_label": "CBSServer",
                    "server_url": "https://labs.test.kadaster.nl/mcp/cbs",
                    "require_approval": "never"
                })
    st.session_state.chat._tools.append({
                    "type": "mcp",
                    "server_label": "ThinkingServer",
                    "server_url": "https://labs.test.kadaster.nl/mcp/sequential-thinking",
                    "require_approval": "never"
                })
    #kadasterserver = streamlit_openai.RemoteMCP(
    #    server_label="kadasterserver",
    #    server_url="https://labs.test.kadaster.nl/mcp/server",
    #)

    #st.session_state.chat = streamlit_openai.Chat(
    #    mcps=[kadasterserver]
    #)
    
st.session_state.chat.run()
