# 파일 닫는 3가지 방법

# 1.. close()
# 단점은 파일을 가지고 작업하다가 에러가 발생하면 파일이 제대로 닫히지 않는 경우가 발생한다.
file = open('/Users/yeongroksong/Desktop/test.txt','r')
line = file.readline().rstrip()
print(line)
# print(dder) >>> error / file.close() 명령어 실행전에 에러가 나면 file.close() 명령어가 실행되지 않는다.
file.close()

# 2. try-finally
try:
    file = open('/Users/yeongroksong/Desktop/test.txt','r')
    line = file.readline().rstrip()
    print(line)
    # print(eeeee) >>> error
finally: # trt에서 오류가 나도 finally는 무조건 실행되기 때문에 1번보다 안전한 벙법이다
    print('finally')
    file.close()
    
# 3. with 명령문, with 명령문 내의 블록이 종료될 때 파일이 자동으로 닫힌다.
# close() 내부적으로 호출이 된다.(권장 방법)
with open('/Users/yeongroksong/Desktop/test.txt','r') as file:
    line = file.readline().rstrip()
    print(line)