# LangChain-Streamlit Template

This repo serves as a template for how to deploy a [LangGraph](https://langchain-ai.github.io/langgraph/) agent on Streamlit.

This repo contains an `main.py` file which has a template for a chatbot implementation.

## Adding your chain

To add your chain, you need to change the `load_chain` function in `main.py`.
Depending on the type of your chain, you may also need to change the inputs/outputs that occur later on.

## Deploy on Streamlit

This is easily deployable on the Streamlit platform.
Note that when setting up your Streamlit app you should make sure to add `OPENAI_API_KEY` as a secret environment variable.

## Setting up LangSmith

To quickly spot issues and improve the performance of your LangGraph projects, sign up for [LangSmith](https://docs.smith.langchain.com/). LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com/).
