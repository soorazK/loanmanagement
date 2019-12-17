// This is the class file for left sidebar of the UI
/*
  Left sidebar should contain main menu elements and sub menu under them
  Submenus are to be rendered when clicked on main menu
  Mainmenu should not contain routes, should just act as show/hide of sub menu
  Submenu should contain routes to different UI components
*/
import React from 'react';
import {BrowserRouter,Link} from 'react-router-dom';
class Sidebar extends React.component {
  menuList= () =>{
    return(
      <BrowserRouter>
        <div className="menu-item">
          <Link to="/dashboard">
            <div className="menu-name">
              Dashboard
            </div>
          </Link>
        </div>
        <div className="menu-item">
            <div className="menu-name">
              Loan Management
            </div>
            <div className="sub-menus">
              <div className="sub-menu-item">
                <Link to="loanmanagement/list">
                  <div className="sub-menu-name">
                    Loan List
                  </div>
                </Link>
              </div>
              <div className="sub-menu-item">
                <Link to="loanmanagement/editloan">
                  <div className="sub-menu-name">
                    Edit Loan
                  </div>
                </Link>
              </div>
            </div>
        </div>
        <div className="menu-item">
            <div className="menu-name">
              Loan Payment
            </div>
            <div className="sub-menus">
              <div className="sub-menu-item">
                <Link to="loanpayment/list">
                  <div className="sub-menu-name">
                    Payment List
                  </div>
                </Link>
              </div>
              <div className="sub-menu-item">
                <Link to="loanapyment/add">
                  <div className="sub-menu-name">
                    Add Payment
                  </div>
                </Link>
              </div>
            </div>
        </div>
      </BrowserRouter>
    )
  }

  render(){
    return(
      <this.menuList />
    )
  }
}
export default Sidebar;
