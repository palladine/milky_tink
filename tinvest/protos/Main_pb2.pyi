from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Quotation(_message.Message):
    __slots__ = ("units", "nano")
    UNITS_FIELD_NUMBER: _ClassVar[int]
    NANO_FIELD_NUMBER: _ClassVar[int]
    units: int
    nano: int
    def __init__(self, units: _Optional[int] = ..., nano: _Optional[int] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ("price", "quantity")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    price: Quotation
    quantity: int
    def __init__(self, price: _Optional[_Union[Quotation, _Mapping]] = ..., quantity: _Optional[int] = ...) -> None: ...
