# class variables and methods vs instance variables and methods vs satic methods

Let's break down the differences between instance variables, class variables, instance methods, class methods, and static methods in Python. Here's a detailed comparison in a table format:

| **Aspect**              | **Instance Variables**                                                                 | **Class Variables**                                                                 | **Instance Methods**                                                                 | **Class Methods**                                                                 | **Static Methods**                                                                 |
|-------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Definition**          | Variables that are specific to each instance of a class.                               | Variables that are shared among all instances of a class.                          | Methods that operate on an instance of the class.                                   | Methods that operate on the class itself.                                         | Methods that do not operate on instance or class variables.                       |
| **Declaration**         | Defined inside the `__init__` method or other instance methods using `self`.           | Defined directly within the class, outside any methods.                            | Defined inside the class, taking `self` as the first parameter.                     | Defined inside the class, taking `cls` as the first parameter.                    | Defined inside the class, using the `@staticmethod` decorator.                    |
| **Access**              | Accessed using `self.variable_name`.                                                   | Accessed using `ClassName.variable_name` or `self.__class__.variable_name`.        | Accessed using `self.method_name()`.                                                | Accessed using `cls.method_name()`.                                               | Accessed using `ClassName.method_name()`.                                         |
| **Scope**               | Specific to each instance of the class.                                                | Shared across all instances of the class.                                          | Operate on data specific to an instance.                                            | Operate on class-level data.                                                      | Operate independently of class or instance data.                                  |
| **Example**             | ```python\nclass MyClass:\n    def __init__(self, value):\n        self.value = value\n``` | ```python\nclass MyClass:\n    class_variable = 10\n```                             | ```python\nclass MyClass:\n    def instance_method(self):\n        pass\n```        | ```python\nclass MyClass:\n    @classmethod\n    def class_method(cls):\n        pass\n``` | ```python\nclass MyClass:\n    @staticmethod\n    def static_method():\n        pass\n``` |

## Additional Details

### Instance Variables

- **Usage**: Store data unique to each instance.
- **Example**:

  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value

  obj1 = MyClass(10)
  obj2 = MyClass(20)
  print(obj1.value)  # Output: 10
  print(obj2.value)  # Output: 20
  ```

### Class Variables

- **Usage**: Store data shared among all instances.
- **Example**:

  ```python
  class MyClass:
      class_variable = 10

  obj1 = MyClass()
  obj2 = MyClass()
  print(obj1.class_variable)  # Output: 10
  print(obj2.class_variable)  # Output: 10
  MyClass.class_variable = 20
  print(obj1.class_variable)  # Output: 20
  print(obj2.class_variable)  # Output: 20
  ```

### Instance Methods

- **Usage**: Operate on instance data.
- **Example**:

  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value

      def instance_method(self):
          return self.value

  obj = MyClass(10)
  print(obj.instance_method())  # Output: 10
  ```

### Class Methods

- **Usage**: Operate on class-level data.
- **Example**:

  ```python
  class MyClass:
      class_variable = 10

      @classmethod
      def class_method(cls):
          return cls.class_variable

  print(MyClass.class_method())  # Output: 10
  ```

### Static Methods

- **Usage**: Perform tasks that do not depend on class or instance data.
- **Example**:

  ```python
  class MyClass:
      @staticmethod
      def static_method(x, y):
          return x + y

  print(MyClass.static_method(5, 3))  # Output: 8
  ```

These distinctions help in organizing and structuring your code effectively, ensuring that methods and variables are used appropriately based on their intended scope and functionality.

If you have any more questions or need further clarification, feel free to ask!

``` python
# Class example
class A:
    def __init__(self):
        self.value_a = 10
    def display(self):
        print("Display class A: ",self.value_a)
class B(A):
    def __init__(self):
        super().__init__()
        self.value = 20
    def display(self):
        print("Display calss B: ",self.value)
class C(B):
    def __init__(self):
        super().__init__()
        self.value = 30
    def display(self):
        print("Display class C: ",self.value)

def main():
    obj = C()
    obj.display()
    super(C, obj).display()
    obj.value_a=15
    super(B, obj).display()
    
if __name__ == '__main__':
    main()
```
### Notes: 
- use @classmethod when you need to work with the class itself (like modifying class variables), and use @staticmethod when you just need a utility function within the class without accessing or modifying class or instance variables.