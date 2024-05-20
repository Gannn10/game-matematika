""" Data.py -> all data like view and category """

def DataView():
  return [
    'Mudah',
    'Sedang',
    'Sulit',
    'Advanced Mode',
    'Practice Mode',
  ]

def Quotes():
  return {
    # List Ucapan 
    # kategori > 80
    'kategoriBaik' : [
        'Kamu Orang Yg Pintar, Pertahankan!',
        'Wah , Kamu Hebat Sekali !!',
        'Jawaban Kamu Diatas rata-rata',
        'Kamu Bisa Menjadi Seperti Einstein',
        'Orang Tua Mu Bangga Punya Anak Seperti Mu',
        'Rahasia Kamu Apa Sih , Jago Banget Matematikanya',
        'Aku Tak Pernah Bertemu Orang Seperti mu!!, Hebat',
        'Ajari Aku Dong!! , Kamu Pintar Sekali',
        'Gak Ada Yang Bisa Ngalahin Kamu !!'
    ],
    # kategori 50 > nilai < 75
    'kategoriCukup' : [
        'Oke Lumayan Untuk Kamu',
        'Jangan Langsung Berbangga Diri yah Ini Belum Seberapa',
        'Aku Yakin Kamu bisa lebih baik dari ini',
        'Dapet Nilai B , itu bagus loh',
        'Sedikit Lagi Mencapai Keberhasilan',
        'Tetap Semangat Yah !!',
        'Terus Belajar & raih Kategori A'
    ],
    # kategori < 45
    'kategoriBuruk' : [
        'Yah , Semangat Terus Deh Buat Kamu',
        'Ayo Kamu Pasti Bisa',
        'Mungkin Kamu Masih Belum terbiasa ya !!',
        'Jangan Mengganggap Diri Kamu Bodoh',
        'Jangan Berkecil Hati Dengan Apa Yg Kamu Dapatkan Sekarang',
        'Tetap Belajar Dan Ubah Kelemahan Menjadi Kelebihanmu',
        'Jangan Patah Semangat Ya'
    ]
  }