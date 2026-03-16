import { useState, useEffect } from 'react';
import axios from 'axios';


export default function Tile({data, onRemove}) {

    const [tileData, setTileData] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        // Функция для загрузки данных
        const fetchData = async () => {
            
            // Предотвращаем множественные запросы
            if (isLoading) return;
            setIsLoading(true);
            
            try {
                const response = await axios.post('http://127.0.0.1:8000/get_info_tile', {
                    num_cell: data.num_cell
                });
                setTileData(response.data);

            } catch (err) {
                console.error(err);
            } finally {
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
        
        <div
            style={{
                border: '1px solid #dadada'
            }}
        >
            {tileData ? (
                <section
                    style={{
                        backgroundColor: tileData.vol >= data.limit ? tileData.state === 'bid' ? '#ffcbcbd8' : '#a9ffa9e0' : '#fff',
                        transition: 'all 0.4s'
                    }}
                >
                    <div>[{data.share.ticker}]</div>
                    <div><b>{tileData.price}</b></div> 
                    <div>{tileData.vol}</div>
                    
                    <div>
                        <a href="#" onClick={(e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            onRemove(data.num_cell);
                        }}>
                            [x]
                        </a>
                    </div>
                </section>
            ) : (
                <div>...</div>
            )}
        </div>

    )

}