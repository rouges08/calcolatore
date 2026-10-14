def somma(a, b):
    return a + b

def divisione(a, b):
    if b == 0:
        return "Errore: Impossibile dividere per zero!"
    return a / b

if __name__ == "__main__":
    print("=== CALCOLATORE ===")
    x = float(input("Inserisci il primo numero: "))
    y = float(input("Inserisci il secondo numero: "))
    
    ris_somma = somma(x, y)
    print(f"Risultato della somma: {ris_somma}")
    
    ris_divisione = divisione(x, y)
    print(f"Risultato della divisione: {ris_divisione}")