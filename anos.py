from datetime import date

hoje=date.today().year
nasc=int(input("ano: "))
idade=hoje-nasc
print()

if idade<=9:
    print("Este atleta é da base mirin")
elif idade<=14:
    print("Este atleta é da base infantil")
elif idade<=19:
    print("Este atleta é da base junior")
elif idade<=25:
    print("Este atleta é da base senior")
else:
    print("Este atleta é da base master")