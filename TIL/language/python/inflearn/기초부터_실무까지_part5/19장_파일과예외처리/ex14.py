# # 정수를 받고자 할때의 예외처리
# try:
#     n = int(input("숫자를 입력하세요 : "))
# except ValueError:
#     print("정수가 아닙니다")

# 파일의 대한 예외처리
# infile = None
# try:
#     fname = input('파일 이름을 입력하세요 : ')
#     infile = open(fname, 'r')
# except FileNotFoundError:
#     print('해당하는 파일이 존재하지 않습니다.')
# finally:
#     infile.close() # try를 못거치고 예외처리가 되었기 때문에 finally가 실행되지 않는다

infile = None
try:
    infile = open('files/test.txt', 'r')
    print("파일을 열었습니다")
except FileNotFoundError:
    print('해당하는 파일이 없습니다.')
else:
    print("파일을 성공적으로 열람하였습니다.")



# 강제로 예외를 발생시키는 구문 / if를 사용해 주면된다
raise NameError('비밀번호가 잘못되었습니다.')