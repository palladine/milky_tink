import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import tinvest.protos.Main_pb2 as _Main_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_ACTION_UNSPECIFIED: _ClassVar[SubscriptionAction]
    SUBSCRIPTION_ACTION_SUBSCRIBE: _ClassVar[SubscriptionAction]
    SUBSCRIPTION_ACTION_UNSUBSCRIBE: _ClassVar[SubscriptionAction]

class SubscriptionInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_INTERVAL_UNSPECIFIED: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_ONE_MINUTE: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_FIVE_MINUTES: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_FIFTEEN_MINUTES: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_ONE_HOUR: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_ONE_DAY: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_2_MIN: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_3_MIN: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_10_MIN: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_30_MIN: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_2_HOUR: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_4_HOUR: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_WEEK: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_MONTH: _ClassVar[SubscriptionInterval]

class CandleInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CANDLE_INTERVAL_UNSPECIFIED: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_1_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_5_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_15_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_HOUR: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_DAY: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_2_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_3_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_10_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_30_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_2_HOUR: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_4_HOUR: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_WEEK: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_MONTH: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_5_SEC: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_10_SEC: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_30_SEC: _ClassVar[CandleInterval]

class OrderBookType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDERBOOK_TYPE_UNSPECIFIED: _ClassVar[OrderBookType]
    ORDERBOOK_TYPE_EXCHANGE: _ClassVar[OrderBookType]
    ORDERBOOK_TYPE_DEALER: _ClassVar[OrderBookType]
    ORDERBOOK_TYPE_ALL: _ClassVar[OrderBookType]

class SubscriptionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_STATUS_UNSPECIFIED: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_SUCCESS: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_DEPTH_IS_INVALID: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_INTERNAL_ERROR: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_SUBSCRIPTION_NOT_FOUND: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_SOURCE_IS_INVALID: _ClassVar[SubscriptionStatus]

class TradeSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRADE_SOURCE_UNSPECIFIED: _ClassVar[TradeSourceType]
    TRADE_SOURCE_EXCHANGE: _ClassVar[TradeSourceType]
    TRADE_SOURCE_DEALER: _ClassVar[TradeSourceType]
    TRADE_SOURCE_ALL: _ClassVar[TradeSourceType]

class CandleSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CANDLE_SOURCE_UNSPECIFIED: _ClassVar[CandleSource]
    CANDLE_SOURCE_EXCHANGE: _ClassVar[CandleSource]
    CANDLE_SOURCE_DEALER_WEEKEND: _ClassVar[CandleSource]

class TradeDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRADE_DIRECTION_UNSPECIFIED: _ClassVar[TradeDirection]
    TRADE_DIRECTION_BUY: _ClassVar[TradeDirection]
    TRADE_DIRECTION_SELL: _ClassVar[TradeDirection]

class LastPriceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LAST_PRICE_UNSPECIFIED: _ClassVar[LastPriceType]
    LAST_PRICE_EXCHANGE: _ClassVar[LastPriceType]
    LAST_PRICE_DEALER: _ClassVar[LastPriceType]
