import React from "react";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";

function NavBar(){
    

    return (
        <div>
           <nav className="navbar">
                <NavLink className="navbar-item" to="/signup">  Signup  </NavLink>
                <NavLink className="navbar-item" to="/login">  Login  </NavLink>
                <NavLink className="navbar-item" to="/logout">  Logout  </NavLink>
                <NavLink className="navbar-item" to="/properties">  Properties  </NavLink> 
            </nav>
        </div> 

        
    )
}
export default NavBar