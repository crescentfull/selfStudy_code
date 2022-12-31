# sales.txt 파일을 읽어서 총매출과 평균 일매출을 파일로 내보내는 프로그램을 작성하시오.
# 내보내는 파일이름은 summary.txt로 하시오

# file = open('/Users/yeongroksong/Desktop/study/code/TIL/language/python/inflearn/기초부터_실무까지_part5/19장_파일과예외처리/sales.txt','r')
# line = file.readline()
# while True:

# 사용자로부터 입력 파일 이름, 출력 파일 이름을 입력 받는다.
infilename = input('입력 파일 이름 : ')
outfilename = input('출력 파일 이름 : ')

# 입출력을 하기 위해서 파일을 연다
infile = open(infilename, 'r')
outfile = open(outfilename, 'w', encoding='UTF-8')

# 합계와 횟수를 위한 변수를 정의한다.
sum = 0
count = 0

# 입력파일에서 한 줄을 읽어서 합계를 계산하고 평균을 구하기 위해서 count 변수값을 1씩 증가
line = infile.readline()
while line != "":
    sales_num = int(line)
    sum += sales_num
    count += 1
    line = infile.readline().rstrip()

# 총 매출과 평균 일 매출을 summary.txt에 기록
outfile.write(f"총 매출 = {sum}\n")
outfile.write(f"평균 일매출 = {sum/count}")

infile.close()
outfile.close()