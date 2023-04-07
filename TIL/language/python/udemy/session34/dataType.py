# age: int
# name: str
# height: float
# is_human: bool
# >>> dataType 지정 가능!

# 함수 안에서도 가능하다
def police_check(age: int)->bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return "they can drive"

if police_check(19):
    print("you may pass")
else:
    print("Pay a fine.")