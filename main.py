import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st



def imsakiye(sehir):
  ramazan=pd.read_html(f'https://www.haberturk.com/ramazan/imsakiye/{sehir}',flavor='bs4')[0] # html sayfasındaki table etiketlerini okur.
  ramazan=ramazan.iloc[0:-1] # 0'dan -1'e kadar satırları alır diğerlerini siler
  ramazan=ramazan.drop(26,axis=0) # 26. satırı siler
  pd.to_datetime(ramazan['Tarih'])
  return ramazan



def iftarKalan(sehir):
  df=imsakiye(sehir) # fonksiyonu bir dataframe'e atarız
  bugun=datetime.today().date().strftime('%Y-%m-%d') # bugünü formatıyla birlikte yazarız
  simdi=datetime.now().time.strftime('%H-%M') # saat ve dakika formatıyla şimdiki zamanı yazarız
  sehirİftar=df[df['Tarih']==bugun]['AKŞAM'].values[0] # tarihi bugüne eşit olan günün AKŞAM'ının değerini gireriz
  kalan=pd.Timedelta(sehirİftar)-pd.Timedelta(simdi) # iftara ne kadar (saat-dakika) kaldığını hesaplarız
  return kalan



def Bugun(sehir):
  df=imsakiye(sehir)
  bugun=datetime.today().date().strftime('%Y-%m-%d')
  sehirİftar=df[df['Tarih']==bugun]
  return sehirİftar


st.header('Hoşgeldin Ramazan')
sehirler=["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]
sehirSec=st.sidebar.selectbox("Şehir seç", sehirler)

sehirSec=sehirSec.upper()
sehirSec=sehirSec.replace("ç","c")
sehirSec=sehirSec.replace("ğ","g")
sehirSec=sehirSec.replace("ö","o")
sehirSec=sehirSec.replace("i","ı")
sehirSec=sehirSec.replace("ç","c")
sehirSec=sehirSec.replace("ş","s")
sehirSec=sehirSec.replace("ü","u")



# st.subheader('İftara kalan süre: ')
# st.write(iftarKalan(sehirSec))
st.subheader('Bugün')
st.table(Bugun(sehirSec))
st.subheader('İmsakiye')
st.table(imsakiye(sehirSec))

