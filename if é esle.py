financed=float(input("qual o valor do imóvel a ser financiado? "))
salary=float(input("qual o salário do cliente? "))
year=float(input("Em quantos anos o cliente deseja pagar o imóvel? "))
yoursalary= salary*0.30
prestacao=float(financed/(year*12))
if float(prestacao <= salary):
    print("sim ")
else:
    print("não ")
print(f"seu financiciado é {yoursalary }")
print(f"pretacao é {int(prestacao) }")