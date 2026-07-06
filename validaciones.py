def leer_patente(patente):
    while True:
        patente = input(patente).strip().upper()
        largo = len(patente)
        
        if largo == 6:
            letras = patente[0:3]
            numeros = patente[3:6]
            if letras.isalpha() and numeros.isdigit():
                return patente
        elif largo == 7:
            letras1 = patente[0:2]
            numeros = patente[2:5]
            letras2 = patente[5:7]
            if letras1.isalpha() and numeros.isdigit() and letras2.isalpha():
                return patente
                
        print("Error: Formato de patente inválido (Debe ser AAA123 o AA123AA).")