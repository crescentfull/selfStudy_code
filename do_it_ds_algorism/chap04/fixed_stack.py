#고정 길이 스택 클래스 FixedStack 구현하기

from typing import Any

class FixedStack :
    """고정 길이 스택 클래스"""

    class Empty(Exception) :
        """비어 있는 FixedStack에 팝 또는 피크할 때 내보내는 예외 처리"""
        pass
    
    class Full(Exception) :
        """가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리"""
        pass
    
    def __init__(self, capacity: int = 256) -> None:
        
        self.stk = [None] * capacity # 스택 본체
        self.capacity = capacity       # 스택의 크기
        self.ptr = 0                          # 스택 포인터
    
    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터 개수를 반환"""
        return self.ptr
    
    def is_empty(self) -> bool:
        """스택이 비어있는지 판단"""
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        """스택이 가득 차 있는지 판단"""
        return self.ptr >= self.capacity
    
    #B
    
    def push(self, value: Any) -> None:
        """스택에 value를 푸시(데이터 삽입)"""
        if self.is_full():                  #스택이 가득 차 있는 경우
            raise FixedStack.Full   #예외 처리 발생
        self.stk[self.ptr] = value
        self.ptr += 1
        
    def pop(self) -> Any:
        """스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)"""
        if self.is_empty():
            raise FixedStack.Empty #예외 처리 발생
        return self.stk[self.ptr -1]
    
    def clear(self) -> None:
        """스택을 비움(모든 데이터를 삭제)"""
        self.ptr = 0
    
    #C    
    def find(self, value: Any) -> Any:
        """스택에서 value를 찾아 첨자(없으면 -1)를 반환"""
        for i in range(self.ptr - 1, -1, -1):  # 꼭대기 쪽부터 선형 검색
            if self.stk[i] == value:
                return i  # 검색 성공
        return -1         # 검색 실패

    def count(self, value: Any) -> bool:
        """스택에 포함되어있는 value의 개수를 반환"""
        c = 0
        for i in range(self.ptr):  # 바닥 쪽부터 선형 검색
            if self.stk[i] == value:
                c += 1             # 들어 있음
        return c

    def __contains__(self, value: Any) -> bool:
        """스택에 value가 있는가?"""
        return self.count(value)

    def dump(self) -> None:
        """덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)"""
        if self.is_empty():  # 스택이 비어 있음
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])