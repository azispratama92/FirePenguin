# ---------------------------------------------
# Author: Azis R. Pratama
#
# Creation date: 16 August 2017
#
# Description: Script bash untuk autologin dan re-connect jaringan wifi-ID
#				
# ---------------------------------------------
echo ===================================================== 
echo Menghubungkan Komputer dengan Jaringan Wifi ID
echo ===================================================== 
sleep 01
nmcli con up @wifi.id
sleep 01
echo ===================================================== 
echo Autentifikasi Pengguna ........
echo =====================================================
python wifi-id.py
sleep 03
echo ===================================================== 
echo Melakukan Ping otomatis ke URL wifi.id
echo =====================================================
echo                                                      
ping wifi.id
