import sys

inputList = sys.argv
parola = inputList[2]
nume_fisier_input = inputList[1]
nume_fisier_output = inputList[3]
fisier_input = open(nume_fisier_input, "r")
fisier_output = open(nume_fisier_output, "w")

text_initial = fisier_input.read()

lungime_text = len(text_initial)
lungime_parola = len(parola)

parola_multiplicata = parola * (lungime_text // lungime_parola)
missing = lungime_text % lungime_parola
parola_multiplicata += parola[:missing]
text_final = ""    

for indice in range(0, lungime_text):
    noul_caracter = ord(text_initial[indice]) ^ ord(parola_multiplicata[indice])
    cod_caracter = bin(noul_caracter)[2:].zfill(8)
    text_final += chr(noul_caracter)
fisier_output.write(text_final)
"""
python decrypt.py output parolamea2021 input_recuperat.txt

"""