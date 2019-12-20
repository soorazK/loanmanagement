// This is the class file for left sidebar of the UI
/*
  Left sidebar should contain main menu elements and sub menu under them
  Submenus are to be rendered when clicked on main menu
  Mainmenu should not contain routes, should just act as show/hide of sub menu
  Submenu should contain routes to different UI components
*/
import React from 'react';
import {BrowserRouter, Link} from 'react-router-dom';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';
class Sidebar extends React.Component {
render(){
  return(
    <BrowserRouter>
    <div ClassName="container">
      <div className="menu-primary">
        <Link to="/dashboard">Dashboard</Link>
      </div>
      <div className="menu-primary">
        <p className="menu-toggle">Loan Management</p>
        <div className="menu-secondary">
        </div>
      </div>

    </div>
    </BrowserRouter>
  )
}
}
export default Sidebar;
