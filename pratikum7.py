import tkinter as tk #membuat grafis
 
 # Menampilkan hasil prediksi pada label hasil
def show_prediction():
    result_label.config(text="Program Studi: Teknologi Informasi")

root = tk.Tk()#membuat jendela aplikasi utama
root.title("Aplikasi Prediksi Prodi Pilihan")#membuat judul

title_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 10))#menampilkan teks 'aplikasi prediksi prodi pilihan'
title_label.grid(row=0, column=0, columnspan=2, pady=5)

entry_fields = []#membuat list kosong
for i in range(10):
    subject_label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")#label untuk stiap input
    subject_label.grid(row=i+1, column=0, padx=5, pady=5, sticky="e")#menempatkan label
    entry = tk.Entry(root)#membuat kolom input
    entry.grid(row=i+1, column=1, padx=5, pady=5)
    entry_fields.append(entry)#menambahkan referensi

predict_button = tk.Button(root, text="Hasil Prediksi", command=show_prediction)#menjalankan fungsi show_prediction
predict_button.grid(row=11, column=0, columnspan=2, pady=5)

result_label = tk.Label(root, text="Luaran hasil prediksi akan muncul di sini", font=("Arial", 8))#membuat label hasil prediksi
result_label.grid(row=12, column=0, columnspan=2, pady=10)

root.mainloop()#menjalankan aplikasi
