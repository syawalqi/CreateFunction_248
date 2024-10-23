import math

Lambda = lambda jari_jari: math.pi * (jari_jari ** 2)

jari_jari = float(input("Masukkan Jari-jari: "))
Lambda = jari_jari
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {Lambda}")