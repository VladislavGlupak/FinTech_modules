/*

Adding Getters and Setters
--------------------------
In this activity, you’ll add a getter and a setter function to the `CustomerAccount` contract that you created earlier.

Instructions
------------
1. Open the Remix IDE. Either paste the code from the starter file into a new Solidity file or open the `customer_contract.sol` file that you created earlier.

2. Create a `view public` getter function named `getInfo` that resembles the following:

    ```solidity
    function getInfo() view public returns() {
      // return user data here
    }
    ```

3. In `returns`, specify the types of data that the `getInfo` function will return. Return the values of all the variables that you specified before, such as those of `address`, `isNewAccount`, `accountBalance`, `customerName`, and `customerLastName`.

    > **Hint** Remember to surround multiple return values with parentheses, and remember to add the semicolons!

4. Because you no longer need the default values for the customer info, remove them.

5. Create a setter function named `setInfo` that resembles the following:

    ```solidity

    function setInfo(address newOwner, bool newAccountStatus,
    uint newAccountBalance, string memory newCustomerName,
    string memory newCustomerLastName) public {
      // set user data here
    }
    ```

    > **Hint** Remember that all the setter does is set the new values of the customer variables.

6. Compile your smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.

*/


pragma solidity ^0.5.0;

contract CustomerAccount {
    address owner = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
    bool isNewAccount = true;
    uint accountBalance = 10000;
    string customerName = "Jordan";
    string customerLastName = "Habib";
}
