# Art Registry with IPFS

In this activity, you’ll update the art registry dApp so that it uses decentralized storage.

## Instructions

The instructions for this activity are divided into the following subsections:

1. Deploy the Contract

2. Prepare the environment

3. Build the dApp

### Deploy the Contract

1. In the Remix IDE, create a new file, and then copy the code from the provided `ArtRegistry.sol` to the new file. Spend a few moments reviewing the code.

2. Launch a Quickstart blockchain with Ganache, and then use MetaMask and the Remix IDE to compile and deploy the `ArtRegistry` contract.

    > **Hint** An earlier module has a detailed video about deploying contracts with Ganache, MetaMask, and Remix that you can reference for this contract.

### Prepare the environment

Copy the provided `SAMPLE.env` file to a new file named `.env`, and then add the missing data
to the environment variables.

### Build the dApp

1. Open `app.py` in the `Unsolved` folder.

2. In `app.py`, in the “Register New Artwork” section, use the `pin_artwork` helper function to pin the file to IPFS.

3. In `app.py`, in the “Appraise Art” section, use the `pin_appraisal_report` helper function to pin an appraisal report to IPFS. Then copy and save the URI to this report for later use as the smart contract’s `reportURI` parameter.

4. Run the application by using `streamlit run app.py`. Test the functionality of the dApp to make sure that it works as expected.
