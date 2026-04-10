import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
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

class GetOrderBookRequest(_message.Message):
    __slots__ = ("figi", "depth", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    depth: int
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., depth: _Optional[int] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class GetOrderBookResponse(_message.Message):
    __slots__ = ("figi", "depth", "bids", "asks", "last_price", "close_price", "limit_up", "limit_down", "instrument_uid", "ticker", "class_code", "last_price_ts", "close_price_ts", "orderbook_ts")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    BIDS_FIELD_NUMBER: _ClassVar[int]
    ASKS_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    CLOSE_PRICE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_UP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_DOWN_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_TS_FIELD_NUMBER: _ClassVar[int]
    CLOSE_PRICE_TS_FIELD_NUMBER: _ClassVar[int]
    ORDERBOOK_TS_FIELD_NUMBER: _ClassVar[int]
    figi: str
    depth: int
    bids: _containers.RepeatedCompositeFieldContainer[Order]
    asks: _containers.RepeatedCompositeFieldContainer[Order]
    last_price: Quotation
    close_price: Quotation
    limit_up: Quotation
    limit_down: Quotation
    instrument_uid: str
    ticker: str
    class_code: str
    last_price_ts: _timestamp_pb2.Timestamp
    close_price_ts: _timestamp_pb2.Timestamp
    orderbook_ts: _timestamp_pb2.Timestamp
    def __init__(self, figi: _Optional[str] = ..., depth: _Optional[int] = ..., bids: _Optional[_Iterable[_Union[Order, _Mapping]]] = ..., asks: _Optional[_Iterable[_Union[Order, _Mapping]]] = ..., last_price: _Optional[_Union[Quotation, _Mapping]] = ..., close_price: _Optional[_Union[Quotation, _Mapping]] = ..., limit_up: _Optional[_Union[Quotation, _Mapping]] = ..., limit_down: _Optional[_Union[Quotation, _Mapping]] = ..., instrument_uid: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., last_price_ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., close_price_ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., orderbook_ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
