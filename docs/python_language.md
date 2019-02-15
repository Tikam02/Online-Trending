### Concepts
******
The resaon we use super is so that child classes that may be using cooperative multiple inheritance will call the correct nex parent class function in the Method Resolution Order.

```
class ChildB(Base):
    def __init__(self):
        super().__init__()
```


Use Case 1: Super can be called upon in a single inheritance, in order to refer to the parent class or multiple classes without explicitly naming them. It’s somewhat of a shortcut, but more importantly, it helps keep your code maintainable for the foreseeable future.

Use Case 2: Super can be called upon in a dynamic execution environment for multiple or collaborative inheritance. This use is considered exclusive to Python, because it’s not possible with languages that only support single inheritance or are statically compiled.