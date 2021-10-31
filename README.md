## Phase 1:
```python
class Shano(DataClass):
  age: int
  first_name: str
  last_name: str
```
## Phase 2:
```python
class Shano(DataClass):
  age: int
  first_name: str
  last_name: str
  pet: Panda  # Another DataClass or a simple class
```
## Phase 3:
```python
class Shano(DataClass):
  age: Optional(int)
  first_name: str
  last_name: str
  pet: Panda  # Another DataClass or a simple class
```
## Phase 4:
```python
class Shano(DataClass):
  age: Default(Optional(int), 25)
  first_name: str
  last_name: str
  pet: Panda  # Another DataClass or a simple class
```
## Extra Phase:
```python
class Shano(DataClass):
  age: Default(Optional(int), 25)
  first_name: str
  last_name: str
  pet: Panda  # Another DataClass or a simple class

  @annotate(optional=True, default=my_name_implementation)
    def name(self) -> str:
      pass
```