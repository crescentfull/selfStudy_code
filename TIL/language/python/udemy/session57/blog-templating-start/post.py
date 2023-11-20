class Post:
    def __init__(self, id, title, body, subtitle):
        self.id = id
        self.title = title
        self.body = body
        self.subtitle = subtitle

    def __repr__(self):
        return f"Post('{self.title}', '{self.id}')"

    # 필요한 경우 추가적인 메서드나 속성을 여기에 정의할 수 있습니다.
    # __repr__ 메서드는 클래스의 문자열 표현을 정의합니다. 이는 디버깅할 때 유용할 수 있습니다