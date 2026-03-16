import { useEffect, useState, useCallback } from 'react';
import Tile from './Tile';
import CellTile from './CellTile';
import axios from "axios"



export default function GridTableTiles() {

    const [isVisibleAddFormTile, setIsVisibleAddFormTile] = useState(false);
    // form fields
    const [selectedShare, setSelectedShare] = useState('');
    // Состояние для хранения компонентов в ячейках
    const [cells, setCells] = useState(() => {
        // Создаем матрицу 10x10, заполненную null
        return Array(10).fill().map(() => Array(10).fill(null));
    });

    const [shares, setShares] = useState([]);
    const [isLoading, setIsLoading] = useState(false);


    const handleResponseShares = async () => {
        try {
            const res = await axios.post("http://127.0.0.1:8000/get_shares", {});
            setShares(res.data);
        }
        catch (err) {
            console.error(err);
        }
    };


    const handleChangeShare = (event) => {
        setSelectedShare(event.target.value);
    };

    
    const handleResponseTiles = async () => {
        try {
            const res = await axios.post("http://127.0.0.1:8000/get_tiles", {});
            
            // Создаем новую матрицу на основе response
            const newMatrix = Array(10).fill().map(() => Array(10).fill(null));
            if (Array.isArray(res.data)) {
                res.data.forEach((value, index) => {
                    const num = value.num_cell;
                    const row = parseInt(num / 10);
                    const col = num % 10;
                    newMatrix[row][col] = value;
                });
                setCells(newMatrix);
                
            }
        } catch (err) {
            console.error(err);
        }
    };


    const toggleVisibleAddFormTile = (e) => {
        e.preventDefault(); // Предотвращаем переход по ссылке
        setIsVisibleAddFormTile(!isVisibleAddFormTile);
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


    // Функция для добавления компонента
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
                limit: limit
            });

            // После успешного добавления обновляем плитки
            await handleResponseTiles();
            
            // Закрываем форму
            //setIsVisibleAddFormTile(false);
            
            // Сбрасываем выбранный инструмент
            setSelectedShare('');
            
            // Сбрасываем форму
            form.reset();

        } catch (err) {
            console.error('Error adding tile:', err);
        } finally {
            setIsLoading(false);
        }

    }, [cells, isLoading]);



    // Функция для удаления компонента
    const removeComponent = useCallback(async (num_cell) => {
        
        // Отправляем запрос на удаление
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
            return prevCells; // Если не нашли компонент
        });
    }, []);


// // Функция для клика по ячейке (можно добавить дополнительную логику)
// const handleCellClick = useCallback((row, col) => {
//     console.log(`Клик по ячейке [${row}, ${col}]`, cells[row][col]);
//     // Здесь можно добавить логику, например, показать информацию о компоненте
// }, [cells]);


// // Подсчет свободных ячеек для отображения
// const freeCellsCount = useMemo(() => {
//     return cells.flat().filter(cell => cell === null).length;
// }, [cells]);


    useEffect(() => {
        handleResponseTiles();
        handleResponseShares();
    }, []);



    return (
        <div>
            <section>
                
                    <button onClick={toggleVisibleAddFormTile}>
                        Новая плитка
                    </button>

                    <button>
                        Удалить все плитки
                    </button>
                
            </section>

            {isVisibleAddFormTile && (
                    <section>
                        
                            <form onSubmit={addTile} action="#" method="POST">
                                
                                <label htmlFor="sel_share">Выбор иструмента</label>
                                <select type="text" name="sel_share" 
                                    value={selectedShare} 
                                    onChange={handleChangeShare}>
                                    <option value="">---</option>
                                    {shares.map((option, index) => (
                                        <option key={index} value={option.id}>
                                            {`[${option.ticker}] ${option.name}`}
                                        </option>
                                    ))}
                                </select>

                                <label htmlFor="period_upd">Интервал обновления (сек)</label>
                                <input name="period_upd" type="number" />
                                
                                <label htmlFor="limit">Лимит (объем)</label>
                                <input name="limit" type="number" />
                            
                                <button type='submit'>Добавить</button>
                                <button onClick={toggleVisibleAddFormTile}>X</button>
                            </form>

                    </section>
                )
            }

            {/* Таблица 10x10 */}
            <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(10, 100px)',
                gap: '3px',
                }}>
                
                {cells.map((row, rowIndex) => (
                    row.map((cell, colIndex) => {
                        return (
                            <section key={`${rowIndex}-${colIndex}`}>
                                    <CellTile
                                        isOccupied={cell !== null}
                                    >
                                    {
                                        cell && (
                                        <Tile
                                            data={cell}
                                            onRemove={removeComponent}
                                        />)
                                    }
                                    </CellTile>
                                    
                            </section>
                            
                            
                        )
                    })
                ))}
            </div>
        </div>

    );
};