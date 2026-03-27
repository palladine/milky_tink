import Home from "./Home";
import GridTiles from "./GridTiles"



export default function Content({ activeComponent }) {

    const renderComponent = () => {
        switch (activeComponent) {
            case 'home':
                return <Home />;
            case 'tiles':
                return <GridTiles />;
            case 'tiles_search':
                return <Home />
            default:
                return <Home />;
        }
    };

    return (
        <div>
            {renderComponent()}
        </div>
    )
}