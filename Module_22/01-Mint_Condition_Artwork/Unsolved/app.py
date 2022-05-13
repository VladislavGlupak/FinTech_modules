import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    # @TODO: YOUR CODE HERE!

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    # @TODO: YOUR CODE HERE!

    return contract


contract = load_contract()


################################################################################
# Register New Artwork
################################################################################
st.title("Register New Artwork")

accounts = w3.eth.accounts

# Use a streamlit component to get the address of the artwork owner from the user
# @TODO: YOUR CODE HERE!

# Use a streamlit component to get the artwork's URI
# HINT: You can just enter this as text for now.
# @TODO: YOUR CODE HERE!

if st.button("Register Artwork"):

    # Use the contract to send a transaction to the registerArtwork function
    tx_hash =  # @TODO: YOUR CODE HERE!

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
st.markdown("---")

################################################################################
# Display a Token
################################################################################
st.markdown("## Display an Art Token")

selected_address = st.selectbox("Select Account", options=accounts)

tokens = contract.functions.balanceOf(selected_address).call()

st.write(f"This address owns {tokens} tokens")

token_id = st.selectbox("Artwork Tokens", list(range(tokens)))

if st.button("Display"):

    # Use the contract's `ownerOf` function to get the art token owner
    owner =  # @TODO: YOUR CODE HERE!

    st.write(f"The token is registered to {owner}")

    # Use the contract's `tokenURI` function to get the art token's URI
    token_uri =  # @TODO: YOUR CODE HERE!

    st.write(f"The tokenURI is {token_uri}")
    st.image(token_uri)
