# programi per vendosjen e notes ne baze te pikeve

piket = int(input("Numri i pikeve te provimit: "))
if 0 <= piket < 50:
    nota = 5
elif 50 <= piket < 60:
    nota = 6
elif 60 <= piket < 70:
    nota = 7
elif 70 <= piket < 80:
    nota = 8
elif 80 <= piket < 90:
    nota = 9
elif 90 <= piket <= 101:
    nota = 10
else:
    print("Piket e shenuara jane jo valide")
    exit(0)

print("Nota:", nota)