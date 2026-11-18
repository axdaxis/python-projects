# Number Sequence Analyzer

Create a command-line program that lets the user work with different number sequences and mathematical patterns.

## Project Goal

The program must display a menu and allow the user to repeatedly select different operations.

## Required Features

Include at least these options:

1.  Generate a Fibonacci sequence

2.  Check if a number is prime

3.  Display all prime numbers in a range

4.  Generate a multiplication table

5.  Calculate a factorial

6.  Run a Collatz sequence

7.  Exit the program

## Requirements

Your program must:

-   Use a loop to keep the menu running until the user selects Exit.

-   Use `if`, `elif`, and `else` statements to process menu choices.

-   Use loops to calculate results.

-   Validate user input.

-   Prevent invalid values where appropriate.

-   Display results clearly.

### Fibonacci Sequence

Ask the user how many numbers to generate.

Example:

```
How many values? 8

0, 1, 1, 2, 3, 5, 8, 13
```

### Prime Number Check

Ask for a number and determine whether it is prime.

```
Enter a number: 17

17 is a prime number.
```

### Prime Number Range

Ask for a starting and ending number and display every prime number in that range.

### Multiplication Table

Ask for a number and a table length.

```
Number: 7
Length: 5

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
```

### Factorial

Calculate the factorial of a number using a loop.

### Collatz Sequence

Ask for a positive integer.

If the number is even:

```
number = number / 2
```

If the number is odd:

```
number = number * 3 + 1
```

Continue until the number reaches `1`.

Also display how many steps were required.