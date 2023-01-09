# LangChain-Streamlit Template

This repo serves as a template for how to deploy a LangChain on Streamlit.

This repo contains an `main.py` file which has a template for a chatbot implementation.

## Adding your chain
To add your chain, you need to change the `load_chain` function in `main.py`.
Depending on the type of your chain, you may also need to change the inputs/outputs that occur later on.

## Deploy on Streamlit

This is easily deployable on the Streamlit platform.
Note that when setting up your StreamLit app you should make sure to add `OPENAI_API_KEY` as a secret environment variable.
