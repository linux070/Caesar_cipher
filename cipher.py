# ``````` Building a Ceaser cipher program.````````

cipher = ('''
          
  ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|   
      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|             
''')         
print(cipher)
print("WELCOME TO THE CEASER CIPHER PROGRAM\n")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt (plain_text, shift_amount):
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter) # ------ list.index(element)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f'The encoded text is : "{cipher_text}"') 

# # ````` NOW TO DECRYPTNG/DECODE.... just the same method brrrrrr, just that we gonna subtract this time around```````
# def decrypt(new_text, shift_amount):
#     decipher_text = ""
#     for letter in new_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decipher_text += new_letter
#     print(f'The decoded text is : "{decipher_text}"')    


# if direction == "encode" :
#  encrypt(plain_text= text, shift_amount= shift)
# else:
#   decrypt(new_text = text, shift_amount = shift)
def caesar (start_text, shift_amount, cipher_direction):
    # if cipher_direction == "decode": 
    #    shift_amount *= - 1
    end_text = ""
    for char in start_text:
      if char in alphabet:
          position = alphabet.index(char)
          if cipher_direction == "encode":
           new_position = position + shift_amount
          else:
           new_position = position - shift_amount 
          end_text += alphabet[new_position] 
      else :
        end_text += char
      # new_position = position + shift_amount
    print(f"The {cipher_direction}d text is {end_text}")

cipher_end = True
while cipher_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26  
  caesar(start_text = text, shift_amount = shift, cipher_direction = direction) 
  result = input("Type 'yes' if you want to go again. Otherwise type 'no' \n")  
  if result == "no":
    cipher_end = False
    print("Goodbye, see you again.")

  # ````` linuxmode ``````
        

       
