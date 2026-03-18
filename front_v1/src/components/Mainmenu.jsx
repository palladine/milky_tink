export default function Mainmenu({ setActiveComponent }) {
    

    const handleClick = (e, component) => {
        e.preventDefault(); // предотвращаем переход по ссылке
        setActiveComponent(component);
    };
    
    return (
        <div>
    
            <section
                style={{
                    display: 'flex',
                    gap: '3px'
                }}
            >
                
                <div>
                    <button onClick={(e) => handleClick(e, 'tiles_search')}>Плитки (поиск)</button>
                </div>
                <div>
                    <button onClick={(e) => handleClick(e, 'tiles')}>Плитки</button>
                </div>

            </section>
        
        </div>
    )

}