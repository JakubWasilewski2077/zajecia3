import math

#zadanie1
#a)
print("i: ")
i = math.exp(10)
print(i)

#b)
print("j: ")
j = (math.log(5 + (math.sin(8) * math.sin(8))))**(1/6)
print(j)

#c
print("k: ")
# k =
#zadanie2
imie = "JAKUB"
nazwisko = "WASILEWSKI"
imie = imie.capitalize()
nazwisko = nazwisko.capitalize()
print(imie, " ", nazwisko)

#zadanie3
piosenka = "la la lo la la"
print("ile razy jest la?: ", piosenka.count("la"))

#zadanie4
lancuch4 = "nazwatest_nazwatest"
print(lancuch4[3])

#zadanie5
print(lancuch4.split("_"))

#zadanie6
stringzadanie6 = "string test xoxoxo"
floatzadanie6 = 5
szesnastokwa6 = 0xF
print(str(stringzadanie6))
print(float(floatzadanie6))
print(hex(szesnastokwa6))

#zadanie7
sporty = ['koszykowka','pilka nozna','rugby','siatkowka','plyawnie']
sporty.reverse()
orderforsporty = [0,1,3,4,2]
sporty = [sporty[i] for i in orderforsporty]
print(sporty)

#zadanie8
slownik = {'lol':'laughing out loud','lmao':'laughing my a## off','RP':'Rzeczy Pospolita'}

#zadanie9
gry = {'Splatoon':"platformer/movement shooter", 'BotW':'Sandbox/Open World/Action', 'Rayman':'platformer'}
print(len(gry))

# #zadanie10
# zdanie = input("Twoje zdanie: ")
# liczba_a = 0
# for letter in zdanie:
#     if letter == 'a':
#         liczba_a = liczba_a + 1
# print("*a* wystepuje: ", liczba_a)

# #zadanie11
# a = input('a:')
# b = input('b:')
# c = input('c:')
# if a != b and b != c:
#     if a > b and a > c:
#         print("a jest najwiekrze")
#     if a < b and c < b:
#         print("b jest najwiekrze")
#     if a < c and c > b:
#         print("c jest najwiekrze")
# else:
#     if a == b and b == c:
#         print("wartosci sa ruwne")

#zadanie12
# listaliczb = [24, 5.5, 16, 3.6]
# print(listaliczb)
# for x in listaliczb:
#     plistaliczb[] = x * x
# print(listaliczb)







