export default function Mainmenu({ setActiveComponent }) {
    

    const handleClick = (e, component) => {
        e.preventDefault(); // предотвращаем переход по ссылке
        setActiveComponent(component);
    };
    
    return (
        <div>
    
            <section>
                
                <div>
                    <button onClick={(e) => handleClick(e, 'tiles')}>Плитки</button>
                </div>

            </section>
        
        </div>
    )

}