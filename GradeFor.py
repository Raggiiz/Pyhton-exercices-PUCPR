nome = input("What's your name: ")

id = int(input("What's your studant number: "))

sum_ = 0
text = ""

for cont in range(1, 5):
    test = float(input("Grade of your %d test: " % cont))
    hw = float(input("Grade of your %d home work: " % cont))
    text += "Test %d: %d - Home work %d: %d - " % (cont, test, cont, hw)
    media = test * 0.6 + hw * 0.4
    sum_ += media

mediaAnual = sum_ / 4

print(text)
print("Your anual grade is %.1f" % mediaAnual)

if mediaAnual >= 7:
    print ("You are aproved")
else:
    print("You are failed")