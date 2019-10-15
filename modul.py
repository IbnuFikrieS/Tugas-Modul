import math
class pesawat(object):
    def __init__(self, r, t, k, w):
        self.jari = r
        self.tinggi = t
        self.tipe = k
        self.warna = w

    def hitungvolume(r, t):
      return math.pi * r * r * t

    def cetakdata(self):
      print("Jari-Jari: ", self.jari)
      print("Tinggi\t: ", self.tinggi)
      print("Tipe\t: ", self.tipe)
      print("warna\t: ", self.warna)



class radio(object):
    def __init__(self, a, g, r, y, n):
        self.panjang = a
        self.lebar = g
        self.tinggi = r
        self.merk = y
        self.warna = n

    def hitungvolume(a, g, r):
      return a * g * r

    def cetakdata(self):
      print("panjang\t: ", self.panjang)
      print("lebar\t: ", self.lebar)
      print("Tinggi\t: ", self.tinggi)
      print("Merek\t: ", self.merk)
      print("warna\t: ", self.warna)



class bola(object):
    def __init__(self, i, b, e, n):
        self.jari = i
        self.jenis = b
        self.kuantitas = e
        self.warna = n

    def hitungvolume(i):
      return 4/3 * math.pi * i * i * i

    def cetakdata(self):
      print("Jari-Jari: ", self.jari)
      print("Jenis\t: ", self.jenis)
      print("Kuantitas: ", self.kuantitas)
      print("warna\t: ", self.warna)












