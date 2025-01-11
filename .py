Hasen = []
Kühlschrank = []
Geld = 100

def add_hase():
    Hase = input(("Wie heißt der Hase den du adoptieren willst?: ")).capitalize()
    if Hase in Hasen:
        print("Du hast so ein Hasen bereits!")
        return
    else:
        Hasen.append(Hase)
        print(f"Du hast {Hase} adoptiert!")

def pet_hase():
    Hase = input("Welchen Hasen willst du streicheln?: ")
    if Hase not in Hasen:
        print("Der Hase existiert nicht!")
        return
    else:
        print(f"Du hast {Hase} gestreichelt!")
        Geld.append(50)
        print(f"50 Euro wurden hinzugefügt! Aktuelles Geld: {sum(Geld)} Euro")

def fill_kühlschrank():
    print("Möchtest du etwas Futter für deine Hasen kaufen?")
    reply = input("Yes/No").capitalize()
    if reply == "Yes":
        shopping = input("Du kannst Karrotten, Salat oder Brot kaufen: ").capitalize()
        if shopping in "Karotten" or "Salat" or "Brot":
            print(f"Du hast {shopping} für 25 Euro gekauft")
            if Geld >= 25:
                Geld -= 25
            else:
                print("Nicht genug Geld")
                return
            print(f"25 Euro wurden abgezogen! Aktuelles Geld: {sum(Geld)} Euro")
        else:
            print("Solch ein Futter haben wir nicht")
            return
        
def feed_hase():
    Hase = input("Welchen Hasen willst du füttern?: ")
    if Hase not in  Hasen:
        print("Der Hase existiert nicht!")
        return
    else:
        print(Kühlschrank)
        futter = input("Was möchtest du {Hase} geben?: ").capitalize()
        if futter not in  Kühlschrank:
            print("Dieses Futter besitzt du nicht")
            return
        else:
            print(f"Du hast {Hase} mit {futter} gefüttert!")
            Kühlschrank.remove(futter)
            print(f"{futter} ist aus deinem Kühlschrank verschwunden!")