import requests
import locale
locale.setlocale(locale.LC_ALL,'')
def mainmenu():
    menu = True
    bank = input('Silahkan ketik nama bank: ')
    url1 = 'https://kurs.web.id/api/v1/' +bank.lower()
    data1 = requests.get(url1)
    mata_uang = data1.json()
    konverter = int(mata_uang['jual'])
    url2 = 'https://blockchain.info/ticker'
    data2 = requests.get(url2)
    bit = data2.json()
    bit_usd = bit['USD']['buy']
    if mata_uang['error'] =='true':
        print('Input error, silahkan masukkan nama bank lain')
    else:
        while (menu <= 6):
            menu1 = int(input('nAPLIKASI KONVERSI MATA UANG\nSILAHKAN PILIH MATA UANG YANG INGIN DIKONVERSI: \n 1. IDR\n 2. USD\n 3. Bitcoin\n Masukkan pilihan: '))
            if menu1 == 1:
                menu2 = int(input('\nKonversi IDR ke: \n 1. USD\n 2. Bitcoin\n Masukkan pilihan: '))
                if menu2 == 1:
                    menu = 1
                elif menu2 == 2:
                    menu = 2
            elif menu1 == 2:
                menu2 == int(input('\nKonversi USD ke: \n 1. IDR\n 2. Bitcoin\n Masukkan pilihan: '))
                if menu2 == 1:
                    menu = 3
                elif menu2 == 2:
                    menu = 4
            elif menu1 == 3:
                menu2 = int(input('\nKonversi Bitcoin ke: \n 1. IDR\n 2. USD\n Masukkan pilihan: '))
                if menu2 == 1:
                    menu = 5
                elif menu2 == 2:
                    menu = 6
            else:
                print('Terimakasih')
                break
            
            if menu == 1:
                nilai = int(input('Masukkan jumlah nominal: IDR'))
                konversi = nilai/konverter
                print('\nHasil konversi dari IDR {:n} adalah USD {:n} \n Dengan nilai kurs jual {:n} dan kurs beli {:n} yang dikeluarkan oleh bank {} pada {}'.format(nilai,round(konversi,2),int(mata_uang['jual']),int(mata_uang['beli']),mata_uang['bank'],mata_uang['timestamp']))
            elif menu == 2:
                nilai = int(input('Silahkan input nominal uang yang akan di konversi : IDR '))
                konversi = nilai/konverter/bit_usd
                print('\nHasil konversi dari IDR {:n} adalah Bitcoin {} \nDengan nilai kurs jual {:n} dan kurs beli {:n} pada {}'.format(nilai,round(konversi,2),bit_usd,bit_usd,mata_uang['timestamp']))
            elif menu == 3:
                nilai = int(input('Silahkan input nominal uang yang akan di konversi : USD '))
                konversi = nilai*konverter
                print('\nHasil konversi dari USD {:n} adalah IDR {:n} \nDengan nilai kurs jual {:n} dan kurs beli {:n} yang dikeluarkan oleh Bank {} pada {}'.format(nilai,konversi,int(mata_uang['jual']),int(mata_uang['beli']),mata_uang['bank'],mata_uang['timestamp']))
            elif menu == 4:
                nilai = int(input('Silahkan input nominal uang yang akan di konversi : USD '))
                konversi = nilai/bit_usd
                print('\nHasil konversi dari USD {:n} adalah Bitcoin {:n} \nDengan nilai kurs jual {:n} dan kurs beli {:n} pada {}'.format(nilai,konversi,bit_usd,bit_usd,mata_uang['timestamp']))
            elif menu == 5:
                nilai = int(input('Silahkan input nominal uang yang akan di konversi : Bitcoin '))
                konversi = nilai*bit_usd*konverter
                print('\nHasil konversi dari Bitcoin {:n} adalah IDR {:n} \nDengan nilai kurs jual {:n} dan kurs beli {:n} pada {}'.format(nilai,konversi,bit_usd,bit_usd,mata_uang['timestamp']))
            elif menu == 6:
                nilai = int(input('Silahkan input nominal uang yang akan di konversi : Bitcoin '))
                konversi = nilai*bit_usd
                print('\nHasil konversi dari Bitcoin {:n} adalah USD {:n} \nDengan nilai kurs jual {:n} dan kurs beli {:n} pada {}'.format(nilai,konversi,bit_usd,bit_usd,mata_uang['timestamp']))
            else:
                print('Thank you for using our services!')

mainmenu()



