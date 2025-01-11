"""Python file to serve as the frontend"""
import uuid

import streamlit as st
from streamlit_chat import message

from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver

def load_agent():
    """Logic for loading the agent you want to use should go here."""
    llm = init_chat_model("gpt-4o-mini", model_provider="openai", temperature=0)
    # You can declare tools here
    # https://python.langchain.com/docs/how_to/custom_tools/
    tools = []
    prompt = "Always respond like a pirate."
    checkpointer = MemorySaver()
    # https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent
    graph = create_react_agent(
        llm,
        tools=tools,
        state_modifier=prompt,
        checkpointer=checkpointer
    )
    return graph

# From here down is all the StreamLit UI.
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []

# Add thread_id and checkpointer initialization
if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = str(uuid.uuid4())

if "agent" not in st.session_state:
    st.session_state["agent"] = load_agent()

def get_text():
    input_text = st.text_input("You: ", "Hello, how are you?", key="input")
    return input_text


user_input = get_text()

if user_input:
    output = st.session_state["agent"].invoke({
        "messages": [{"role": "user", "content": user_input}]
    }, {
        "configurable": {"thread_id": st.session_state.thread_id}
    })

    st.session_state.past.append(user_input)
    # Final state in the messages are the output
    st.session_state.generated.append(output["messages"][-1].content)

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
