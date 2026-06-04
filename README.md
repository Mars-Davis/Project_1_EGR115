# Project Documentation EGR115
Project Overview
The Circuit Calculator and safety check is a Python program that calculates the current in a circuit and helps determine whether a selected electrical wire gauge is safe for a given electrical load. The program compares calculated current against predefined ampacity values for different wire sizes and outputs a safety result.
This project demonstrates how programming can be applied to basic electrical engineering principles.
Purpose
The purpose of this program is to:
Simulate a basic engineering safety check for wire selection
Help determine if a wire can safely handle a given electrical current
Apply fundamental programming concepts to a real-world engineering problem
How It Works
The user creates a circuit with resistors connect either in series or parallel
The user selects a wire gauge (AWG)
The program uses a list to store available wire sizes
A tuple stores corresponding maximum current ratings
The program matches the selected AWG to its ampacity using index positions
The user enters the expected current load
The program compares values and outputs:
Safe
Unsafe
