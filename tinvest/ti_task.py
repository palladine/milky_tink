class Task:
    def __init__(self, service, method, params=None, extras=None):
        self.service = service
        self.method = method
        self.params = params if params else {}
        self.extras = extras      # дополнительные параметры

        try:
            self.data = getattr(self, f'setParams{self.method}')(**self.params)
        except Exception:
            raise AttributeError(f'Wrong method')



    def setParamsShares(self, instrumentStatus: str = 'INSTRUMENT_STATUS_UNSPECIFIED',
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
        return {
            'instrumentStatus': instrumentStatus,
            'instrumentExchange': instrumentExchange
        }
    


    def setParamsShareBy(self, 
                            _id: str, 
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
    


    def setParamsGetOrderBook(self,
                                instrumentId: str,
                                depth: int = 50
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
            raise TypeError("missing 1 required positional argument: 'instrumentId'")

        if not depth:
            raise TypeError("got an unexpected keyword argument 'depth'")
        
        return {
            'depth': depth,
            'instrumentId': instrumentId
        }