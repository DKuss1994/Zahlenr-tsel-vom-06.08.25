from cryptography.fernet import Fernet

class PasswortManager:
    def __init__(self, key_file ="key.key", enc_file = "passwort.enc"):
        self.key_file = key_file
        self.enc_file = enc_file

# Hier wird der Schlüssel zum öffnen der Chiffre erstellet. Und die Chiffren funktion wird damit erstellt
    def erstelle_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as file:
          file.write(key)
        print(f"Schlüssel zur Chiffre wurde erstellt in {self.key_file}")

#wb und rb für writte binar und read binar lesen und schreiben binare code zahlen


#Hier lesen wir den Schlüssel aus der erstellen Datei raus für den Werkezeugkasten. also der Chiffre
    def lade_key(self):
        with open(self.key_file,"rb") as file:
            return file.read()

    def verschlüssel_password(self, password: str):
        key = self.lade_key()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(password.encode())
        with open(self.enc_file, "wb") as file:
            file.write(encrypted)
        print(f"passwort wurd verschlüsselt und in Passwort.enc gepackt{self.enc_file}")


    def lade_password(self) -> str:
        with open(self.key_file, "rb")as file:
            schlüssel = file.read()
        cipher = Fernet (schlüssel)
        with open(self.enc_file,"rb")as file:
            token = file.read()
        return cipher.decrypt(token).decode()