SUBSCRIPTION_ACTION_UNSPECIFIED: SubscriptionAction
SUBSCRIPTION_ACTION_SUBSCRIBE: SubscriptionAction
SUBSCRIPTION_ACTION_UNSUBSCRIBE: SubscriptionAction
SUBSCRIPTION_INTERVAL_UNSPECIFIED: SubscriptionInterval
SUBSCRIPTION_INTERVAL_ONE_MINUTE: SubscriptionInterval
SUBSCRIPTION_INTERVAL_FIVE_MINUTES: SubscriptionInterval
SUBSCRIPTION_INTERVAL_FIFTEEN_MINUTES: SubscriptionInterval
SUBSCRIPTION_INTERVAL_ONE_HOUR: SubscriptionInterval
SUBSCRIPTION_INTERVAL_ONE_DAY: SubscriptionInterval
SUBSCRIPTION_INTERVAL_2_MIN: SubscriptionInterval
SUBSCRIPTION_INTERVAL_3_MIN: SubscriptionInterval
SUBSCRIPTION_INTERVAL_10_MIN: SubscriptionInterval
SUBSCRIPTION_INTERVAL_30_MIN: SubscriptionInterval
SUBSCRIPTION_INTERVAL_2_HOUR: SubscriptionInterval
SUBSCRIPTION_INTERVAL_4_HOUR: SubscriptionInterval
SUBSCRIPTION_INTERVAL_WEEK: SubscriptionInterval
SUBSCRIPTION_INTERVAL_MONTH: SubscriptionInterval
CANDLE_INTERVAL_UNSPECIFIED: CandleInterval
CANDLE_INTERVAL_1_MIN: CandleInterval
CANDLE_INTERVAL_5_MIN: CandleInterval
CANDLE_INTERVAL_15_MIN: CandleInterval
CANDLE_INTERVAL_HOUR: CandleInterval
CANDLE_INTERVAL_DAY: CandleInterval
CANDLE_INTERVAL_2_MIN: CandleInterval
CANDLE_INTERVAL_3_MIN: CandleInterval
CANDLE_INTERVAL_10_MIN: CandleInterval
CANDLE_INTERVAL_30_MIN: CandleInterval
CANDLE_INTERVAL_2_HOUR: CandleInterval
CANDLE_INTERVAL_4_HOUR: CandleInterval
CANDLE_INTERVAL_WEEK: CandleInterval
CANDLE_INTERVAL_MONTH: CandleInterval
CANDLE_INTERVAL_5_SEC: CandleInterval
CANDLE_INTERVAL_10_SEC: CandleInterval
CANDLE_INTERVAL_30_SEC: CandleInterval
ORDERBOOK_TYPE_UNSPECIFIED: OrderBookType
ORDERBOOK_TYPE_EXCHANGE: OrderBookType
ORDERBOOK_TYPE_DEALER: OrderBookType
ORDERBOOK_TYPE_ALL: OrderBookType
SUBSCRIPTION_STATUS_UNSPECIFIED: SubscriptionStatus
SUBSCRIPTION_STATUS_SUCCESS: SubscriptionStatus
SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND: SubscriptionStatus
SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID: SubscriptionStatus
SUBSCRIPTION_STATUS_DEPTH_IS_INVALID: SubscriptionStatus
SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID: SubscriptionStatus
SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED: SubscriptionStatus
SUBSCRIPTION_STATUS_INTERNAL_ERROR: SubscriptionStatus
SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS: SubscriptionStatus
SUBSCRIPTION_STATUS_SUBSCRIPTION_NOT_FOUND: SubscriptionStatus
SUBSCRIPTION_STATUS_SOURCE_IS_INVALID: SubscriptionStatus
TRADE_SOURCE_UNSPECIFIED: TradeSourceType
TRADE_SOURCE_EXCHANGE: TradeSourceType
TRADE_SOURCE_DEALER: TradeSourceType
TRADE_SOURCE_ALL: TradeSourceType
CANDLE_SOURCE_UNSPECIFIED: CandleSource
CANDLE_SOURCE_EXCHANGE: CandleSource
CANDLE_SOURCE_DEALER_WEEKEND: CandleSource
TRADE_DIRECTION_UNSPECIFIED: TradeDirection
TRADE_DIRECTION_BUY: TradeDirection
TRADE_DIRECTION_SELL: TradeDirection
LAST_PRICE_UNSPECIFIED: LastPriceType
LAST_PRICE_EXCHANGE: LastPriceType
LAST_PRICE_DEALER: LastPriceType

