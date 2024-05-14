class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Create a dictionary to store the substitution table
        substitution_table = {}
    
        # Iterate through each character in the key
        seen_letters = set()
        for char in key:
            if char.isalpha() and char.islower() and char not in seen_letters:
                # Map the lowercase letter to the next available alphabet letter (starting from 'a')
                substitution_table[char] = chr(ord('a') + len(substitution_table))
                seen_letters.add(char)
    
        # Fill in any missing letters in the substitution table with the remaining alphabet letters
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for letter in alphabet:
            if letter not in substitution_table:
                substitution_table[letter] = letter
    
        # Decode the message using the substitution table
        decoded_message = []
        for char in message:
            if char == ' ':
                # Preserve spaces in the decoded message
                decoded_message.append(' ')
            elif char in substitution_table:
                # Substitute the character using the substitution table
                decoded_message.append(substitution_table[char])
    
        # Join the decoded characters into the final decoded message string
        return ''.join(decoded_message)