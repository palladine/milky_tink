import { useState } from "react"
import Mainmenu from "./Mainmenu"
import Content from "./Content"


export default function Desktop() {

    const [activeComponent, setActiveComponent] = useState('home');

    return (
        <div>

            <Mainmenu setActiveComponent={setActiveComponent} />

            <Content activeComponent={activeComponent} />
        
        </div>
    )
}