import Home from "./Home";
import GridTableTiles from "./GridTableTiles";


export default function Content({ activeComponent }) {

    const renderComponent = () => {
        switch (activeComponent) {
            case 'home':
                return <Home />;
            case 'tiles':
                return <GridTableTiles />;
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