#------KAPATMA ASİSTANI 1.0 - github.com/bahaakbas02-dev------

import tkinter as tk
import os

#------Fonksiyonlar------

def kapat():
    os.system("shutdown /s /t 0")

def yenidenBaslat():
    os.system("shutdown /r 0")

def oturumuKapat():
    os.system("shutdown /l")    

def sureliKapat():
    global input1Value

    input1Value = input1.get()

    os.system(f"shutdown /s /t {input1Value}")

def sureliRestart():
    global input2Value

    input2Value = input2.get()

    os.system(f"shutdown /r /t {input2Value}")

#------Kullanıcı Arabirimi------

root = tk.Tk()
root.geometry("600x600")
root.title("KAPATMA ASİSTANI 1.0")

label1 = tk.Label(text="KAPATMA ASİSTANI 1.0", font=("Arial", 24))
label1.pack(pady=10)

#------Kapatma Düğmesi------
dugme1 = tk.Button(text="Kapat", command=kapat, bg="red", font=("Arial", 16))
dugme1.pack(pady=10)

#------Oturumu Kapatma Düğmesi------
dugme2 = tk.Button(text="Oturumu Kapat", command=oturumuKapat, bg="yellow" , font=("Arial", 16))
dugme2.pack(pady=10)

#------Yeniden Başlatma Düğmesi------
dugme3 = tk.Button(text="Yeniden Başlat", command=yenidenBaslat, bg="green", font=("Arial", 16))
dugme3.pack(pady=10)

#------Süreli Kapatma------
label2 = tk.Label(text="SÜRELİ KAPAT", font=("Arial", 24))
label2.pack(pady=5)

aciklama1 = tk.Label(text="(saniye ile ölçülür)", font=("Arial", 14))
aciklama1.pack(pady=5)

input1 = tk.Entry(width=24)
input1.pack(pady=5)

dugme4 = tk.Button(text="Süreli Kapat ⏱️", command=sureliKapat, bg="red", font=("Arial", 16))
dugme4.pack(pady=5)

#------Süreli Yeniden Başlatma------
label2 = tk.Label(text="SÜRELİ YENİDEN BAŞLAT", font=("Arial", 24))
label2.pack(pady=5)

aciklama2 = tk.Label(text="(saniye ile ölçülür)", font=("Arial", 14))
aciklama2.pack(pady=5)

input2 = tk.Entry(width=24)
input2.pack(pady=5)

dugme5 = tk.Button(text="Süreli Yeniden Başlat ⏱️", command=sureliRestart, bg="green", font=("Arial", 16))
dugme5.pack(pady=5)

root.mainloop()