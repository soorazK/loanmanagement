import React from 'react';
import ReactDOM from 'react-dom';
import './Css/font-awesome.min.css';
import './Scss/master.scss';
import Login from './Components/login.js'
import Logout from './Components/logout.js'
import Loantypes from './Components/loantypes'
const App = ()=> {
  return (
    <div>
    <Login/>
    <Logout/>
    <Loantypes/>
    </div>

  )
}

ReactDOM.render(<App/>,
document.querySelector('#navbar'));
