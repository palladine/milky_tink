from .errors import get_error_by_code


def setParamsGetSandboxAccounts(status: str = 'ACCOUNT_STATUS_UNSPECIFIED'):
        '''
            Счета пользователя
            params:
                - status: Статус счета
                    [ACCOUNT_STATUS_UNSPECIFIED, ACCOUNT_STATUS_NEW, ACCOUNT_STATUS_OPEN, 
                    ACCOUNT_STATUS_CLOSED, ACCOUNT_STATUS_ALL]
                    Default: ACCOUNT_STATUS_UNSPECIFIED
        '''
        return {
            'status': status
        }

# +
def setParamsShares(instrumentStatus: str = 'INSTRUMENT_STATUS_BASE',
                    instrumentExchange: str = 'INSTRUMENT_EXCHANGE_UNSPECIFIED'):
    '''
        Список акций
        params:
            - instrumentStatus: Статус запрашиваемых инструментов
                [INSTRUMENT_STATUS_UNSPECIFIED, INSTRUMENT_STATUS_BASE, INSTRUMENT_STATUS_ALL]
                Default: INSTRUMENT_STATUS_UNSPECIFIED
            - instrumentExchange: Площадка торговли
                [INSTRUMENT_EXCHANGE_UNSPECIFIED, INSTRUMENT_EXCHANGE_DEALER]
                Default: INSTRUMENT_EXCHANGE_UNSPECIFIED
    '''
    params = {
        'instrument_status': instrumentStatus,
        'instrument_exchange': instrumentExchange
    }
    
    return params


# +
def setParamsMarketDataServerSideStream(instruments: list[str] | None = None, 
                                        depth: int = 10,
                                        ping_delay = 120000):
    '''
        server-side стрим предоставления биржевой информации (стаканы по инструментам)
    '''
    if instruments is None:
        raise AttributeError(get_error_by_code(704, 'instruments'))
    else:
        instruments_ids = []
        for instrument in instruments:
            instruments_ids.append(
                {
                    "depth": depth,
                    "instrument_id": instrument,
                    "order_book_type": "ORDERBOOK_TYPE_UNSPECIFIED"
                }
            )
        
        params = {
                "subscribe_order_book_request": {
                    "subscription_action": "SUBSCRIPTION_ACTION_SUBSCRIBE",
                    "instruments": instruments_ids
                },
                "ping_settings": {
                    "ping_delay_ms": ping_delay
                }
        }

    return params



def setParamsShareBy(_id: str, 
                        id_type: str = 'INSTRUMENT_ID_UNSPECIFIED',
                        class_code: str|None = None,
                    ):
    '''
        Получить акцию по ее идентификатору
        params:
            - idType: Тип идентификатора инструмента (Required)
                [INSTRUMENT_ID_UNSPECIFIED,
                INSTRUMENT_ID_TYPE_FIGI,
                INSTRUMENT_ID_TYPE_TICKER, 
                INSTRUMENT_ID_TYPE_UID,
                INSTRUMENT_ID_TYPE_POSITION_UID]
                Default: INSTRUMENT_ID_UNSPECIFIED
            - classCode: Идентификатор class_code (Required, если id_type = ticker)
            - id: Идентификатор запрашиваемого инструмента (Required)
    '''
    if not _id:
        raise TypeError("missing 1 required positional argument: '_id'")
    
    result = {
        'idType': id_type,
        'id': _id
    }

    if id_type == 'INSTRUMENT_ID_TYPE_TICKER':
        if not class_code:
            raise TypeError("got an unexpected keyword argument 'class_code'")
        else:
            result.update({'classCode': class_code})

    return result



def setParamsGetOrderBook(instrumentId: str,
                            depth: int = 10
                        ):
    '''
        Стакан по инструменту
        params:
            - depth: Глубина стакана (Required)
            - instrumentId: Идентификатор инструмента (Required)
                            [figi,
                            instrument_uid,
                            ticker_class_code]
    '''
    if not instrumentId:
        raise AttributeError(get_error_by_code(704, 'instrument'))

    if not depth:
        raise AttributeError(get_error_by_code(704, 'depth'))
    
    return {
        'depth': depth,
        'instrument_id': instrumentId
    }