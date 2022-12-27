# ContentSender, kakaoSender, SmsSender 클래스의 실행파일

from KakaoSender import *
from SmsSender import *

if __name__ == "__main__":
    cs1 = KakaoSender("카카오톡","ㅇㅇ","100만")
    cs1.sendMsg("송영록")
    print("-"*40)
    cs2 = SmsSender("SMS 문자", "ㄷㄷ", "고마워")
    cs2.sendMsg("송어어")