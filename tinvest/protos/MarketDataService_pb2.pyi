import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import tinvest.protos.Main_pb2 as _Main_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
    bids: _containers.RepeatedCompositeFieldContainer[_Main_pb2.Order]
    asks: _containers.RepeatedCompositeFieldContainer[_Main_pb2.Order]
    last_price: _Main_pb2.Quotation
    close_price: _Main_pb2.Quotation
    limit_up: _Main_pb2.Quotation
    limit_down: _Main_pb2.Quotation
    instrument_uid: str
    ticker: str
    class_code: str
    last_price_ts: _timestamp_pb2.Timestamp
    close_price_ts: _timestamp_pb2.Timestamp
    orderbook_ts: _timestamp_pb2.Timestamp
    def __init__(self, figi: _Optional[str] = ..., depth: _Optional[int] = ..., bids: _Optional[_Iterable[_Union[_Main_pb2.Order, _Mapping]]] = ..., asks: _Optional[_Iterable[_Union[_Main_pb2.Order, _Mapping]]] = ..., last_price: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., close_price: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., limit_up: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., limit_down: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., instrument_uid: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., last_price_ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., close_price_ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., orderbook_ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
