#Rate Spiel 

from random import randint

print ("Willkommen beim zahlen Rate Spiel. Hier spielst du gegen den Computer und versuchst eine Zahl zwischen 1 und 100 zu erraten. ")

  # Hier wird immer eine neue Zahl generiert für jede neue Runde.
zahl = randint (1, 100)
counter = 0

def prüfe_zahl (ich, zahl):
    if ich < zahl:
      
      print (f"Deine Zahl {ich} ist kleiner als meine Zahl.")
    elif ich > zahl:
    
      print (f"Deine Zahl {ich} ist größer als meine Zahl.")

    elif ich == zahl:
      
      print ("Herzlichen Glückwunsch du hast das Spiel gewonnen!")
      
    
def bewertung (counter):
  if ich == zahl:
    if counter == 1:
      print (f"Du hast es mit {counter} geschafft. Auch ein bilndes Huhn trifft auf ein Korn.")

    elif counter < 5:
      print (f"Du hast es mit {counter} geschafft. Sehr starkes Spiel von dir.")
          
    elif counter > 10:
      print(f"Du hast es mit {counter} geschafft.Du musst echt noch üben.")
    else:
      print ("Du musst wirklich noch üben.")
while True:
  try:
    ich = int(input("Tip eine Zahl ein. "))
    counter += 1
    prüfe_zahl(ich, zahl)
    bewertung(counter)
    if ich == zahl:
      weiter = input("Möchten Sie noch eine Runde Spielen? (j)")
      if weiter != "j":
        break
    
  except ValueError:
    print("Nur Zahlen benutzen. ")

schwierigkeit = input("Willst du den Schwierigkeits Level steigern(j)")
try:
  if schwierigkeit =="j":
    schwierigkeit_klein = int(input("Gib einmal die kleinste Zahl ein"))
    schwierigkeit_groß = int(input("Gib einmal die größte Zahl ein"))
    zahl = randint(schwierigkeit_klein,schwierigkeit_groß)
    counter = 0
    while True:
      #
      ich = int(input("Tip eine Zahl ein. "))
      counter += 1
      prüfe_zahl(ich, zahl)
      bewertung(counter)
      if ich == zahl:
        weiter = input("Möchten Sie noch eine Runde Spielen? (j)")
        if weiter != "j":
          break
    
except ValueError:
  print("Nur Zahlen benutzen. ")

print("Dankeschön für deine Zeit. Bitte probiere auch andere Sachen von mir aus. Gerne Feedback da lassen.")
