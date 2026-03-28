from cryptography.fernet import Fernet

def executer_chiffrement():
   
    cle = Fernet.generate_key()
    cipher_suite = Fernet(cle)
    
    print(f"Clé générée : {cle.decode()}")

    message_original = "Ceci est un secret d'État.".encode()

    message_chiffre = cipher_suite.encrypt(message_original)
    print(f"\nMessage chiffré (Token) : {message_chiffre.decode()}")

    
    message_dechiffre = cipher_suite.decrypt(message_chiffre)
    print(f"\nMessage déchiffré : {message_dechiffre.decode()}")

if __name__ == "__main__":
    executer_chiffrement()
