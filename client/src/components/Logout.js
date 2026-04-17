import React from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
function Logout({setLogout}){
    const history = useHistory()
    function handleLogout(){
        fetch("/logout", {
            method: "DELETE",
        }).then(() => setLogout())
        history.push('/')
    }
    
    return(
        <header>
            <button onClick={handleLogout} type="button">Logout</button>
        </header>
    )
}
export default Logout