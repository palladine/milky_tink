import { useState, useEffect, useCallback } from "react";
import axios from "axios";
import Tile from "./Tile";



export default function GridTiles() {
    
    const [cells, setCells] = useState(() => {
            return Array(10).fill().map(() => Array(10).fill(null));
    });
    const [curnums, setCurnums] = useState([]);
    const [infoorderbooks, setInfoorderbooks] = useState({});
    const [isFormAddTile, setFormAddTile] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [selectedShare, setSelectedShare] = useState('');
    const [shares, setShares] = useState([]);

    const GetShares = async () => {
        try {
            const res = await axios.post("http://127.0.0.1:8000/get_shares", {});
            setShares(res.data);
        }
        catch (err) {
            console.error(err);
        }
    };

    // информация о плитках из БД + занесение ее в ячейки 
    const GetTiles = async () => {
            try {
                const res = await axios.post("http://127.0.0.1:8000/get_tiles", {});
                
                const newMatrix = Array(10).fill().map(() => Array(10).fill(null));
                if (Array.isArray(res.data)) {
                    let nums = [];
                    res.data.forEach((value, index) => {
                        const num = value.num_cell;
                        nums.push(num);
                        const row = parseInt(num / 10);
                        const col = num % 10;
                        newMatrix[row][col] = value;
                    });
                    setCells(newMatrix);
                    setCurnums(nums);
                }
            } catch (err) {
                console.error(err);
            }
    };
    

    // Функция для поиска первой свободной ячейки
    const findFirstEmptyCell = (currentCells) => {
        for (let row = 0; row < 10; row++) {
            for (let col = 0; col < 10; col++) {
                if (currentCells[row][col] === null) {
                    return { row, col };
                }
            }
        }
        return null;
    };


    const ChangeShare = (event) => {
        setSelectedShare(event.target.value);
    };


    // Добавление плитки 
    const addTile = useCallback(async (e) => {
        e.preventDefault();
        e.stopPropagation();
        
        // Предотвращаем множественные запросы
        if (isLoading) return;
        setIsLoading(true);

        // Сохраняем данные формы до асинхронных операций
        const form = e.currentTarget;
        const formData = new FormData(form);
        const share_id = parseInt(formData.get('sel_share'));
        const period_upd = parseFloat(formData.get('period_upd'));
        const limit = parseInt(formData.get('limit'));
        const depth = parseInt(formData.get('depth'))

        // Ищем свободную ячейку
        const emptyCell = findFirstEmptyCell(cells);
        
        if (!emptyCell) {
            alert('No free cell!');
            setIsLoading(false);
            return;
        }

        const { row, col } = emptyCell;
        const calc_num_cell = row * 10 + col;

        try {
            await axios.post("http://127.0.0.1:8000/add_tile", {
                id_share: share_id,
                num_cell: calc_num_cell,
                period_upd: period_upd,
                limit: limit,
                depth: depth
            });

            // После успешного добавления обновляем плитки
            await GetTiles();
            
            // Закрываем форму
            //setFormAddTile(false);
            
            setSelectedShare('');
            
            form.reset();

        } catch (err) {
            console.error('Error adding tile:', err);
        } finally {
            setIsLoading(false);
        }

    }, [cells, isLoading]);



    // Функция для удаления плитки
    const removeTile = useCallback(async (num_cell) => {
        
        await axios.post("http://127.0.0.1:8000/remove_tile", {
            num_cell: num_cell
        });
        
        setCells(prevCells => {
            const newCells = prevCells.map(row => [...row]);

            for (let row = 0; row < 10; row++) {
                for (let col = 0; col < 10; col++) {
                    if (newCells[row][col]?.num_cell === num_cell) {
                        newCells[row][col] = null;
                        return newCells;
                    }
                }
            }
            return prevCells;
        });
    }, []);


    const toggleFormAddTile = (e) => {
        e.preventDefault();
        setFormAddTile(!isFormAddTile);
    };




    useEffect(() => {
        GetTiles();
        GetShares();
    }, []);
    
    
    useEffect(() => {
        let isMounted = true;
        let timeoutId = null;

        const getInfoOrderBooks = async () => {
            try {
                const response = await axios.post(
                    'http://127.0.0.1:8000/get_orderbook_tiles', 
                    { nums_cells: curnums },
                );
                
                if (isMounted) {
                    setInfoorderbooks(response.data);
                }
            } catch (err) {
                if (isMounted) {
                    console.log(err.message);
                }
            } finally {
                if (isMounted) {
                    timeoutId = setTimeout(getInfoOrderBooks, 1000);
                }
            }
        };

        if (curnums.length > 0) {
            getInfoOrderBooks();
        }

        return () => {
            isMounted = false;
            if (timeoutId) {
                clearTimeout(timeoutId);
            }
        };
    }, [curnums]);
    

    return (

        <div>
            
            {/* menu */}
            <section
                style={{
                    display: 'flex',
                    gap: '3px',
                    margin: '3px 0px'
                }}
            >
                    <button onClick={toggleFormAddTile}>
                        Новая плитка
                    </button>

                    <button>
                        Удалить все плитки
                    </button>
            </section>


            {isFormAddTile && (
                    <section>
                        
                            <form onSubmit={addTile} action="#" method="POST">
                                
                                <label htmlFor="sel_share">Выбор иструмента</label>
                                <select type="text" name="sel_share" 
                                    value={selectedShare} 
                                    onChange={ChangeShare}>
                                    <option value="">---</option>
                                    {shares.map((option, index) => (
                                        <option key={index} value={option.id}>
                                            {`[${option.ticker}] ${option.name}`}
                                        </option>
                                    ))}
                                </select>

                                <label htmlFor="period_upd">Интервал обновления (сек)</label>
                                <input name="period_upd" type="number" step="0.1" />
                                
                                <label htmlFor="limit">Лимит (объем)</label>
                                <input name="limit" type="number" step='100' />

                                <label htmlFor="depth">Глубина стакана</label>
                                <input name="depth" type="number" />
                            
                                <button type='submit'>Добавить</button>
                                <button onClick={toggleFormAddTile}>X</button>
                            </form>

                    </section>
                )
            }


            {/* таблица */}
            <section style={{
                    margin: '10px 0px', 
                    display: 'flex',
                    flexDirection: 'row',
                    alignItems: 'center',
                    flexWrap: 'wrap',
                    gap: '5px'
            }}>
            
                {cells.map((row, rowIndex) => (
                        row.map((cell, colIndex) => {
                            const pnum = rowIndex * 10 + colIndex;
                            const share_value = infoorderbooks[pnum] || null;

                            return (
                                <div key={`${pnum}`} style={{
                                    width: '170px'
                                }}>
                                    {share_value ? (
                                        <div style={{
                                            border: '1px solid #9292929f',
                                        }}>
                                            <Tile
                                                share_datas={share_value}
                                                cell_datas={cells[rowIndex][colIndex]}
                                                onRemove={removeTile}
                                            />
                                        </div>
                                    ): (
                                        <div style={{
                                            border: '1px solid #9292923d',
                                            height: '23px'
                                        }}></div>
                                    )}
                                </div>
                            )
                        })
                    ))
                }
            </section>
    
    
        </div>
    )
    

}