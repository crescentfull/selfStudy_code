# Class

## 1. 클래스란?

![객체와클래스](https://user-images.githubusercontent.com/86424094/145210069-e743ddd5-cc1a-4802-9222-fee8fa5da758.png)

클래스는 객체를 생성하기 위한 청사진, 혹은 템플레이트라고 생각하면 된다. 클래스에는 객체를 생성하기 위한 필드와 메소드가 정의되어 있다. 클래스로부터 만들어진 객체를 해당 클래스의 인스턴스(instance)라고 한다. 자동차로 예를 들면, 클래스는 자동차의 설계도이고 설계도에 따라 제작된 자동차들이 객체이고 제작된 자동차 객체는 자동차 클래스의 인스턴스이다.  클래스로브터 객체를 만드는 과정을 인스턴스 화 라고 한다. 하나의 클래스로부터 여러개의 인스턴스를 만들 수 있다.

``` python
class Car:
  def __init__(self, model, color, year):
    self.model = model
    self.color = color
    self.year  = year
    
  def drive(self, speed):
    if speed != 0:
      return f'The speed of the car is {speed}.'
    
  def stop(self):
    return "The car has stopped."
    
first_car  = Car("k5", "black", 2021)
second_car = Car("seltos", "white", 2021)

first_car.move(100)
second_car.stop()
    
```



## 2. 클래스 선언

객체는 독립성(Individuality)을 가지므로 클래스도 독립성(Individuality)을 가져야 한다. 

파이썬에서는 `class`를 사용하여 클래스를 선언할 수 있다.
다음은 클래스 정의의 가장 간단한 형태이다. 보통의 클래스 식별자는 대문자로 시작하며 다른 클래스와 구분되어야 한다.

``` python
class ClassName:
    pass
```

위의 클래스는 아무 기능도 갖고있지 않은 클래스이지만 이 클래스도 객체를 생성할 수 있다. 
파이썬에서는 다음과 같이 객체를 생성한다.

```python
first_object  = ClassName()
second_object = ClassName()
```

`first_object`와 `second_object`가 객체이다.

클래스는 크게 2가지로 구성되어야 한다.

- 해당 entity를 표현하는 data / property
- 해당 entity가 가지고 있는 기능들 → Methods

> property가 없는 클래스는 단순 함수를 묶어놓은 클래스이기 때문에, 특별한 경우를 제외하고는 의미가 없는 클래스가 된다. property가 없다는 것은 객체화 하는 의미가 없기때문에 클래스로 구현할 의미가 없다. 이런경우는 단순히 함수들을 묶어놓은 namespace의 역할만 할 뿐이다.
>
> 반대로 method가 없는 클래스들은 단순히 데이터를 담고있는 자료구조이므로 굳이 클래스를 사용할 필요가 없다.

![클래스선언](https://user-images.githubusercontent.com/86424094/145231920-21e55160-67d9-432d-ba39-750983eac443.png)

앞서 정의했던 Car 클래스를 예로 들면 `property`는 model, year, color이고 `method`는 drive와 stop이다.

## 3. 생성자(Constructure)

생성자(constructure)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.

만약 다음과 같이 클래스를 정의했다고 가정해보자.

``` python
class Coffee:
  def setdata(self, water, shot):
    self.water = water
    shef.shot  = shot
    
  def customize(self, ingredient):
    return self.water + self.shot + self.ingredient
  
latte = Coffee()
latte.customize('milk') 
  
```

Coffee 클래스의 인스턴스 latte에 `setdata`메서드를 수행하지 않고 `customize`메서드를 수행하면 다음과 같은 에러를 확인할 수 있다.

```shell
AttributeError: 'Coffee' object has no attribute 'water'
```



만약 객체에 초깃값을 설정해야할 필요가 있을때는 `setdata`메서드를 만들기 보다는 생성자를 구현하는것이 좋다. 

파이썬에서는 `__init__`을 통해 생성자를 추가할 수 있다.

``` python
class Coffee2:
    def __init__(self, water, shot):
        self.water = water
        self.shot = shot

    def customize(self, ingredient):
        return self.water + self.shot + self.ingredient
```

`__init__`메서드는 `latte = Coffee2()`처럼 인스턴스를 생성할때 자동으로 호출되는 메서드로 `__init__ `(initialize)라는 말 그대로 인스턴스를 초기화 하는 역할을 한다. 

> **__(double underscore)의 의미**
>
> - private을 구현하기 위해 사용 
>   - _(single underscore)를 사용한 변수는 접근이 가능하지만 __(double underscore)를 사용하면 접근이 불가능 하다.
> - magic method
>   - 클래스에 특수 이름으로 메서드를 정의하여 특수 구문에 의해 호출되는 특정 연산을 구현할 수 있다.
>   - 클래스가 언어 연산자와 관련하여 고유한 동작을 정의할 수 있도록 한다.
>
> 참고 : https://docs.python.org/3/reference/datamodel.html#special-method-names



생성자를 정의 했으니, 다음을 수행해보자.

```python
latte2 = Coffee2()
```

``` shell
TypeError: __init__() missing 2 required positional arguments: 'water' and 'shot'
```

`latte2 = Coffee2()`를 수행할때 생성자 `__init__`이 호출되어 에러가 발생했다. 에러가 발생한 이유는 생성자의 매개변수인 water과 shot이 전달되지 않았기 때문이다. 이와같은 오류를 방지하려면 water과 shot에 해당되는 값을 다음과 같이 전달해 주어야 한다.

``` python
latte2 = Coffee2(200, 2)
```



## 4. 상속

상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다. 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있다. 상속은 기존 클래스는 그대로 놔둔 채 클래스의 기능을 확장시킬때 주로 사용한다.

```python
from sample_class import Car

class Truck(Car):
    def __init__(self, name):
        self.name = name

    def load(self, baggage):
        return f"Loaded {baggage} into the truck."
```

위와 같이 Car class를 상속받은 Truck class가 있다고 가정했을때 Truck class에는 정의되어 있지 않지만 다음과 같이 Car class에 정의되어 있던 drive, stop 메소드를 사용할 수 있다. 또한 상속받은 클래스의 기능 뿐 아니라 새로운 기능도 추가할 수 있다.

``` python
truck = Truck("Poter")
truck.drive(100) # The speed of the car is 100.
truck.stop() # The car has stopped.
truck.load("box") # Loaded box into the truck.
```



## 5. 메소드 오버라이딩

부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메소드 오버라이딩이라고 한다. 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.

다음과 같은 클래스가 있다고 가정해보자. 이것을 실행하면 아래와같은 오류가 발생한다.

``` python
class Calculator:
    def __init__(self, first, second):
        self.first  = first
        self.second = second
    
    def div(self):
        return self.first / self.second
      
a = Calculator(4,0)
a.div()s
```

``` shell
ZeroDivisionError: division by zero
```

파이썬에서는 4를 0으로 나눌 수 없기때문에 `ZeroDivisionError`를 발생시킨다. 이를 방지하고 싶다면 Calculator를 상속하는 다음과 같은 클래스를 만들어서 div메소드를 재 정의 할 수 있다.

``` python
class OveridedCalculator(Calculator):
    def div(self):
        return 0 if self.second == 0 else self.first / self.second

b = OveridedCalculator(4, 0)
b.div() # 0
```

기존 Calculator와는 달리 에러가 발생하지 않고 0을 리턴하는 것을 확인할 수 있다.




