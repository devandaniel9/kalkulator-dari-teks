# Kalkulator dari teks

import streamlit as st

# streamlit run Kalkulator-dari-teks-3.py
st.title("Program Kalkukator dari Teks ")
# Input

st.write("##### *Created by Devan Daniel Nainggolan (Kelas 8 Betania)*")
st.write("")
st.write("""
- Program ini dapat menyelesaikan permasalahan Matematika dalam bentuk text
- Program ini otomatis mendahulukan perkalian (*) dan pembagian (/) terlebih dahulu dari kiri ke kanan. Kemudian dilanjutkan dengan pertambahan (+) dan pengurangan (-).""")

st.write("### **Masukkan operasi matematika yang ingin dicari solusinya **")
angka = st.text_input("kali (*), bagi (/), tambah (+), kurang (-)", "21 - 2 * 5+ 3 * 4 + 2 * 3")
#angka = "21-2*5+3*4+2*3"
# -----
    
angka2 = list(angka)

angka = angka + "+"

abc = []
a = ""
for angka2 in angka:
    if angka2 == "+" or angka2 == "-" or angka2 == "*" or angka2 == "/":
        abc.append(int(a))
        abc.append(angka2)
        a = ""
    else:
        a = a + angka2

abc.pop(-1)

def fungsi(a):
    if a[1] == "+": b = a[0]+a[2]
    if a[1] == "-": b = a[0]-a[2]
    if a[1] == "*": b = a[0]*a[2]
    if a[1] == "/": b = a[0]/a[2]
    return b

def fungsi2(a):
    c = ""
    for b in a:
        c = c + str(b)
    return c

def fungsi3(a):
    count = 0
    check = True
    for b in a:
        if b == "*" or b == "/":
            check = False
            break
        count += 1
    if check:
        count = 1
    return count

x = fungsi2(abc).replace("*","\*")
#st.write(f"1. {x}")
i = 1

st.write("### **Solusi Matematika**")
while len(abc) > 1:
    letak = fungsi3(abc)

    abc = abc[0:letak-1] + [fungsi(abc[letak-1:letak+2])] + abc[letak+2:]

    x = fungsi2(abc).replace("*","\*")
    st.write(f"{i}. {x}")
    i += 1

st.write("### Jawabannya adalah", f"**{x}**")