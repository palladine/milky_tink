import { useState, useEffect, useRef } from 'react';
import axios from 'axios';


export default function Tile({data, onRemove}) {

    const [tileData, setTileData] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const lastUpdateRef = useRef(0);

    useEffect(() => {
        // Функция для загрузки данных
        const fetchData = async () => {
            
            // Защита от слишком частых обновлений
            const now = Date.now();
            if (now - lastUpdateRef.current < 100) {
                return;
            }
            
            // Предотвращаем множественные запросы
            if (isLoading) return;
            setIsLoading(true);
            


            try {
                const response = await axios.post('http://127.0.0.1:8000/get_info_tile', {
                    num_cell: data.num_cell
                }, { timeout: 1500 });
                setTileData(response.data);
            } catch (err) {
                console.error(err);
            } finally {
                lastUpdateRef.current = now;
                setIsLoading(false);
            }
        };

        // Загружаем данные сразу при монтировании
        fetchData();

        // Устанавливаем интервал обновления
        const intervalId = setInterval(fetchData, parseInt(data.period_upd)*1000);

        // Очищаем интервал при размонтировании компонента
        return () => clearInterval(intervalId);
    }, []);


    return (
        
        <div style={{
            display: 'flex',
            fontSize: '14px',
            justifyContent: 'space-around',
            alignItems: 'center'
        }}>
            {tileData ? (
                <section
                    style={{
                        border: '1px solid #aaaaaa',
                        backgroundColor: tileData.vol >= data.limit ? tileData.state === 'bid' ? '#ffcbcbd8' : '#a9ffa9e0' : '#eeeeee77',
                        transition: 'all 0.3s',
                        display: 'flex',
                        flexDirection: 'row',
                        alignItems: 'center',
                        width: '170px',
                        height: '23px',
                        flexBasis: '170px',
                        justifyContent: 'space-around',
                        margin: '-1px',
                        
                    }}
                >
                    <div>{data.share.ticker}</div>
                    <div><b>{tileData.price}</b></div> 
                    <div>{tileData.vol}</div>
                    
                    <div>
                        <a href="#" onClick={(e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            onRemove(data.num_cell);
                        }}
                        style={{
                            textDecoration: 'none',
                            color: '#141414'
                        }}
                        >
                            &times;
                        </a>
                    </div>
                </section>
            ) : (
                <div>...</div>
            )}
        </div>

    )

}