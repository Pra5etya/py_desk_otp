import sqlite3
from tkinter import *
from vonage import Client

# Inisialisasi Tkinter
root = Tk()
root.title("Registrasi Nomor Handphone")

# Koneksi ke database SQLite
conn = sqlite3.connect('nomor_telepon.db')
c = conn.cursor()

# Buat tabel jika belum ada
c.execute('''CREATE TABLE IF NOT EXISTS nomor_telepon
             (id INTEGER PRIMARY KEY,
              nomor TEXT NOT NULL UNIQUE)''')
conn.commit()

# Fungsi untuk menambahkan nomor telepon ke database
def tambah_nomor():
    nomor_telepon = entry_nomor.get()

    # Tambahkan nomor telepon ke database
    c.execute("INSERT INTO nomor_telepon (nomor) VALUES (?)", (nomor_telepon,))
    conn.commit()

    # Kirim kode verifikasi ke nomor telepon menggunakan Vonage API
    vonage = Client(key='YOUR_VONAGE_API_KEY', secret='YOUR_VONAGE_API_SECRET')
    vonage.verify.start({'number': nomor_telepon, 'brand': 'YourApp'})

    label_status.config(text="Nomor telepon berhasil terdaftar dan kode verifikasi telah dikirim.")

# Antarmuka pengguna dengan Tkinter
label_nomor = Label(root, text="Masukkan Nomor Handphone:")
label_nomor.grid(row=0, column=0, padx=10, pady=10)

entry_nomor = Entry(root, width=20)
entry_nomor.grid(row=0, column=1, padx=10, pady=10)

button_tambah = Button(root, text="Tambahkan", command=tambah_nomor)
button_tambah.grid(row=1, column=0, columnspan=2, pady=10)

label_status = Label(root, text="")
label_status.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

# Tutup koneksi database saat aplikasi ditutup
conn.close()
