
# ============================================================
# BYTE INSPECTOR
# ============================================================
# This program is a small cybersecurity learning tool.
#
# It does two main things:
#
# 1. Converts a decimal number into:
#       - Binary
#       - Hexadecimal
#
# 2. Inspects text and shows:
#       - The character
#       - Its decimal byte value
#       - Its hexadecimal value
#       - Its binary value
#       - Whether it is printable ASCII
#
# The purpose is to practice concepts used in:
# - Assembly programming
# - Reverse engineering
# - Malware analysis
# - Digital forensics
# - Cybersecurity
# ============================================================


# ------------------------------------------------------------
# FUNCTION 1: convert_number()
# ------------------------------------------------------------
# This function receives a decimal number and converts it
# into binary and hexadecimal.
#
# Example:
#
#     42 decimal
#        ↓
#     101010 binary
#        ↓
#     2A hexadecimal
# ------------------------------------------------------------

def convert_number(number):

    # Display a heading so the user knows what is being shown.
    print("\nNumber Conversion")
    print("-----------------")

    # Print the original decimal number.
    print(f"Decimal:     {number}")

    # bin() converts a number into binary.
    #
    # Example:
    # bin(42)
    # gives:
    # '0b101010'
    #
    # The "0b" tells us that the value is binary.
    print(f"Binary:      {bin(number)}")

    # hex() converts a number into hexadecimal.
    #
    # Example:
    # hex(42)
    # gives:
    # '0x2a'
    #
    # The "0x" tells us that the value is hexadecimal.
    print(f"Hexadecimal: {hex(number)}")


# ------------------------------------------------------------
# FUNCTION 2: inspect_text()
# ------------------------------------------------------------
# This function examines every character entered by the user.
#
# Example:
#
#     A
#
# The computer represents A using a numeric value:
#
#     Decimal = 65
#     Hex     = 41
#     Binary  = 01000001
#
# This is useful because computers ultimately work with
# numeric byte values rather than human-readable characters.
# ------------------------------------------------------------

def inspect_text(text):

    # Display a heading.
    print("\nByte Inspection")
    print("---------------")

    # A string can contain many characters.
    #
    # The for loop goes through them one at a time.
    #
    # Example:
    #
    #     "ABC"
    #
    # becomes:
    #
    #     A
    #     B
    #     C
    #
    for character in text:

        # ord() converts a character into its numeric
        # Unicode value.
        #
        # For normal ASCII characters, this is also their
        # ASCII value.
        #
        # Example:
        #
        #     ord("A") = 65
        #     ord("B") = 66
        #
        byte_value = ord(character)

        # Convert the numeric value into hexadecimal.
        #
        # Example:
        #
        #     65 → 0x41
        #
        hex_value = hex(byte_value)

        # Convert the numeric value into binary.
        #
        # Example:
        #
        #     65 → 0b1000001
        #
        binary_value = bin(byte_value)

        # ----------------------------------------------------
        # CHECK IF THE CHARACTER IS PRINTABLE ASCII
        # ----------------------------------------------------
        #
        # Standard printable ASCII characters have values
        # from 32 to 126.
        #
        # 32 = space
        # 48 = 0
        # 65 = A
        # 97 = a
        # 126 = ~
        #
        # Values below 32 are generally control characters.
        # Values above 126 are outside standard printable ASCII.
        #
        if 32 <= byte_value <= 126:
            printable = "Printable"
        else:
            printable = "Non-printable"

        # Display all the information about this character.
        #
        # !r shows the character in a way that makes spaces
        # and special characters easier to identify.
        #
        # Example output:
        #
        # 'A'  Decimal: 65   Hex: 0x41  Binary: 0b1000001
        #
        print(
            f"{character!r}  "
            f"Decimal: {byte_value:<3}  "
            f"Hex: {hex_value:<4}  "
            f"Binary: {binary_value:<10}  "
            f"{printable}"
        )


# ------------------------------------------------------------
# FUNCTION 3: main()
# ------------------------------------------------------------
# This is the main part of the program.
#
# It controls the interaction between the user and the
# functions we created above.
# ------------------------------------------------------------

def main():

    # Display the program title.
    print("BYTE INSPECTOR")
    print("==============")

    # --------------------------------------------------------
    # NUMBER CONVERTER
    # --------------------------------------------------------
    #
    # The while loop allows the user to convert multiple
    # numbers without restarting the program.
    #
    while True:

        # Ask the user for a decimal number.
        #
        # input() always gives us text, so later we convert
        # the input into an integer using int().
        user_input = input(
            "\nEnter a decimal number (or q to quit): "
        )

        # If the user enters q, stop the loop and exit.
        if user_input.lower() == "q":
            print("Goodbye!")
            break

        # ----------------------------------------------------
        # TRY / EXCEPT
        # ----------------------------------------------------
        #
        # The user might enter something that isn't a number.
        #
        # Example:
        #
        #     hello
        #
        # int("hello") would cause an error.
        #
        # try/except allows us to handle that error without
        # crashing the program.
        #
        try:

            # Convert the user's input from text into an integer.
            number = int(user_input)

            # For this beginner project, we only accept
            # positive numbers and zero.
            if number < 0:
                print("Please enter a positive number.")
                continue

            # Send the number to our conversion function.
            convert_number(number)

        except ValueError:

            # This message appears if the user enters something
            # that cannot be converted into an integer.
            print("Invalid input. Please enter a whole number.")

        # ----------------------------------------------------
        # BYTE INSPECTOR
        # ----------------------------------------------------
        #
        # After converting the number, ask the user whether
        # they want to inspect some text.
        #
        text = input(
            "\nEnter text to inspect (or press Enter to skip): "
        )

        # If the user entered text, inspect it.
        if text:
            inspect_text(text)


# ------------------------------------------------------------
# PROGRAM ENTRY POINT
# ------------------------------------------------------------
#
# Python executes the code below when this file is run
# directly using:
#
#     python main.py
#
# __name__ becomes "__main__" when this file is executed
# directly.
#
# This prevents main() from automatically running if another
# Python file imports main.py.
# ------------------------------------------------------------

if __name__ == "__main__":
    main()

