# istype

After python 3.5, we got a `typing` module.

## Usage

We known `typing.Union[int, str]` mean the type is one of `int` or `str`.
However, we cannot use `isinstance()` for test it.

So...

``` py
from istype import isinstanceof

isinstanceof(1, Union[int, str]) # now it will return True
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
