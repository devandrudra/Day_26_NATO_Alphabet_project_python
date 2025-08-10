# Phonetic Alphabet Generator
Generate a phonetic alphabet (e.g. NATO-like or custom phonetic mappings) from input text or words — useful for spelling, testing voice recognition, teaching pronunciation, or generating mnemonic phrases.

# Features
Convert any string into a phonetic sequence (word-for-letter)

Support for built-in alphabets (NATO / custom)

Option to generate randomized or deterministic mnemonic words per letter

CLI and importable Python module usage

Easily extendable with custom alphabets or language mappings

# Demo
Input:  rudra

Output: ['Romeo', 'Uniform', 'Delta', 'Romeo', 'Alfa']

# How It works-

1. CSV file which stores all char and associated NATO representation
2. opening as dataframe and making a dictionary using dictionary comprehension for char and associated NATO word
3. making a list which stores all of the input char NATO represenatation
