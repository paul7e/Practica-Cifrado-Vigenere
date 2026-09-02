# Integrantes del equipo:
#Abad Gonzalez Pablo
#Herrera Rojas Ximena 
#Ramos Cabrera Paul Manuel 
#Lozano Bustamante Miguel Alejandro 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

module = len(alphabet)

def Encrypted(message, key):
    result = ""
    message = message.lower()
    key = key.lower()
    keyLength = len(key)
    
    for i in range(len(message)):

        messageChar = message[i]

        if messageChar in alphabet:
            letterPosition = alphabet.index(messageChar)
            letterPositionKey = alphabet.index(key[i % keyLength])
            letterPositionEncrypted = (letterPosition + letterPositionKey) % module

            result += alphabet[letterPositionEncrypted]
        else:
            
            result += messageChar

    return result



def Decrypted(encryptedMessage, key):
    result = ""
    encryptedMessage = encryptedMessage.lower()
    key = key.lower()
    keyLength = len(key)
    
    for i in range(len(encryptedMessage)):

        messageChar = encryptedMessage[i]
        
        if messageChar in alphabet:
            letterPosition = alphabet.index(messageChar)
            letterPositionKey = alphabet.index(key[i % keyLength])
            letterPositionDecrypted = (letterPosition - letterPositionKey) % module
            
            result += alphabet[letterPositionDecrypted]
        else:

            result += messageChar
            
    return result


print(f"\n")
message = input("Message: ")
key = input("Key: ")

encryptedMessage = Encrypted(message, key)
decryptedMessage = Decrypted(encryptedMessage, key)


print(f"\n------------------------------------")
print(f"Message:    {message}")
print(f"Key:        {key}")
print(f"Encrypted:  {encryptedMessage}")
print(f"Decrypted:  {decryptedMessage}")
print(f"------------------------------------\n")

