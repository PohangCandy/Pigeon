import requests
from bs4 import BeautifulSoup
import json

keyword = "부천시 소서구 옥길동"

url = "https://new.land.naver.com/complexes/101778?ms=37.452181,126.7566736,18&a=APT:PRE&e=RETAIL"
res = requests.get(url)
res.raise_for_status()

soup = str(BeautifulSoup(res.text, "lxml"))

# "filter: {" 문자열이 존재하는지 확인
if "filter: {" in soup:
    value = soup.split("filter: {")[1].split("}")[0].replace(" ","").replace("'","")

    lat = value.split("lat:")[1].split(",")[0]
    lon = value.split("lon:")[1].split(",")[0]
    z = value.split("z:")[1].split(",")[0]
    cortarNo = value.split("cortarNo:")[1].split(",")[0]
    rletTpCds = value.split("rletTpCds:")[1].split(",")[0]
    tradTpCds = value.split("tradTpCds:")[1].split()[0]

    # lat - btm : 37.550985 - 37.4331698 = 0.1178152
    # top - lat : 37.6686142 - 37.550985 = 0.1176292
    lat_margin = 0.118

    # lon - lft : 126.849534 - 126.7389841 = 0.1105499
    # rgt - lon : 126.9600839 - 126.849534 = 0.1105499
    lon_margin = 0.111

    btm = float(lat) - lat_margin
    lft = float(lon) - lon_margin
    top = float(lat) + lat_margin
    rgt = float(lon) + lon_margin

    # 최초 요청 시 디폴트 값으로 설정되어 있으나, 원하는 값으로 구성
    rletTpCds = "SG"  # 상가
    tradTpCds = "A1:B1:B2"  # 매매/전세/월세 매물 확인
else:
    print("필터 데이터를 찾을 수 없습니다.")
