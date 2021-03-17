#zad1
# A=[1-x for x in range(1,11)]
# print(A)
# B=[4**x for x in range(0,8)]
# print(B)
# C=[x for x in B if x%2==0]
# print(C)

#zad2
# import random
# lista1=[random.randrange(0, 100) for x in range(0,10)]
# print(lista1)
# lista2=[x for x in lista1 if x%2==0]
# print(lista2)

#zad3
# slownik1={'arbuz':'kg','mak':'sztuki','ziemniaki':'kg','banany':'sztuki'}
# print(slownik1)
# slownik2={x for (x,y) in slownik1.items() if y=='sztuki'}
# print(slownik2)

#zad4
# def trojkat(a,b,c):
#     if a>b:
#         if a>c:
#             if ((b * b) + (c * c)) == (a * a):
#                 print("Jest prostokątny")
#             else:
#                 print("Nie jest prostokątny")
#         else:
#             if ((a * a) + (b * b)) == (c * c):
#                 print("Jest prostokątny")
#             else:
#                 print("Nie jest prostokątny")
#     elif a<b:
#         if b>c:
#             if ((a * a) + (c * c)) == (b * b):
#                 print("Jest prostokątny")
#             else:
#                 print("Nie jest prostokątny")
#         else:
#             if ((a * a) + (b * b)) == (c * c):
#                 print("Jest prostokątny")
#             else:
#                 print("Nie jest prostokątny")
#     else:
#         if a>c:
#             print("Nie jest prostokątny")
#         elif a<c:
#             if ((a * a) + (b * b)) == (c * c):
#                 print("Jest prostokątny")
#             else:
#                 print("Nie jest prostokątny")
#         else:
#             print("Nie jest prostokątny")
#
# trojkat(3,4,5)

#zad5
# def trapez(a=2,b=5,h=10):
#     print(((a+b)*h)/2)
# trapez()

#zad6
# def ciag(a1=1,b=4,ile=10):
#     a=[a1]
#     for x in range(1,ile):
#         a1*=b
#         a.append(a1)
#     print(a)
# ciag()