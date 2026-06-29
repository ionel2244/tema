from datetime import datetime

nume = input("Introdu numele: ")
data_nasterii = input("Introdu data nașterii (zz-ll-aaaa): ")

data_nasterii = datetime.strptime(data_nasterii, "%d-%m-%Y")

azi = datetime.today()

varsta = azi.year - data_nasterii.year

if (azi.month, azi.day) < (data_nasterii.month, data_nasterii.day):
    varsta -= 1

print(f"\nSalut, {nume}!")
print(f"Ai {varsta} ani.")