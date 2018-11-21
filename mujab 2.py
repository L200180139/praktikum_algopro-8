a={'nim':'139','nama':'mujab','alamat':'Rembang','status':'mahasiswa','hobi':'olahraga','makanan':'nasi_dan_lauknya','pacar':'apa_itu'}
def nim():
    print 'nim',a['nim']
def nama():
    print 'nama',a['nama']
def alamat():
    print 'alamat',a['alamat']
def status():
    print 'status',a['status']
def hobi():
    print 'hobi',a['hobi']
def cita():
    print 'makanan',a['makanan']
def istri():
    print 'pacar',a['pacar']
def pilihan():
    print 'pilihan yang tersedia:'
    print 'b menampilkan bantuan ini'
    print 'N menampilkan nim'
    print 'a menampilkan nama'
    print 'A menampilkan alamat'
    print 'K menampilkan hobi'
    print 'x menampilkan makanan'
    print 'X menampilkan status'
    print 'I menampilkan apa_itu'
pilihan()

g=str(raw_input('pilihan saudara:'))
while g != 'p':
    if g == 'a':
        nama()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'b':
        pilihan()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'N':
        nim()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'A':
        alamat()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'K':
        hobi()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'x':
        makanan()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'X':
        status()
        g=str(raw_input('pilihan saudara:'))
    elif g == 'I':
        pacar()
        g=str(raw_input('pilihan saudara:'))

