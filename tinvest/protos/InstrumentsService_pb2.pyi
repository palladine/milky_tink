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

class InstrumentStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTRUMENT_STATUS_UNSPECIFIED: _ClassVar[InstrumentStatusType]
    INSTRUMENT_STATUS_BASE: _ClassVar[InstrumentStatusType]
    INSTRUMENT_STATUS_ALL: _ClassVar[InstrumentStatusType]

class InstrumentExchangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTRUMENT_EXCHANGE_UNSPECIFIED: _ClassVar[InstrumentExchangeType]
    INSTRUMENT_EXCHANGE_DEALER: _ClassVar[InstrumentExchangeType]

class ShareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHARE_TYPE_UNSPECIFIED: _ClassVar[ShareType]
    SHARE_TYPE_COMMON: _ClassVar[ShareType]
    SHARE_TYPE_PREFERRED: _ClassVar[ShareType]
    SHARE_TYPE_ADR: _ClassVar[ShareType]
    SHARE_TYPE_GDR: _ClassVar[ShareType]
    SHARE_TYPE_MLP: _ClassVar[ShareType]
    SHARE_TYPE_NY_REG_SHRS: _ClassVar[ShareType]
    SHARE_TYPE_CLOSED_END_FUND: _ClassVar[ShareType]
    SHARE_TYPE_REIT: _ClassVar[ShareType]

class RealExchange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REAL_EXCHANGE_UNSPECIFIED: _ClassVar[RealExchange]
    REAL_EXCHANGE_MOEX: _ClassVar[RealExchange]
    REAL_EXCHANGE_RTS: _ClassVar[RealExchange]
    REAL_EXCHANGE_OTC: _ClassVar[RealExchange]
    REAL_EXCHANGE_DEALER: _ClassVar[RealExchange]
INSTRUMENT_STATUS_UNSPECIFIED: InstrumentStatusType
INSTRUMENT_STATUS_BASE: InstrumentStatusType
INSTRUMENT_STATUS_ALL: InstrumentStatusType
INSTRUMENT_EXCHANGE_UNSPECIFIED: InstrumentExchangeType
INSTRUMENT_EXCHANGE_DEALER: InstrumentExchangeType
SHARE_TYPE_UNSPECIFIED: ShareType
SHARE_TYPE_COMMON: ShareType
SHARE_TYPE_PREFERRED: ShareType
SHARE_TYPE_ADR: ShareType
SHARE_TYPE_GDR: ShareType
SHARE_TYPE_MLP: ShareType
SHARE_TYPE_NY_REG_SHRS: ShareType
SHARE_TYPE_CLOSED_END_FUND: ShareType
SHARE_TYPE_REIT: ShareType
REAL_EXCHANGE_UNSPECIFIED: RealExchange
REAL_EXCHANGE_MOEX: RealExchange
REAL_EXCHANGE_RTS: RealExchange
REAL_EXCHANGE_OTC: RealExchange
REAL_EXCHANGE_DEALER: RealExchange

class MoneyValue(_message.Message):
    __slots__ = ("currency", "units", "nano")
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    NANO_FIELD_NUMBER: _ClassVar[int]
    currency: str
    units: int
    nano: int
    def __init__(self, currency: _Optional[str] = ..., units: _Optional[int] = ..., nano: _Optional[int] = ...) -> None: ...

class BrandData(_message.Message):
    __slots__ = ("logo_name", "logo_base_color", "text_color")
    LOGO_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_BASE_COLOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
    logo_name: str
    logo_base_color: str
    text_color: str
    def __init__(self, logo_name: _Optional[str] = ..., logo_base_color: _Optional[str] = ..., text_color: _Optional[str] = ...) -> None: ...

