# # 딕셔너리에 파일쓰기와 파일읽기
import pickle

# # 딕셔너리를 만듬
# gameOption = {
#     "Sound" : 8,
#     "VideoQuality" : "HIGH",
#     "Money" : 100000,
#     "Weaponlist" : ["gun", "missile", "knife"]
# }

# file = open("save.txt", "wb")         # 이진 파일 오픈, 확장자명 마음대로 바꿔도 된다.
# pickle.dump(gameOption, file)       # 딕셔너리를 피클 모듈을 이용하여 파일로 저장
# file.close()

file = open("save.p", "rb")
obj = pickle.load(file)
print(obj)
file.close()