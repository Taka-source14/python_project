import tkinter as tk
from tkinter import messagebox
import re

class HesapMakinesi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Hesap Makinesi")
        self.pencere.geometry("350x500")  # Pencere boyutu güncellendi
        self.pencere.configure(bg="#2c3e50")  # Arka plan rengi güncellendi
        self.pencere.resizable(False, False)  # Pencere boyutu sabit

        # Ekran Frame'i
        ekran_frame = tk.Frame(self.pencere, bg="#2c3e50")
        ekran_frame.pack(padx=10, pady=10, fill='x')

        # Ekran
        self.ekran = tk.Entry(ekran_frame, width=18, font=('Arial', 24), 
                             justify='right', bg="#34495e", fg="white",
                             borderwidth=5, relief='sunken')
        self.ekran.pack(fill='x', padx=5, pady=5)
        
        # Butonlar Frame'i
        buton_frame = tk.Frame(self.pencere, bg="#2c3e50")
        buton_frame.pack(padx=10, pady=5)

        # Butonlar
        butonlar = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Butonları yerleştir
        for i, buton in enumerate(butonlar):
            row = i // 4
            col = i % 4
            command = lambda x=buton: self.tikla(x)
            btn = tk.Button(buton_frame, text=buton, width=6, height=2,
                          font=('Arial', 14, 'bold'), command=command,
                          bg="#3498db", fg="white", activebackground="#2980b9",
                          relief='raised', borderwidth=3)
            btn.grid(row=row, column=col, padx=5, pady=5)
        
        # Temizle butonu
        tk.Button(buton_frame, text="C", width=6, height=2,
                 font=('Arial', 14, 'bold'), command=self.temizle,
                 bg="#e74c3c", fg="white", activebackground="#c0392b",
                 relief='raised', borderwidth=3).grid(row=4, column=0, padx=5, pady=5)

    def tikla(self, deger):
        if deger == '=':
            self.hesapla()
        else:
            mevcut = self.ekran.get()
            self.ekran.delete(0, tk.END)
            self.ekran.insert(tk.END, mevcut + deger)

    def hesapla(self):
        try:
            ifade = self.ekran.get()
            # Sadece sayılar ve izin verilen operatörler
            if not re.match(r'^[0-9+\-*/.() ]*$', ifade):
                raise ValueError("Geçersiz karakterler!")
            sonuc = eval(ifade, {"__builtins__": None}, {})
            self.ekran.delete(0, tk.END)
            # Sonucu formatla (çok uzun ondalık sayıları kısalt)
            if isinstance(sonuc, float):
                sonuc = '{:.8f}'.format(sonuc).rstrip('0').rstrip('.')
            self.ekran.insert(tk.END, sonuc)
        except Exception as e:
            messagebox.showerror("Hata", f"Geçersiz İşlem! {str(e)}")
            self.ekran.delete(0, tk.END)

    def temizle(self):
        self.ekran.delete(0, tk.END)

    def basla(self):
        self.pencere.mainloop()

# Konsol versiyonu
def konsol_hesap_makinesi():
    print("Basit Hesap Makinesi")
    print("İşlemler: +, -, *, /")
    print("Çıkış için 'q' yazın")
    
    while True:
        islem = input("\nİşlemi girin (örn: 2 + 2): ")
        
        if islem.lower() == 'q':
            print("Hesap makinesi kapatılıyor...")
            break
            
        try:
            # Sadece sayılar ve izin verilen operatörler
            if not re.match(r'^[0-9+\-*/.() ]*$', islem):
                raise ValueError("Geçersiz karakterler!")
            sonuc = eval(islem, {"__builtins__": None}, {})
            print(f"Sonuç: {sonuc}")
        except Exception as e:
            print(f"Geçersiz işlem! {str(e)}")

if __name__ == "__main__":
    secim = input("Hangi versiyonu kullanmak istersiniz? (1: GUI, 2: Konsol): ")
    
    if secim == "1":
        hesap_makinesi = HesapMakinesi()
        hesap_makinesi.basla()
    elif secim == "2":
        konsol_hesap_makinesi()
    else:
        print("Geçersiz seçim!") 