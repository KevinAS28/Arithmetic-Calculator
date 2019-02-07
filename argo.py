#!/usr/bin/python

import os
import math

kalkulator = "y"

while(kalkulator=='y'):
 
 print """  

  ___________________________________
 |                                  |
 |    ini adalah kalkulator         |
 |    untuk menghitung              |
 |    barisan,deretan geometri dan  |
 |    aritmetika                    |
 |                                  |
 |                                  |
 |                                  |
 |                                  |
 |-----------------------------------

ketik nomor untuk memilih:

1.menghitung barisan aritmetika

2.menghitung barisan geometri

3.mengihtung deretan aritmetika

4.menghitung deretan geometri

5.contoh soal barisan aritmetika

6.contoh soal barisan geometri

7.contoh soal deretan aritmetika

8.contoh soal deretan geometri


 """
 
 pilihmenu = input("pilihan mu? ")
 
  
 #barisan aritmetika
 if (pilihmenu==1):
  print """
   
   anda akan mencari b atau n dari aritmetika
   
   rumus : a + (n-1) x b
  
   ket:
   
   a = angka awal/mulai pada barisan
   n = barisan yang ditanya
   b = beda
   
   memilih beda atau banyak
   mencari n atau b?
   
   jika ingin mencari n ketik n
   jika ingin mencari b ketik b
                                  """
  pilihnb = raw_input("cari b atau n? ")

  if (pilihnb=="n"):
   print """
    anda akan mencari suku ke-n dalam sebuah barisan airtmetika
         """
   sukuaa = int(raw_input("suku mula-mula? "))
   sukuna = int(raw_input("suku ke/yang dicari? "))
   bedaa = int(raw_input("beda? "))
   hasilaa = int(sukuna-1)
   hasilab = int(hasilaa*bedaa)
   hasilac = int(sukuaa+hasilab)
   #print(hasilac)
   tmbh = "+"
   kali = "x"
   rumusa = "a"
   rumusn = "n"
   krng = "-"
   rumusb = "b"
   print("langkah-langkah mengetahui n")
   print("rumusnya a + (n-1) x b")
   print("maka :")
   print(" ")
   print(str(sukuaa)+tmbh+str(hasilaa)+kali+str(bedaa))
   print("hasilnya adalah"+(" ")+str(hasilac))
   print(" ")
   
   

  if (pilihnb=="b"):
   print """ untuk mencari beda pada barisan aritmetika,tinggal mengkurangkan saja"
   cariba = raw_input(" ")
   print(cariab)
  
# if (pilihmenu==2):
#  print """
#    anda akan mencari suku ke-n dalam sebuah barisan geometri
#    
#    rumusnya
#    
#    a x r(pangkat)n-1 
#
#    sebelum anda mencari suku ke-n,anda harus mencari rasio terlebih dahulu
#    
#    tekan n untuk lanjut
#    """
#  menugeo = raw_input("pilihan mu? ")
#  if (menugeo=="n"):
#   print """
# ada beberapa macam soal tentang barisan geometri,seperti
#
# sebuah tali yang dipotong potong atau suku ke-.. suku ke-.. maka suku ke-..
#
# jika soalnya tentang tali,ketik t
# jika soalnya tentang suku-suku,ketik s
#"""
#   menugeoa = str(raw_input("pilihan mu? "))
#   
#   if (menugeoa=="t")
#    
 if (pilihmenu==10):
  testt=os.system("ls -l")
  print testt
 
 kalkulator = raw_input("mulai program lagi? Y/N ")