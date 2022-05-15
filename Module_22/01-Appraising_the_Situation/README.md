# Activity: Appraising the Situation

In this activity, you’ll create a dApp for the artwork registry contract.

## Instructions

The instructions for this activity are divided into the following sections:

1. Deploy the Contract

2. Prepare the Environment File

3. Build the dApp

### Deploy the Contract

1. In the Remix IDE, create a new file, and then copy the code from the provided `ArtRegistry.sol` to the new file. Spend a few moments reviewing the code.

2. Launch a Quickstart blockchain with Ganache, and then use MetaMask and the Remix IDE to compile and deploy the `ArtRegistry` contract.

    > **Hint** An earlier module has a detailed video about deploying contracts with Ganache, MetaMask, and Remix that you can reference for this contract.

### Prepare the Environment File

Copy the provided `SAMPLE.env` file to a new file named `.env`, and then add the missing data
to the environment variables.

> **Hint** You can find the value for `WEB3_PROVIDER_URI` in the RPC Server field in Ganache. For the `SMART_CONTRACT_ADDRESS` value, use the address of the deployed contract in the Remix IDE. You can find it in the Deployed Contracts section.

### Build the dApp

1. Open `app.py` in the `Unsolved` folder.

2. In `app.py`, in the “Register New Artwork” section, complete the following substeps:

    * Define new Streamlit components to get the following data from the user:

        * The name of the artwork

        * The name of the artist

        * The initial appraisal value

        * The URI of the artwork

    * Create a button named “Register Artwork” that uses the contract's `registerArtwork` function to register the data that you get from the Streamlit components.

        > **Hint** Some of the function parameters in the `ArtRegistry` smart contract are defined as specific types. Because you use the Web3.py library to call these functions from your Python code, you need to make sure that you pass them the right types of data. For example, the `registerArtwork` function in the smart contract has an `initialAppraisalValue` parameter of type `uint256`. So before using Web3.py to call `registerArtwork`, you need to use the Python `int` function to convert the string from the Streamlit component to an integer.

    * Display the transaction receipt on the webpage.

3. In `app.py`, in the “Appraise Art” section, complete the following substeps:

    * Use Web3.py to call the `newAppraisal` function of the contract to record a new appraisal when someone clicks the Appraise Artwork button.

        > **Hint** You can use the first account, in `w3.eth.accounts[0]`, for the transaction.

4. In `app.py`, in the “Get Appraisals” section, complete the following substeps:

    * Create a Streamlit component that gets an artwork token ID from the user.

    * In the button code, create a filter that lists all the appraisal events for the token.

    * Display all the entries from the event filter on the webpage.

5. Run the application by using `streamlit run app.py`. Test the functionality of the dApp to make sure that it works as expected.
