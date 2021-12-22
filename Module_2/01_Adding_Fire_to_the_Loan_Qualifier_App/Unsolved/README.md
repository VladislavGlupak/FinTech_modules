# Activity: Adding Fire to the Loan Qualifier App

In this activity, you'll enhance the Loan Qualifier application by incorporating the Fire library and adding CLI interactivity.

## Background

Up to this point, the loan qualifier application has hardcoded users' values. Now you'll take the application to the next level by allowing the user to input these values dynamically through the Fire CLI library.

## Instructions

Use the files in the Unsolved folder to complete the following steps.

1. Open `app.py` and import `fire`at the top of the file.

2. At the bottom of `app.py`, replace the `run()` function with the `if __name__ == "__main__":` declaration. Move the call to the `run()` function inside the conditional.

    > **Hint** Be sure to test your code by running your program from the command line (Terminal or Git Bash). In the next steps, you'll refactor the function call to incorporate dynamic input from the CLI.

3. Remove the parentheses from `run()` and pass the function reference to `fire.Fire()`.

    > **Hint** Test your code again by running the program from the CLI.

4. To accept dynamic input for the user's `credit_score` variable, complete the following steps:

    * Inside the `run()` function, comment out the variable `credit_score = 750`.

    * Pass the variable `credit_score` into the `run()` function as a parameter.

    * In your CLI, run the program using the following syntax: `python app.py --credit_score=750`

        > **Note** With this syntax, you're dynamically passing the value of 750 to the variable credit score via a command-line argument.

    * Confirm that your program returns the same variables for the monthly debt-to-income and loan-to-value ratios as well as the number of qualifying loans.

5. Refactor your code using the preceding steps to dynamically take in the values for the variables `debt` and `income`.

    > **Hint** You can list multiple arguments in your command-line instruction, like in the following example:
    >
    > `python app.py --credit_score=750 --debt=5000`.

6. Now that you can dynamically enter information for the user, try to pass different values from the command line into the program. How do the values change for the monthly debt-to-income ratio, loan-to-value ratio, and number of qualifying banks?
