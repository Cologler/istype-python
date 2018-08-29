# istype

After python 3.5, we got a `typing` module.

## Usage

We known `typing.Union[int, str]` mean the type is one of `int` or `str`.
However, we cannot use `isinstance()` for test it.

So...

``` py
from typing import Union
from istype import isinstanceof

assert isinstanceof(1, Union[int, str])
```

try use `from istype import isinstanceof as isinstance` !

## Supported types

* Union
* Any
* Optional
* Tuple
* List
* AnyStr
* Set
* Dict
* Type
* Iterable
* Collection

## Configurable

``` py
from typing import List
from istype import TypeMatcher

matcher = TypeMatcher()
assert not matcher.isinstance([1], List[str])
matcher.check_list_elements = False
assert matcher.isinstance([1], List[str]) # now can ignore element checks
```
