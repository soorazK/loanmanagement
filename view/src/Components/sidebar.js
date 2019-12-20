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
 menuToggle= (e) => {
   var icon=document.getElementById(e).getElementsByTagName('i')[0];
    var subMenu=document.getElementById(e).lastChild;
    if(subMenu.classList[1]==="hide"){
      subMenu.classList.remove("hide");
      icon.classList.remove("icon-caret-down");
      icon.classList.add("icon-caret-up");
    }

    else{
      subMenu.classList.add("hide");
      icon.classList.remove("icon-caret-up");
      icon.classList.add("icon-caret-down");

    }

  }
render(){
  return(
    <BrowserRouter>
    <div className="menu-container">
      <div className="menu-primary">
        <button className="menu-toggle"><Link to="/dashboard">Dashboard</Link></button>
      </div>
      <div className="menu-primary" id="loanManagement">
        <button className="menu-toggle" onClick={this.menuToggle.bind(this,"loanManagement")}>Loan Management  <i className="icon-caret-down"></i></button>
        <div className="menu-secondary hide">
          <Link to="/loans/list">List</Link>
          <Link to="/loans/types">Loan types</Link>
          <Link to="/loans/payments">Payments</Link>
          <Link to="/loans/refunds">Refunds</Link>
        </div>
      </div>
      <div className="menu-primary" id="loanApplication">
        <button className="menu-toggle" onClick={this.menuToggle.bind(this,"loanApplication")}>Loan Application  <i className="icon-caret-down"></i></button>
        <div className="menu-secondary hide">
          <Link to="/loans/new">Apply</Link>
          <Link to="/loans/types">Check Status</Link>
        </div>
      </div>
      <div className="menu-primary" id="settings">
        <button className="menu-toggle" onClick={this.menuToggle.bind(this,"settings")}>Settings  <i className="icon-caret-down"></i></button>
        <div className="menu-secondary hide">
          <Link to="/settings/account">Account Settigs</Link>
          <Link to="/settings/theme">Themes</Link>
        </div>
      </div>
    </div>
    </BrowserRouter>
  )
}
}
export default Sidebar;
