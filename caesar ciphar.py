from art import logo
print(logo) 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
to_continue = True

while to_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  
  def caesar(user_direction = direction):
    caesar_text = ""
    for letter in text:
        if letter in alphabet:
          position = alphabet.index(letter)
          if direction == "encode":
            new_position = position + shift
          elif direction == "decode":
            new_position = position - shift
          new_letter = alphabet[new_position]
          caesar_text += new_letter
        else:
          caesar_text += letter
    print(f"The {direction}d text is {caesar_text}.")    
  
  caesar(user_direction = direction) 
  decision = input("Want to continue? Type 'yes' or 'no'.\n")
  if decision == "no":
    to_continue = False
    print("Thanks for using Caesar Cipher.")
    