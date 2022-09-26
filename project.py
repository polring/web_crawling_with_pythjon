import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")



# 1위 - 3위 컨테이너 선택자: div.inner 선택자가 가르키는 모든 데이터를 리스트 형식으로 저장한다.
clips = html.select("div.inner")

for cl in clips:
    title = cl.select_one("dt.title")    #select함수는 데이터 중 첫번째 데이터만 저장하는 함수이다.
    chn = cl.select_one("dd.chn")
    hit = cl.select_one("span.hit")
    like = cl.select_one("span.like")

    print("제목", title.text.strip())
    print("채널명", chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)
    

    
    
# 4위-100위 컨테이너 선택자: 
clips = html.select("div.cds")

for cl in clips:
    title = cl.select_one("dt.title") #select는 결과괎이 리스트로 반환,select_one는 문서의 가장처음 값을 반환
    chn = cl.select_one("dd.chn")
    hit = cl.select_one("span.hit")
    like = cl.select_one("span.like")

    print("제목", title.text.strip())
    print("채널명", chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50) #구분자 
    
    
    

    

    

    
