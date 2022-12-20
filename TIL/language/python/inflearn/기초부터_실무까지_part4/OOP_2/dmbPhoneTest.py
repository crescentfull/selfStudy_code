# phone class + dmb class main code

from dmbPhone import *

if __name__ == "__main__":
    # 자식 클래스 인스턴스 생성
    dmbPhone = DmbPhone("python", "black", 10)
    
    # 조상클래스 상속필드
    print("모델 : ", dmbPhone.model)
    print("색상 : ", dmbPhone.color)
    # 자식클래스 필드
    print("채널 : ", dmbPhone.channel)
    
    dmbPhone.powerOn()
    dmbPhone.bell()
    dmbPhone.sendVoice("여보세요")
    dmbPhone.receiveVoice("안녕하세요! 저는 아무개입니다")
    dmbPhone.sendVoice("안녕하세요! 저는 누구에요")
    dmbPhone.hangUp()
    print('*'*40)
    # 자식클래스에서 만든 dmb 기능
    dmbPhone.trunOnDmb()
    dmbPhone.changeChannelDmb(15)
    dmbPhone.turnOffDmb()