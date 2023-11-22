import tkinter as tk
from tkinter import messagebox
import sqlite3

# Fungsi untuk menentukan prediksi berdasarkan nilai tertinggi
def predict_major(matematika, sejarah, biologi, kedokteran, bahasa_indonesia, kimia, aik, penjas, seni_budaya, bahas_inggris):
    subjects = [mat, phy, chem, bio, indo, eng, hist, geo, econ, socio]
    max_subject_index = subjects.index(max(subjects))

    if max_subject_index == 0:
        return "Matematika"
    elif max_subject_index == 1:
        return "Sejarah"
    elif max_subject_index == 2:
        return "Biologi"
    elif max_subject_index == 3:
        return "Kedokteran"
    elif max_subject_index == 4:
        return "Bahasa Indonesia"
    elif max_subject_index == 5:
        return "Kimia"
    elif max_subject_index == 6:
        return "Aik"
    elif max_subject_index == 7:
        return "Penjas"
    elif max_subject_index == 8:
        return "Seni Budaya"
    elif max_subject_index == 9:
        return "Bahasa Inggris"
    else:
        return "Belum dapat diprediksi"

# Fungsi untuk menambahkan nilai ke dalam database SQLite
def add_data_to_db(name, matematika, sejarah, biologi, kedokteran, bahasa_indonesia, kimia, aik, penjas, seni_budaya, bahas_inggris):
    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        nama_siswa TEXT,
                        matematika INTEGER,
                        sejarah INTEGER,
                        biologi INTEGER,
                        kedokteran INTEGER,
                        bahasa_indonesia INTEGER,
                        kimia INTEGER,
                        aik INTEGER,
                        penjas INTEGER,
                        seni_budaya INTEGER,
                        bahas_inggris INTEGER,
                        prediksi_fakultas TEXT)''')

    # Menambahkan data ke dalam tabel
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, matematika, fisika, kimia, biologi, bahasa_indonesia, 
        bahasa_inggris, sejarah_indonesia, geografi, ekonomi, sosiologi, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, mat, phy, chem, bio, indo, eng, hist, geo, econ, socio, prediction))

    conn.commit()
    conn.close()

# Fungsi yang dijalankan ketika tombol submit ditekan
def submit_button_pressed():
    name = entry_nama.get()
    matematika = int(entry_mat.get())
    sejarah = int(entry_phy.get())
    biologi = int(entry_chem.get())
    kedokteran = int(entry_bio.get())
    bahasa_indonesia = int(entry_indo.get())
    kimia = int(entry_eng.get())
    aik = int(entry_hist.get())
    penjas = int(entry_geo.get())
    seni_budaya = int(entry_econ.get())
    bahasa_inggris = int(entry_socio.get())

    prediction = predict_major(matematika, sejarah, biologi, kedokteran, bahasa_indonesia, kimia, aik, penjas, seni_budaya, bahas_inggris)
    
    # Menampilkan hasil prediksi
    messagebox.showinfo("Prediksi Fakultas", f"Prediksi fakultas untuk {name}: {prediction}")

    # Menambahkan data ke dalam database
    add_data_to_db(name, matematika, sejarah, biologi, kedokteran, bahasa_indonesia, kimia, aik, penjas, seni_budaya, bahas_inggris)

# Membuat GUI dengan Tkinter
root = tk.Tk()
root.title("Prediksi Fakultas")

# Membuat label dan entry untuk nama siswa
label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

# Membuat label dan entry untuk nilai Matematika
label_matematika = tk.Label(root, text="Nilai Matematika:")
label_matematika.pack()
entry_matematika = tk.Entry(root)
entry_matematika.pack()

# Membuat label dan entry untuk nilai Fisika
label_sejarah = tk.Label(root, text="Nilai Sejarah:")
label_sejarah.pack()
entry_sejarah = tk.Entry(root)
entry_sejarah.pack()

# Membuat label dan entry untuk nilai Kimia
label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

# Membuat label dan entry untuk nilai Biologi
label_kedokteran = tk.Label(root, text="Nilai Kedokteran:")
label_kedokteran.pack()
entry_kedokteran = tk.Entry(root)
entry_kedokteran.pack()

# Membuat label dan entry untuk nilai Bahasa Indonesia
label_bahasa_indoonesia = tk.Label(root, text="Nilai Bahasa Indonesia:")
label_bahasa_indoonesia.pack()
entry_bahasa_indoonesia = tk.Entry(root)
entry_bahasa_indoonesia.pack()

# Membuat label dan entry untuk nilai Bahasa Inggris
label_kimia = tk.Label(root, text="Nilai Kimia:")
label_kimia.pack()
entry_kimia = tk.Entry(root)
entry_kimia.pack()

# Membuat label dan entry untuk nilai Sejarah Indonesia
label_aik = tk.Label(root, text="Nilai Aik:")
label_aik.pack()
entry_aik = tk.Entry(root)
entry_aik.pack()

# Membuat label dan entry untuk nilai Geografi
label_penjas = tk.Label(root, text="Nilai Penjas:")
label_penjas.pack()
entry_penjas = tk.Entry(root)
entry_penjas.pack()

# Membuat label dan entry untuk nilai Ekonomi
label_seni_budaya = tk.Label(root, text="Nilai Seni Budaya:")
label_seni_budaya.pack()
entry_seni_budaya = tk.Entry(root)
entry_seni_budaya.pack()

# Membuat label dan entry untuk nilai Sosiologi
label_bahasa_inggris = tk.Label(root, text="Nilai Bahasa Inggris:")
label_bahasa_inggris.pack()
entry_bahasa_inggris = tk.Entry(root)
entry_bahasa_inggris.pack()

# Membuat tombol submit
button_submit = tk.Button(root, text="Submit", command=submit_button_pressed)
button_submit.pack()

root.mainloop()
