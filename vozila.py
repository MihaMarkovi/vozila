class Vozila(object):

    def __init__(self, znamka, model, st_km, datum_servisa):
        self.znamka = znamka
        self.model = model
        self.st_km = st_km
        self.datum_servisa = datum_servisa
        

    def izpisi_vozilo(self):
        return self.znamka + ", " + self.model + ": " + self.st_km

moja_vozila = []

def dodaj_vozilo():
    znamka = raw_input("Znamka vozila: ")
    model = raw_input("Model vozila: ")
    st_km = raw_input("Stevilo prevozenih kilometrov: ")
    datum_servisa = raw_input("Datum zadnjega servisa: ")

    vozilo = Vozila(znamka, model, st_km, datum_servisa)

    moja_vozila.append(vozilo)


def izberi_vozilo():
    
    
    num = int(raw_input("vpisi zaporedno stevilko vozila"))
    
    if not ( 0 <= num < len(moja_vozila)):
        print("Vozilo ni najdeno.")
        return -1
    return num

def izbrisi_vozilo():
    num = izberi_vozilo()
    if num == -1:
        
        return
    
    print("Brisem ....")
    
    bliznjica = False
    if bliznjica:
        
        izbrisani = moja_vozila.pop(num)
    else:
        
        izbrisani = moja_vozila[num]
       
        del moja_vozila[num]


    print("Izbrisal: " + izbrisani.izpisi_vozilo())

def uredi_vozilo():
    num = izberi_kontakt()
    if num == -1:
        
        return
  
    print("Urejanje: " + moja_vozila[num].izpisi_vozilo())
    znamka = raw_input("Znamka vozila: ")
    model = raw_input("Model vozila: ")
    st_km = raw_input("Stevilo prevozenih kilometrov: ")
    datum_servisa = raw_input("Datum zadnjega servisa: ")

    
    kontakt = Contact(znamka, model, st_km, datum_servisa)

    
    moja_vozila[num] = vozilo

    

def izpisi_vozila():
    print("St \t| Vozila")
    print("-"*50)
    for j in range(len(moja_vozila)):
        print(str(j) + "\t| " + moja_vozila[j].izpisi_vozilo())

while True:
    odgovor = raw_input("Povej kaj zelis narediti (dodaj, izbrisi, uredi, izpisi, koncaj)?").lower()
    
    if odgovor == "dodaj":
        dodaj_vozilo()
    elif odgovor == "uredi":
        uredi_vozilo()
    elif odgovor == "izbrisi":
        izbrisi_vozilo()
    elif odgovor == "izpisi":
        izpisi_vozila()
    elif odgovor == "koncaj":
        break
    else:
        print("Nisem razumel odgvora :(")

