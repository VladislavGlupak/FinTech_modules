/*
SafeMath

Instructions:

1. Navigate to Remix, and create a new file called `ArcadeTokenSafeMath.sol`. Copy the contents of this activity’s starter file into Remix to help you get started.

2. Add the following import statement just below the pragma and above the contract definition:

  ```solidity
import "github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";
```

3. Define a smart contract called `ArcadeToken`.

4. Add the following as the first line of code in your smart contract:

  ```solidity
  using SafeMath for uint;
  ```

 > **Note** This statement will link the SafeMath library to the `uint` type, allowing you to call `.add`, `.sub`, `.mul`, `.div`, etc. directly from a `uint`, rather than using `&plus;`, `&minus;`, `*`, and `/`.

5. Replace every math operation in the contract with the SafeMath equivalent. For example, the following code:

  ```solidity
  balances[msg.sender] -= value;
  ```

becomes:

  ```solidity
  balances[msg.sender] = balances[msg.sender].sub(value);
  ```

6. Deploy and test your contract. You should now be safe from any integer underflows and overflows!

> **Hint** Remember to include the variable reassignments&mdash;SafeMath will not mutate the variable it is operating on. You must reassign the variable with an `=`. For example: `balances[recipient] = balances[recipient].add(value);`.

*/

pragma solidity ^0.5.0;

// @TODO: import the SafeMath library via Github URL
// YOUR CODE HERE!

contract ArcadeToken {
    // @TODO: add the "using SafeMath..." line here to link the library to all uint types
    // YOUR CODE HERE!

    address payable owner = msg.sender;
    string public symbol = "ARCD";
    uint public exchange_rate = 100;

    mapping(address => uint) balances;

    function balance() public view returns(uint) {
        return balances[msg.sender];
    }

    function transfer(address recipient, uint value) public {
        // @TODO: replace the following with the .sub function
        balances[msg.sender] -= value;
        // @TODO: replace the following with the .add function
        balances[recipient] += value;
    }

    function purchase() public payable {
        // @TODO: replace the following with the .mul function
        uint amount = msg.value * exchange_rate;
        // @TODO: replace the following with the .add function
        balances[msg.sender] += amount;
        owner.transfer(msg.value);
    }

    function mint(address recipient, uint value) public {
        require(msg.sender == owner, "You do not have permission to mint tokens!");
        // @TODO: replace the following with the .add function
        balances[recipient] += value;
    }
}
