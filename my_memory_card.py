from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QRadioButton
from random import shuffle, randint


""" BUAT OBJEK """
aplikasi = QApplication([])
jendela_utama = QWidget()
jendela_utama.setWindowTitle("QUIZ-WINDOWZ")
jendela_utama.resize(350, 250)


""" BUAT OBJEK WIDGET BAGIAN DUA """
pertanyaan = QLabel("SUDAH MAKAN BELUM?")
tombol_aja = QPushButton("JAWAB")
radio_btn1 = QRadioButton("BELUM")
radio_btn2 = QRadioButton("SUDAH")
radio_btn3 = QRadioButton("BELUM 2 KALI")
radio_btn4 = QRadioButton("KEMARIN SUDAH")
radio_grupbox = QGroupBox("PILIHAN JAWABAN")
hasil_grupbox = QGroupBox("HASILNYA") ## INI GRUP BOX UNTUK HASIL JAWABAN
benarsalah = QLabel("BENAR / SALAH")
jawaban = QLabel("JAWABAN YANG BENAR")


""" MEMBUAT KELAS PERTANYAAN """
class Question:
    def __init__(self, pertanyaan, benar, salah1, salah2, salah3):
        self.pertanyaan = pertanyaan
        self.benar = benar
        self.salah1 = salah1
        self.salah2 = salah2
        self.salah3 = salah3


""" MEMBUAT LIST KUMPULAN PERTANYAAN """
LIST_PERTANYAAN = list()
LIST_PERTANYAAN.append(Question("Handphone pertama di dunia", "Motorola", "Iphone", "Nokia", "Ericsson"))
LIST_PERTANYAAN.append(Question("Jamur yang aman dimakan?", "Tiram", "Fly Agaric", "False Parasol", "Galerina marginata"))
LIST_PERTANYAAN.append(Question("Berapa jarak Bulan dari bumi?", "384.400km", "100.000km", "1km", "698.200km"))
LIST_PERTANYAAN.append(Question("Gunung tertinggi di dunia?", "Gunung Everest", "Gunung K2", "Gunung Kangchenjunga", "Gunung Lhotse"))
LIST_PERTANYAAN.append(Question("Os Windows paling pertama?", "Windows 1.0 (1985)", "Windows XP (2001)", "Windows 7 (2009)", "Windows 10 (2015)"))

""" BUAT TAMPILAN UNTUK RADIO GRUP BOX PILIHAN JAWABAN NYA"""
garisv_grupbox = QVBoxLayout()
garish1_grupbox = QHBoxLayout()
garish2_grupbox = QHBoxLayout()
garish1_grupbox.addWidget(radio_btn1)
garish1_grupbox.addWidget(radio_btn2)
garish2_grupbox.addWidget(radio_btn3)
garish2_grupbox.addWidget(radio_btn4)
garisv_grupbox.addLayout(garish1_grupbox)
garisv_grupbox.addLayout(garish2_grupbox)
radio_grupbox.setLayout(garisv_grupbox) ## ATUR TAMPILAN UTAMA RADIO GRUPBOX


""" BUAT TAMPILAN UNTUK HASIL GRUP BOX """
garisv_hasilgrupbox = QVBoxLayout()
garisv_hasilgrupbox.addWidget(benarsalah)
garisv_hasilgrupbox.addWidget(jawaban, alignment=Qt.AlignHCenter)
hasil_grupbox.setLayout(garisv_hasilgrupbox) ## ATUR TAMPILAN UTAMA HASIL GRUPBOX


""" BUAT TAMPILAN UTAMA APLIKASI """
garisv_utama = QVBoxLayout()
garisv_utama.addWidget(pertanyaan, alignment=Qt.AlignHCenter)
garisv_utama.addWidget(radio_grupbox)
garisv_utama.addWidget(hasil_grupbox) ## MENAMPILKAN HASIL GRUP BOX
garisv_utama.addWidget(tombol_aja)


""" TAMPIL/SEMBUNYIKAN """
radio_grupbox.show()
hasil_grupbox.hide()


""" MEMBUAT GRUP TOMBOL """
pilihan_grup = QButtonGroup()
pilihan_grup.addButton(radio_btn1)
pilihan_grup.addButton(radio_btn2)
pilihan_grup.addButton(radio_btn3)
pilihan_grup.addButton(radio_btn4)


""" MEMBUAT FUNGSI UNTUK EVENT HANDLER """
jendela_utama.jumlah_benar = 0
jendela_utama.jumlah_soal = 0
def show_result():
    radio_grupbox.hide()
    hasil_grupbox.show()
    tombol_aja.setText("lanjut soal")
    print(" ")
    print("[ STATS ]")
    print(">>")
    print("total soal:", jendela_utama.jumlah_soal)
    print("total jawaban benar:", jendela_utama.jumlah_benar)
    print("Rate:",(jendela_utama.jumlah_benar/jendela_utama.jumlah_soal)*100, "%")

def show_question():
    pilihan_grup.setExclusive(False)
    radio_btn1.setChecked(False)
    radio_btn2.setChecked(False)
    radio_btn3.setChecked(False)
    radio_btn4.setChecked(False)
    pilihan_grup.setExclusive(True)


    radio_grupbox.show()
    hasil_grupbox.hide()
    tombol_aja.setText("Jawab")


""" LANJUTANNYA """
LIST_PILIHAN = [radio_btn1, radio_btn2, radio_btn3, radio_btn4]
def tanya(pertanyaannya): ## ini kita ubah untuk part 3
    shuffle(LIST_PILIHAN)
    LIST_PILIHAN[0].setText(pertanyaannya.benar)
    LIST_PILIHAN[1].setText(pertanyaannya.salah1)
    LIST_PILIHAN[2].setText(pertanyaannya.salah2)
    LIST_PILIHAN[3].setText(pertanyaannya.salah3)
    pertanyaan.setText(pertanyaannya.pertanyaan)
    jawaban.setText(pertanyaannya.benar)
    show_question() ## tambah ini


def klik():
    if tombol_aja.text() == "Jawab":
        check_answer()
    else:
        next_question() ## tambah ini


def check_answer():
    if LIST_PILIHAN[0].isChecked():
        benarsalah.setText("yay! benarr XD")
        jendela_utama.jumlah_benar += 1
    
    else:
        benarsalah.setText("yaahh.. itu salah :(")
    show_result()


#jendela_utama.pertanyaan_saatini = -1
def next_question():
    #jendela_utama.pertanyaan_saatini += 1
    #if jendela_utama.pertanyaan_saatini == len(LIST_PERTANYAAN):
    #    jendela_utama.pertanyaan_saatini = 0
    #tanya(LIST_PERTANYAAN[jendela_utama.pertanyaan_saatini])
    angka_acak = randint(1, len(LIST_PERTANYAAN)) -1 ## UNTUK DAPAT NOMOR INDEXNYA
    tanya(LIST_PERTANYAAN[angka_acak])
    jendela_utama.jumlah_soal += 1

next_question()
""" EVENT HANDLER """
tombol_aja.clicked.connect(klik) ## hubungkan dengan tombol






""" TAMPILKAN APLIKASI DAN JENDELA """
jendela_utama.setLayout(garisv_utama) ## ATUR TAMPILAN UTAMA JENDELA
jendela_utama.show()
aplikasi.exec_()