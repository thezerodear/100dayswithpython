alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = ("""
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88                                                                           
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88   """)
print(logo)
print("Welcome to the Caesar Cipher program!")
print("This program will encrypt and decrypt messages using the Caesar Cipher.")


def caesar_cipher(original_text, shift,encode_decode): 
        if encode_decode == "encode":
          output = encode(original_text, shift)
          print(f"Encoded message: {output}")
        elif encode_decode == "decode":
          output = decode(original_text, shift)
          print(f"Decoded message: {output}")




def encode(original_text,shift):
   output = ""
   for i in original_text:
      if i in alpha:
         index = alpha.index(i)
         new_index = (index + shift) % 26
         output += alpha[new_index]
      else:
         output += i
   return output

def decode(original_text,shift):
   output = ""
   for i in original_text:
      if i in alpha:
         index = alpha.index(i)
         new_index = (index - shift) % 26
         output += alpha[new_index]
      else:
         output += i
   return output


# main loop

while True:
    print("\nPlease choose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        caesar_cipher(message, shift,"encode")
        print("Message encrypted successfully!")
    elif choice == "2":
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        caesar_cipher(message, shift,"decode")
        print("Message decrypted successfully!")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

            