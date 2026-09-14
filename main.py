import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import os

# Tema ve Renk Ayarları
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class SporGunluguApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Emojimin Spor Günlüğü ❤️")
        self.geometry("600x730")
        self.resizable(False, False)

        # 1. Başlık ve Kalp Alanı (Ortalama Düzeltildi)
        self.header_label = ctk.CTkLabel(
            self,
            text="❤️ Emojimin Spor Günlüğü ❤️",
            font=ctk.CTkFont(size=24, weight="bold"),
            anchor="center"
        )
        self.header_label.pack(pady=(20, 10), fill="x")

        # 2. Fotoğraf Alanı (En Uygun Boyut: 160x200 dikey oran)
        # fotografimiz.jpg veya fotografimiz.png ikisini de kontrol eder
        foto_yolu = None
        if os.path.exists("fotografimiz.jpg"):
            foto_yolu = "fotografimiz.jpg"
        elif os.path.exists("fotografimiz.png"):
            foto_yolu = "fotografimiz.png"

        if foto_yolu:
            img = Image.open(foto_yolu)
            # Dikey fotoğraf için oran koruyarak boyutlandırma (En: 160, Boy: 200)
            img = img.resize((160, 200), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            self.img_label = tk.Label(self, image=self.photo, bg="#1a1a1a")
            self.img_label.pack(pady=10)
        else:
            self.no_img_label = ctk.CTkLabel(
                self,
                text="[ Bizim Fotoğrafımız ]\n(Klasöre 'fotografimiz.jpg' ekleyin)",
                font=ctk.CTkFont(size=12, slant="italic")
            )
            self.no_img_label.pack(pady=10)

        # 3. Giriş Formu
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(padx=20, pady=10, fill="x")

        self.gun_label = ctk.CTkLabel(self.form_frame, text="Gün / Tarih:")
        self.gun_label.pack(anchor="w", padx=10, pady=(10, 0))
        self.gun_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Örn: Pazartesi / 14 Eylül")
        self.gun_entry.pack(fill="x", padx=10, pady=(0, 10))

        self.spor_label = ctk.CTkLabel(self.form_frame, text="Yapılan Antrenman:")
        self.spor_label.pack(anchor="w", padx=10, pady=(5, 0))
        self.spor_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Örn: Bacak & Kardiyo, 45 dk")
        self.spor_entry.pack(fill="x", padx=10, pady=(0, 10))

        # Kaydet Butonu
        self.kaydet_btn = ctk.CTkButton(
            self,
            text="Günlüğü Kaydet 💪❤️",
            command=self.gunluk_ekle,
            fg_color="#e91e63",
            hover_color="#c2185b"
        )
        self.kaydet_btn.pack(pady=10)

        # 4. Kayıtlı Günlük Listesi
        self.liste_label = ctk.CTkLabel(self, text="Geçmiş Antrenmanlar:", font=ctk.CTkFont(size=16, weight="bold"))
        self.liste_label.pack(anchor="w", padx=25, pady=(10, 5))

        self.textbox = ctk.CTkTextbox(self, width=550, height=180)
        self.textbox.pack(padx=20, pady=(0, 20))

        self.eski_kayitlari_yukle()

    def eski_kayitlari_yukle(self):
        if os.path.exists("spor_gunlugu.txt"):
            with open("spor_gunlugu.txt", "r", encoding="utf-8") as file:
                icerik = file.read()
                self.textbox.insert("1.0", icerik)
        self.textbox.configure(state="disabled")

    def gunluk_ekle(self):
        gun = self.gun_entry.get().strip()
        spor = self.spor_entry.get().strip()

        if not gun or not spor:
            messagebox.showwarning("Eksik Bilgi", "Lütfen hem günü hem de yapılan sporu girin!")
            return

        yeni_kayit = f"🗓️ {gun} ➔ 🏋️ {spor}\n" + ("-" * 50) + "\n"

        self.textbox.configure(state="normal")
        self.textbox.insert("1.0", yeni_kayit)
        self.textbox.configure(state="disabled")

        with open("spor_gunlugu.txt", "a", encoding="utf-8") as file:
            file.write(yeni_kayit)

        self.gun_entry.delete(0, 'end')
        self.spor_entry.delete(0, 'end')


if __name__ == "__main__":
    app = SporGunluguApp()
    app.mainloop()