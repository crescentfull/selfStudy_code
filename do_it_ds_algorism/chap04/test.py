#append()
a_list = [1,2,3]
a_list.append(1) # => [1,2,3,1]

#pop()
a_list = [1,2,3]
a_list.pop()        #=> [1,2]

print(a_list.pop())
#출력: 2
#a_list : [1]

s = []
s.append(1)
s.append(2)
s.append(3)
s.append(5)

print(s)
print(s[-1])
print(len(s))
print(s.pop())
print(len(s))
print(len(s) == 0)
## Stack Class
 
class stack:
    def __init__(self):         # 스택 객체 생성
        self.items = []
    def push(self, item):  # 스택 요소 추가 push(.append())
        self.items.append(item)
    def pop(self):              # 스택 요소 삭제 pop()
        return self.items.pop()
    def peek(self):             # 스택 맨 앞 요소 리턴
        return self.items[0]
    def isEmpty(self):          # 스택이 비었는지 확인(비었으면 True 리턴)
        return not self.items
    
 
stk = stack()                   # stack 객체 생성
print(stk)                      # stack object 생성 확인
                                    # => <__main__.stack object at 0x000001915CB04470> : 생성됨
print(stk.isEmpty())    # 처음에는 아무것도 들어있지 않으므로 True 출력
stk.push(1)                  # stk 에 1 넣음 : [1]
stk.push(2)                 # stk 에 2 넣음 : [1,2]
print(stk.items)          #  =>  [1,2]
print(stk.pop())           # stk 에 2가 꺼내지면서 출력 : 2 / [1]
print(stk.peek())         # stk 맨 앞 값 출력 : 1
print(stk.isEmpty())    # 비어있지 않으므로 False 출력
print(stk.pop())            # stk 에 1가 꺼내지면서 출력 : 1 / []
print(stk.isEmpty())        # 객체에 아무것도 들어있지 않으므로 True 출력


#괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 
# 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
# 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
# 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
#
#여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

case = int(input())