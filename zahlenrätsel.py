
from random import randint
import os
import json

class Zahlenrätsel:
  def __init__(self):
    self.highscore_liste = []
    self.counter = 0
    self.minimum = 1
    self.maximum = 5
    self.pc_zahl = randint(self.minimum, self.maximum)
    self.admincode = "Hallo"
    self.ende = 1
  
   # Einfach Json speicherung des Telefonbuches
  def speichern (self):
    speichern = {"Highscore": self.highscore_liste,}
    with open ("speichern.json", "w") as file:
      json.dump(speichern, file, indent=2)
      print("Programm wurde erfolgreich gespeichert!")
  # Hier wird die Jsondatei geladen.
  def laden (self):
    if os.path.exists("speichern.json"):
        with open ("speichern.json", "r") as file:
          daten = json.load(file)
          self.highscore_liste = daten["Highscore"]
          print("Programm wurde erfolgreich geladen")
    else:
      print("Kein Speicherstand gefunden.")
  
  def passwort_brauch(self):
    buchstaben = "q w e r t z u i o p ü a s d f g h j k l ö ä y x c v b n m "
    x = buchstaben.split()
    y = buchstaben.upper().split()
    buchstaben = x + y
    buchstaben = sorted(buchstaben)
    return buchstaben
  

  def prüfung_passwort(self, passwort):
    buchstaben = self.passwort_brauch()
    if any(x in buchstaben for x in passwort):
      return True
    else:
      print(f"Dein Passwort brauch mindestens ein Buchstaben")
      return False
    

    

  def code_ändern(self):
    print(f"Aktuellercode {self.admincode}")
    while True:
      pw_1 = self.eingabe("Neues Passwort eingeben: ",str)
      if self.prüfung_passwort(pw_1) == False:
        continue
      pw_2 = self.eingabe("Noch einmal Passwort eingeben: ",str)
      if pw_1 == pw_2 :
        self.admincode = pw_1
        print(f"Admincode wurde erfolgreich in {self.admincode} geändert")
        break
      else:
        print(f"Admincode stimmt nicht überein. Versuch es noch einmal")
        continue
  def radius(self):
    print("Radius wird hier eingestellt! ")
    while True:
      self.minimum = self.eingabe("Gib deine niedrigste Ratezahl ein: ",int)
      self.maximum = self.eingabe("Gib die höchste Ratezahl ein: ", int)
      if self.maximum<=self.minimum:
        print("Die niedrigste Ratezahl ist größer als die große Ratezahl.")
        print(f"Niedrigste Zahl: {self.minimum}| Höchste Zahl: {self.maximum}")
        continue
      else:
        print ("Gib eine Zahl ein!")
        continue

  def admin_einstellung(self):
    while True:
      user_tuen = self.eingabe("Du bist im Einstellungmodus. Möchtest du den Rateradius einstellen (r). Willst du den Admincode ändern (a) und (b) fürs beenden: ",str).strip().lower()
      if user_tuen == "r":
        self.radius()
      elif user_tuen == "a":
        self.code_ändern()
      elif user_tuen == "b":
        print(f"Admincode: {self.admincode} Rateradius: {self.minimum}|{self.maximum}.")
        print("Einstellungmodus wird beendet")
        user_eingabe = 0
        break
      else:
        print("Du hast ein Fehler gemacht r, a oder n eingeben")

      

  def eingabe(self,frage:str, typ, min_value=None , max_value=None):
    try:
      while True:
        eingabe = input(frage)
        if eingabe == self.admincode:
          self.admin_einstellung()
        elif typ == int:
          eingabe = int(eingabe)
        elif typ == str:
          eingabe = str(eingabe)
        elif typ == float:
          eingabe = float(eingabe)
        else:
          raise TypeError (f"Typ {typ} wird nicht unterstützt.")
          # Validierungsbereich
        if min_value is not None and eingabe < min_value:
          print(f"❌ Deine Eingabe: {eingabe} ist kleiner als min_value: {min_value}")
          continue
        if max_value is not None and eingabe> max_value:
          print(f"❌ Deine Eingabe: {eingabe} ist größer als max_value: {max_value}")
          continue
        return eingabe
    except ValueError:
      print("Bitte benutzt Zahlen")
   
  def prüfung(self, user_eingabe):
    self.versuche()
    try: 
      if user_eingabe < self.pc_zahl:
        print (f"Deine Zahl {user_eingabe} ist kleiner als meine Zahl.")
      elif user_eingabe > self.pc_zahl:
        print (f"Deine Zahl {user_eingabe} ist größer als meine Zahl.")
      elif user_eingabe == self.pc_zahl:
        print ("Herzlichen Glückwunsch du hast das Spiel gewonnen!")
        self.bewertung(user_eingabe)
        self.highscore()
        self.pc_zahl = randint (self.minimum, self.maximum)
        self.counter = 0
        self.ende = 0
    except TypeError:
      pass
  
    
    
  def bewertung (self, user_eingabe):
    if user_eingabe == self.pc_zahl:
      if self.counter == 1:
        print (f"Du hast es mit {self.counter} geschafft. Auch ein bilndes Huhn trifft auf ein Korn.")

      elif self.counter < 5:
        print (f"Du hast es mit {self.counter} geschafft. Sehr starkes Spiel von dir.")
            
      elif self.counter > 10:
        print(f"Du hast es mit {self.counter} geschafft.Du musst echt noch üben.")
      else:
        print ("Du musst wirklich noch üben.")
  
  def highscore(self):
    name = self.eingabe("Gib dein Namen ein.", str)
    self.highscore_liste.append((self.counter,name))
    self.highscore_liste.sort()
    print(self.highscore_liste)

  def spiel_beenden(self):
    eingabe = self.eingabe("Willst du das Spiel beenden? (J/N)",str).strip().lower()
    if eingabe == "j":
      return False
    elif eingabe == "n":
      self.ende = 1
      return True
    else:
      print("Bitte mach eine richtige Eingabe.")



  def versuche(self):
    self.counter += 1

  def einleitung(self):
    print (f"Willkommen beim zahlen Rate Spiel. Hier spielst du gegen den Computer und versuchst eine Zahl zwischen {self.minimum} und {self.maximum} zu erraten. ")
  #Hauptprogramm:
  def start(self):
    self.einleitung()
    self.laden()
    while True:
      user_eingabe = self.eingabe("Gib eine Zahl ein: ",int, self.minimum, self.maximum)
      self.prüfung(user_eingabe)
      if self.ende == 0:
        x = self.spiel_beenden()
        if x == False:
          self.speichern()
          break

      

zahlenrätsel=Zahlenrätsel()
zahlenrätsel.start()