class Share(_message.Message):
    __slots__ = ("figi", "ticker", "class_code", "isin", "lot", "currency", "klong", "kshort", "dlong", "dshort", "dlong_min", "dshort_min", "short_enabled_flag", "name", "exchange", "ipo_date", "issue_size", "country_of_risk", "country_of_risk_name", "sector", "issue_size_plan", "nominal", "trading_status", "otc_flag", "buy_available_flag", "sell_available_flag", "div_yield_flag", "share_type", "min_price_increment", "api_trade_available_flag", "uid", "real_exchange", "position_uid", "asset_uid", "instrument_exchange", "required_tests", "for_iis_flag", "for_qual_investor_flag", "weekend_flag", "blocked_tca_flag", "liquidity_flag", "first_1min_candle_date", "first_1day_candle_date", "brand", "dlong_client", "dshort_client")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    ISIN_FIELD_NUMBER: _ClassVar[int]
    LOT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    KLONG_FIELD_NUMBER: _ClassVar[int]
    KSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_FIELD_NUMBER: _ClassVar[int]
    DSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_MIN_FIELD_NUMBER: _ClassVar[int]
    DSHORT_MIN_FIELD_NUMBER: _ClassVar[int]
    SHORT_ENABLED_FLAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    IPO_DATE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_NAME_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_PLAN_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    OTC_FLAG_FIELD_NUMBER: _ClassVar[int]
    BUY_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    SELL_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    DIV_YIELD_FLAG_FIELD_NUMBER: _ClassVar[int]
    SHARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    REAL_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    ASSET_UID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_TESTS_FIELD_NUMBER: _ClassVar[int]
    FOR_IIS_FLAG_FIELD_NUMBER: _ClassVar[int]
    FOR_QUAL_INVESTOR_FLAG_FIELD_NUMBER: _ClassVar[int]
    WEEKEND_FLAG_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TCA_FLAG_FIELD_NUMBER: _ClassVar[int]
    LIQUIDITY_FLAG_FIELD_NUMBER: _ClassVar[int]
    FIRST_1MIN_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_1DAY_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    DLONG_CLIENT_FIELD_NUMBER: _ClassVar[int]
    DSHORT_CLIENT_FIELD_NUMBER: _ClassVar[int]
    figi: str
    ticker: str
    class_code: str
    isin: str
    lot: int
    currency: str
    klong: _Main_pb2.Quotation
    kshort: _Main_pb2.Quotation
    dlong: _Main_pb2.Quotation
    dshort: _Main_pb2.Quotation
    dlong_min: _Main_pb2.Quotation
    dshort_min: _Main_pb2.Quotation
    short_enabled_flag: bool
    name: str
    exchange: str
    ipo_date: _timestamp_pb2.Timestamp
    issue_size: int
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    issue_size_plan: int
    nominal: MoneyValue
    trading_status: _Main_pb2.SecurityTradingStatus
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    div_yield_flag: bool
    share_type: ShareType
    min_price_increment: _Main_pb2.Quotation
    api_trade_available_flag: bool
    uid: str
    real_exchange: RealExchange
    position_uid: str
    asset_uid: str
    instrument_exchange: InstrumentExchangeType
    required_tests: _containers.RepeatedScalarFieldContainer[str]
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    liquidity_flag: bool
    first_1min_candle_date: _timestamp_pb2.Timestamp
    first_1day_candle_date: _timestamp_pb2.Timestamp
    brand: BrandData
    dlong_client: _Main_pb2.Quotation
    dshort_client: _Main_pb2.Quotation
    def __init__(self, figi: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., isin: _Optional[str] = ..., lot: _Optional[int] = ..., currency: _Optional[str] = ..., klong: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., kshort: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., dlong: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., dshort: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., dlong_min: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., dshort_min: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., short_enabled_flag: bool = ..., name: _Optional[str] = ..., exchange: _Optional[str] = ..., ipo_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., issue_size: _Optional[int] = ..., country_of_risk: _Optional[str] = ..., country_of_risk_name: _Optional[str] = ..., sector: _Optional[str] = ..., issue_size_plan: _Optional[int] = ..., nominal: _Optional[_Union[MoneyValue, _Mapping]] = ..., trading_status: _Optional[_Union[_Main_pb2.SecurityTradingStatus, str]] = ..., otc_flag: bool = ..., buy_available_flag: bool = ..., sell_available_flag: bool = ..., div_yield_flag: bool = ..., share_type: _Optional[_Union[ShareType, str]] = ..., min_price_increment: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., api_trade_available_flag: bool = ..., uid: _Optional[str] = ..., real_exchange: _Optional[_Union[RealExchange, str]] = ..., position_uid: _Optional[str] = ..., asset_uid: _Optional[str] = ..., instrument_exchange: _Optional[_Union[InstrumentExchangeType, str]] = ..., required_tests: _Optional[_Iterable[str]] = ..., for_iis_flag: bool = ..., for_qual_investor_flag: bool = ..., weekend_flag: bool = ..., blocked_tca_flag: bool = ..., liquidity_flag: bool = ..., first_1min_candle_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., first_1day_candle_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., brand: _Optional[_Union[BrandData, _Mapping]] = ..., dlong_client: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ..., dshort_client: _Optional[_Union[_Main_pb2.Quotation, _Mapping]] = ...) -> None: ...

class InstrumentsRequest(_message.Message):
    __slots__ = ("instrument_status", "instrument_exchange")
    INSTRUMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    instrument_status: InstrumentStatusType
    instrument_exchange: InstrumentExchangeType
    def __init__(self, instrument_status: _Optional[_Union[InstrumentStatusType, str]] = ..., instrument_exchange: _Optional[_Union[InstrumentExchangeType, str]] = ...) -> None: ...

class SharesResponse(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[Share]
    def __init__(self, instruments: _Optional[_Iterable[_Union[Share, _Mapping]]] = ...) -> None: ...
