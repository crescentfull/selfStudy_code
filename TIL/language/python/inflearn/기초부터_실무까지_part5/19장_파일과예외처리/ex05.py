# 파이썬에서 파일 쓰는 방법
# write() : 기본적으로 파일에 쓰는 방법이다. 빈칸(\n)이 필요하면 직접 입력해야한다.
# writelines() : 리스튿 등으로 된 여러문장을 입력하기 위해서 사용한다.
# 문자열을 빈칸(\n)으로 연결하기 위해 join()을 사용한다

file = open("write_test.txt", "w")
file.write("안녕하세요 반갑습니다.\n")
file.write("안녕하세요 송영록입니다니다.\n")
file.close()

file = open("write_test.txt", "a")
file.writelines(['하나','둘','셋','넷','다섯','파이팅'])
file.write('\n')
# 리스트를 보내기는 하는데 \n이라는 것과 리스트의 내용과 합치는 join()을 이용하여 파일에 기록
file.writelines("\n".join(['하나','둘','셋','넷','다섯','파이팅']))
file.write('\n')
file.close()