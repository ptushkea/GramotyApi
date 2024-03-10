# GramotyApi

### Installing
```
Ещё въ разработкѣ
```

### Example
```py
from gramoty import *


def main():
  search = Search().find(1, 1) # "find(int, int)" - Городъ и Номеръ
  birchmark = Api().get(search, split=True) # "split" - Раздѣлять ли текстъ

  return birchmark.text # Возвращаетъ текстъ берестяной грамоты 


if __name__ == '__main__':
  main()

```
