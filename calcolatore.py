def somma(a, b):
    return a + b


if __name__ == "__main__":
    print("=== CALCOLATORE ===")
    x = float(input("Inserisci il primo numero: "))
    y = float(input("Inserisci il secondo numero: "))
    risultato = somma(x, y)
    print(f"Risultato della somma: {risultato}")