class CandleInstrument(_message.Message):
    __slots__ = ("figi", "interval", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    interval: SubscriptionInterval
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., interval: _Optional[_Union[SubscriptionInterval, str]] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class OrderBookInstrument(_message.Message):
    __slots__ = ("figi", "depth", "instrument_id", "order_book_type")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_TYPE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    depth: int
    instrument_id: str
    order_book_type: OrderBookType
    def __init__(self, figi: _Optional[str] = ..., depth: _Optional[int] = ..., instrument_id: _Optional[str] = ..., order_book_type: _Optional[_Union[OrderBookType, str]] = ...) -> None: ...

class TradeInstrument(_message.Message):
    __slots__ = ("figi", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class InfoInstrument(_message.Message):
    __slots__ = ("figi", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class LastPriceInstrument(_message.Message):
    __slots__ = ("figi", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class GetCandlesRequest(_message.Message):
    __slots__ = ("figi", "to", "interval", "instrument_id", "candle_source_type", "limit")
    class CandleSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CANDLE_SOURCE_UNSPECIFIED: _ClassVar[GetCandlesRequest.CandleSource]
        CANDLE_SOURCE_EXCHANGE: _ClassVar[GetCandlesRequest.CandleSource]
        CANDLE_SOURCE_INCLUDE_WEEKEND: _ClassVar[GetCandlesRequest.CandleSource]
    CANDLE_SOURCE_UNSPECIFIED: GetCandlesRequest.CandleSource
    CANDLE_SOURCE_EXCHANGE: GetCandlesRequest.CandleSource
    CANDLE_SOURCE_INCLUDE_WEEKEND: GetCandlesRequest.CandleSource
    FIGI_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CANDLE_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    figi: str
    to: _timestamp_pb2.Timestamp
    interval: CandleInterval
    instrument_id: str
    candle_source_type: GetCandlesRequest.CandleSource
    limit: int
    def __init__(self, figi: _Optional[str] = ..., to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., interval: _Optional[_Union[CandleInterval, str]] = ..., instrument_id: _Optional[str] = ..., candle_source_type: _Optional[_Union[GetCandlesRequest.CandleSource, str]] = ..., limit: _Optional[int] = ..., **kwargs) -> None: ...

class SubscribeCandlesRequest(_message.Message):
    __slots__ = ("subscription_action", "instruments", "waiting_close", "candle_source_type")
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    WAITING_CLOSE_FIELD_NUMBER: _ClassVar[int]
    CANDLE_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    subscription_action: SubscriptionAction
    instruments: _containers.RepeatedCompositeFieldContainer[CandleInstrument]
    waiting_close: bool
    candle_source_type: GetCandlesRequest.CandleSource
    def __init__(self, subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., instruments: _Optional[_Iterable[_Union[CandleInstrument, _Mapping]]] = ..., waiting_close: bool = ..., candle_source_type: _Optional[_Union[GetCandlesRequest.CandleSource, str]] = ...) -> None: ...

class SubscribeOrderBookRequest(_message.Message):
    __slots__ = ("subscription_action", "instruments")
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    subscription_action: SubscriptionAction
    instruments: _containers.RepeatedCompositeFieldContainer[OrderBookInstrument]
    def __init__(self, subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., instruments: _Optional[_Iterable[_Union[OrderBookInstrument, _Mapping]]] = ...) -> None: ...

class SubscribeTradesRequest(_message.Message):
    __slots__ = ("subscription_action", "instruments", "trade_source", "with_open_interest")
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    TRADE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    WITH_OPEN_INTEREST_FIELD_NUMBER: _ClassVar[int]
    subscription_action: SubscriptionAction
    instruments: _containers.RepeatedCompositeFieldContainer[TradeInstrument]
    trade_source: TradeSourceType
    with_open_interest: bool
    def __init__(self, subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., instruments: _Optional[_Iterable[_Union[TradeInstrument, _Mapping]]] = ..., trade_source: _Optional[_Union[TradeSourceType, str]] = ..., with_open_interest: bool = ...) -> None: ...

class SubscribeInfoRequest(_message.Message):
    __slots__ = ("subscription_action", "instruments")
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    subscription_action: SubscriptionAction
    instruments: _containers.RepeatedCompositeFieldContainer[InfoInstrument]
    def __init__(self, subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., instruments: _Optional[_Iterable[_Union[InfoInstrument, _Mapping]]] = ...) -> None: ...

class SubscribeLastPriceRequest(_message.Message):
    __slots__ = ("subscription_action", "instruments")
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    subscription_action: SubscriptionAction
    instruments: _containers.RepeatedCompositeFieldContainer[LastPriceInstrument]
    def __init__(self, subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., instruments: _Optional[_Iterable[_Union[LastPriceInstrument, _Mapping]]] = ...) -> None: ...

class PingDelaySettings(_message.Message):
    __slots__ = ("ping_delay_ms",)
    PING_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    ping_delay_ms: int
    def __init__(self, ping_delay_ms: _Optional[int] = ...) -> None: ...

class CandleSubscription(_message.Message):
    __slots__ = ("figi", "interval", "subscription_status", "instrument_uid", "waiting_close", "stream_id", "subscription_id", "subscription_action", "candle_source_type", "ticker", "class_code")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    WAITING_CLOSE_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CANDLE_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    interval: SubscriptionInterval
    subscription_status: SubscriptionStatus
    instrument_uid: str
    waiting_close: bool
    stream_id: str
    subscription_id: str
    subscription_action: SubscriptionAction
    candle_source_type: GetCandlesRequest.CandleSource
    ticker: str
    class_code: str
    def __init__(self, figi: _Optional[str] = ..., interval: _Optional[_Union[SubscriptionInterval, str]] = ..., subscription_status: _Optional[_Union[SubscriptionStatus, str]] = ..., instrument_uid: _Optional[str] = ..., waiting_close: bool = ..., stream_id: _Optional[str] = ..., subscription_id: _Optional[str] = ..., subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., candle_source_type: _Optional[_Union[GetCandlesRequest.CandleSource, str]] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ...) -> None: ...

class OrderBookSubscription(_message.Message):
    __slots__ = ("figi", "depth", "subscription_status", "instrument_uid", "stream_id", "subscription_id", "order_book_type", "subscription_action", "ticker", "class_code")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    depth: int
    subscription_status: SubscriptionStatus
    instrument_uid: str
    stream_id: str
    subscription_id: str
    order_book_type: OrderBookType
    subscription_action: SubscriptionAction
    ticker: str
    class_code: str
    def __init__(self, figi: _Optional[str] = ..., depth: _Optional[int] = ..., subscription_status: _Optional[_Union[SubscriptionStatus, str]] = ..., instrument_uid: _Optional[str] = ..., stream_id: _Optional[str] = ..., subscription_id: _Optional[str] = ..., order_book_type: _Optional[_Union[OrderBookType, str]] = ..., subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ...) -> None: ...

class TradeSubscription(_message.Message):
    __slots__ = ("figi", "subscription_status", "instrument_uid", "stream_id", "subscription_id", "with_open_interest", "subscription_action", "ticker", "class_code")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    WITH_OPEN_INTEREST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    subscription_status: SubscriptionStatus
    instrument_uid: str
    stream_id: str
    subscription_id: str
    with_open_interest: bool
    subscription_action: SubscriptionAction
    ticker: str
    class_code: str
    def __init__(self, figi: _Optional[str] = ..., subscription_status: _Optional[_Union[SubscriptionStatus, str]] = ..., instrument_uid: _Optional[str] = ..., stream_id: _Optional[str] = ..., subscription_id: _Optional[str] = ..., with_open_interest: bool = ..., subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ...) -> None: ...

class InfoSubscription(_message.Message):
    __slots__ = ("figi", "subscription_status", "instrument_uid", "stream_id", "subscription_id", "subscription_action", "ticker", "class_code")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    subscription_status: SubscriptionStatus
    instrument_uid: str
    stream_id: str
    subscription_id: str
    subscription_action: SubscriptionAction
    ticker: str
    class_code: str
    def __init__(self, figi: _Optional[str] = ..., subscription_status: _Optional[_Union[SubscriptionStatus, str]] = ..., instrument_uid: _Optional[str] = ..., stream_id: _Optional[str] = ..., subscription_id: _Optional[str] = ..., subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ...) -> None: ...

class SubscribeCandlesResponse(_message.Message):
    __slots__ = ("tracking_id", "candles_subscriptions")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    CANDLES_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    candles_subscriptions: _containers.RepeatedCompositeFieldContainer[CandleSubscription]
    def __init__(self, tracking_id: _Optional[str] = ..., candles_subscriptions: _Optional[_Iterable[_Union[CandleSubscription, _Mapping]]] = ...) -> None: ...

class SubscribeOrderBookResponse(_message.Message):
    __slots__ = ("tracking_id", "order_book_subscriptions")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    order_book_subscriptions: _containers.RepeatedCompositeFieldContainer[OrderBookSubscription]
    def __init__(self, tracking_id: _Optional[str] = ..., order_book_subscriptions: _Optional[_Iterable[_Union[OrderBookSubscription, _Mapping]]] = ...) -> None: ...

class SubscribeTradesResponse(_message.Message):
    __slots__ = ("tracking_id", "trade_subscriptions", "trade_type")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    TRADE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRADE_TYPE_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    trade_subscriptions: _containers.RepeatedCompositeFieldContainer[TradeSubscription]
    trade_type: TradeSourceType
    def __init__(self, tracking_id: _Optional[str] = ..., trade_subscriptions: _Optional[_Iterable[_Union[TradeSubscription, _Mapping]]] = ..., trade_type: _Optional[_Union[TradeSourceType, str]] = ...) -> None: ...

class SubscribeInfoResponse(_message.Message):
    __slots__ = ("tracking_id", "info_subscriptions")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    info_subscriptions: _containers.RepeatedCompositeFieldContainer[InfoSubscription]
    def __init__(self, tracking_id: _Optional[str] = ..., info_subscriptions: _Optional[_Iterable[_Union[InfoSubscription, _Mapping]]] = ...) -> None: ...

class Candle(_message.Message):
    __slots__ = ("figi", "interval", "open", "high", "low", "close", "volume", "time", "last_trade_ts", "instrument_uid", "ticker", "class_code", "volume_buy", "volume_sell", "candle_source_type")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_TRADE_TS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_BUY_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SELL_FIELD_NUMBER: _ClassVar[int]
    CANDLE_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    interval: SubscriptionInterval
    open: _Main_pb2.Quotation
    high: _Main_pb2.Quotation
    low: _Main_pb2.Quotation
    close: _Main_pb2.Quotation
    volume: int
    time: _timestamp_pb2.Timestamp
    last_trade_ts: _timestamp_pb2.Timestamp
    instrument_uid: str
    ticker: str
    class_code: str
    volume_buy: int
    volume_sell: int
    candle_source_type: CandleSource
    def __init__(self, figi: _Optional[str] = ..., interval: _Optional[_Union[SubscriptionInterval, str]] = ..., open: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., high: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., low: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., close: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., volume: _Optional[int] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_trade_ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_uid: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., volume_buy: _Optional[int] = ..., volume_sell: _Optional[int] = ..., candle_source_type: _Optional[_Union[CandleSource, str]] = ...) -> None: ...

class Trade(_message.Message):
    __slots__ = ("figi", "direction", "price", "quantity", "time", "instrument_uid", "trade_source", "ticker", "class_code")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    direction: TradeDirection
    price: _Main_pb2.Quotation
    quantity: int
    time: _timestamp_pb2.Timestamp
    instrument_uid: str
    trade_source: TradeSourceType
    ticker: str
    class_code: str
    def __init__(self, figi: _Optional[str] = ..., direction: _Optional[_Union[TradeDirection, str]] = ..., price: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., quantity: _Optional[int] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_uid: _Optional[str] = ..., trade_source: _Optional[_Union[TradeSourceType, str]] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ...) -> None: ...

class OrderBook(_message.Message):
    __slots__ = ("figi", "depth", "is_consistent", "bids", "asks", "time", "limit_up", "limit_down", "instrument_uid", "order_book_type", "ticker", "class_code")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    IS_CONSISTENT_FIELD_NUMBER: _ClassVar[int]
    BIDS_FIELD_NUMBER: _ClassVar[int]
    ASKS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_UP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_DOWN_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    depth: int
    is_consistent: bool
    bids: _containers.RepeatedCompositeFieldContainer[_Main_pb2.Order]
    asks: _containers.RepeatedCompositeFieldContainer[_Main_pb2.Order]
    time: _timestamp_pb2.Timestamp
    limit_up: _Main_pb2.Quotation
    limit_down: _Main_pb2.Quotation
    instrument_uid: str
    order_book_type: OrderBookType
    ticker: str
    class_code: str
    def __init__(self, figi: _Optional[str] = ..., depth: _Optional[int] = ..., is_consistent: bool = ..., bids: _Optional[_Iterable[_Union[_Main_pb2.Order, _Mapping]]] = ..., asks: _Optional[_Iterable[_Union[_Main_pb2.Order, _Mapping]]] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., limit_up: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., limit_down: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., instrument_uid: _Optional[str] = ..., order_book_type: _Optional[_Union[OrderBookType, str]] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ...) -> None: ...

class TradingStatus(_message.Message):
    __slots__ = ("figi", "trading_status", "time", "limit_order_available_flag", "market_order_available_flag", "instrument_uid", "ticker", "class_code")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_ORDER_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    MARKET_ORDER_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    trading_status: _Main_pb2.SecurityTradingStatus
    time: _timestamp_pb2.Timestamp
    limit_order_available_flag: bool
    market_order_available_flag: bool
    instrument_uid: str
    ticker: str
    class_code: str
    def __init__(self, figi: _Optional[str] = ..., trading_status: _Optional[_Union[_Main_pb2.SecurityTradingStatus, str]] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., limit_order_available_flag: bool = ..., market_order_available_flag: bool = ..., instrument_uid: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ...) -> None: ...

class Ping(_message.Message):
    __slots__ = ("time", "stream_id", "ping_request_time")
    TIME_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    PING_REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    stream_id: str
    ping_request_time: _timestamp_pb2.Timestamp
    def __init__(self, time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stream_id: _Optional[str] = ..., ping_request_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LastPriceSubscription(_message.Message):
    __slots__ = ("figi", "subscription_status", "instrument_uid", "stream_id", "subscription_id", "subscription_action", "ticker", "class_code")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    subscription_status: SubscriptionStatus
    instrument_uid: str
    stream_id: str
    subscription_id: str
    subscription_action: SubscriptionAction
    ticker: str
    class_code: str
    def __init__(self, figi: _Optional[str] = ..., subscription_status: _Optional[_Union[SubscriptionStatus, str]] = ..., instrument_uid: _Optional[str] = ..., stream_id: _Optional[str] = ..., subscription_id: _Optional[str] = ..., subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ...) -> None: ...

class SubscribeLastPriceResponse(_message.Message):
    __slots__ = ("tracking_id", "last_price_subscriptions")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    last_price_subscriptions: _containers.RepeatedCompositeFieldContainer[LastPriceSubscription]
    def __init__(self, tracking_id: _Optional[str] = ..., last_price_subscriptions: _Optional[_Iterable[_Union[LastPriceSubscription, _Mapping]]] = ...) -> None: ...

class LastPrice(_message.Message):
    __slots__ = ("figi", "price", "time", "ticker", "class_code", "instrument_uid", "last_price_type")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    price: _Main_pb2.Quotation
    time: _timestamp_pb2.Timestamp
    ticker: str
    class_code: str
    instrument_uid: str
    last_price_type: LastPriceType
    def __init__(self, figi: _Optional[str] = ..., price: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., instrument_uid: _Optional[str] = ..., last_price_type: _Optional[_Union[LastPriceType, str]] = ...) -> None: ...

class OpenInterest(_message.Message):
    __slots__ = ("instrument_uid", "time", "open_interest", "ticker", "class_code")
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    OPEN_INTEREST_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    instrument_uid: str
    time: _timestamp_pb2.Timestamp
    open_interest: int
    ticker: str
    class_code: str
    def __init__(self, instrument_uid: _Optional[str] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., open_interest: _Optional[int] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ...) -> None: ...

class MarketDataServerSideStreamRequest(_message.Message):
    __slots__ = ("subscribe_candles_request", "subscribe_order_book_request", "subscribe_trades_request", "subscribe_info_request", "subscribe_last_price_request", "ping_settings")
    SUBSCRIBE_CANDLES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_ORDER_BOOK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_TRADES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_INFO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_LAST_PRICE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    subscribe_candles_request: SubscribeCandlesRequest
    subscribe_order_book_request: SubscribeOrderBookRequest
    subscribe_trades_request: SubscribeTradesRequest
    subscribe_info_request: SubscribeInfoRequest
    subscribe_last_price_request: SubscribeLastPriceRequest
    ping_settings: PingDelaySettings
    def __init__(self, subscribe_candles_request: _Optional[_Union[SubscribeCandlesRequest, _Mapping]] = ..., subscribe_order_book_request: _Optional[_Union[SubscribeOrderBookRequest, _Mapping]] = ..., subscribe_trades_request: _Optional[_Union[SubscribeTradesRequest, _Mapping]] = ..., subscribe_info_request: _Optional[_Union[SubscribeInfoRequest, _Mapping]] = ..., subscribe_last_price_request: _Optional[_Union[SubscribeLastPriceRequest, _Mapping]] = ..., ping_settings: _Optional[_Union[PingDelaySettings, _Mapping]] = ...) -> None: ...

class MarketDataResponse(_message.Message):
    __slots__ = ("subscribe_candles_response", "subscribe_order_book_response", "subscribe_trades_response", "subscribe_info_response", "candle", "trade", "orderbook", "trading_status", "ping", "subscribe_last_price_response", "last_price", "open_interest")
    SUBSCRIBE_CANDLES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_ORDER_BOOK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_TRADES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_INFO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CANDLE_FIELD_NUMBER: _ClassVar[int]
    TRADE_FIELD_NUMBER: _ClassVar[int]
    ORDERBOOK_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_LAST_PRICE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    OPEN_INTEREST_FIELD_NUMBER: _ClassVar[int]
    subscribe_candles_response: SubscribeCandlesResponse
    subscribe_order_book_response: SubscribeOrderBookResponse
    subscribe_trades_response: SubscribeTradesResponse
    subscribe_info_response: SubscribeInfoResponse
    candle: Candle
    trade: Trade
    orderbook: OrderBook
    trading_status: TradingStatus
    ping: Ping
    subscribe_last_price_response: SubscribeLastPriceResponse
    last_price: LastPrice
    open_interest: OpenInterest
    def __init__(self, subscribe_candles_response: _Optional[_Union[SubscribeCandlesResponse, _Mapping]] = ..., subscribe_order_book_response: _Optional[_Union[SubscribeOrderBookResponse, _Mapping]] = ..., subscribe_trades_response: _Optional[_Union[SubscribeTradesResponse, _Mapping]] = ..., subscribe_info_response: _Optional[_Union[SubscribeInfoResponse, _Mapping]] = ..., candle: _Optional[_Union[Candle, _Mapping]] = ..., trade: _Optional[_Union[Trade, _Mapping]] = ..., orderbook: _Optional[_Union[OrderBook, _Mapping]] = ..., trading_status: _Optional[_Union[TradingStatus, _Mapping]] = ..., ping: _Optional[_Union[Ping, _Mapping]] = ..., subscribe_last_price_response: _Optional[_Union[SubscribeLastPriceResponse, _Mapping]] = ..., last_price: _Optional[_Union[LastPrice, _Mapping]] = ..., open_interest: _Optional[_Union[OpenInterest, _Mapping]] = ...) -> None: ...
