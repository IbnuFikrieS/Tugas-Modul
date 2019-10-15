import modul

def main():
    #pesawat
    r = int(input("Masukkan Nilai Jari-jari: "))
    t = int(input("Masukkan Nilai Tinggi: "))
    k = "Boeing 707"
    w = "Putih-Biru"

    pesawat = modul.pesawat(r,t,k,w)
    volume = modul.pesawat.hitungvolume(r,t)

    print("\nPesawat")
    print("Jari-jari: ", r)
    print("Tinggi\t: ", t)
    print("Tipe\t: ", k)
    print("Warna\t: ", w)
    print("Volume\t: ", volume)


    print("\n")
    #radio
    a = int(input("Masukkan Nilai Panjang: "))
    g = int(input("Masukkan Nilai Lebar: "))
    r = int(input("Masukkan Nilai Tinggi: "))
    y = "Philips-007"
    n = "Pink"

    radio = modul.radio(a,g,r,y,n)
    volume = modul.radio.hitungvolume(a,g,r)

    print("\nRadio")
    print("Panjang\t: ", a)
    print("Lebar\t: ", g)
    print("Tinggi\t: ", r)
    print("Merek\t: ", y)
    print("Warna\t: ", n)
    print("Volume\t: ", volume)


    print("\n")
    #bola
    i = int(input("Masukkan Nilai Jari-jari: "))
    b = "Bola Kulit"
    e = "4"
    n = "Merah-Kuning"

    bola = modul.bola(i,b,e,n)
    volume = modul.bola.hitungvolume(i)

    print("\nBola")
    print("Jari-jari: ", i)
    print("jenis\t: ", b)
    print("Kuantitas: ", e)
    print("Warna\t: ", n)
    print("Volume\t: ", volume)

if __name__ == "__main__":
   main()
