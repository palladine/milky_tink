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
                    timeoutId = setTimeout(getInfoOrderBooks, 700);
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