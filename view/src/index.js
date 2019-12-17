//react modules
import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter, Route, Link, Switch} from 'react-router-dom'
//css and scss files
import './Css/font-awesome.min.css';
import './Scss/master.scss';

//react components
import Header from './Components/header.js'
import Login from './Components/Dashboard/login.js'
import NotFound from './Components/notFound.js'
//assigning app variable
const App= () =>{
  return(
    <BrowserRouter>
      <Route path="/dashboard/login" exact component={Login} />
  </BrowserRouter>
  )
}
//rendering different components
ReactDOM.render(<Header name="Nepal"/>, document.querySelector('#navbar'))
ReactDOM.render(<App />, document.querySelector('#app'))
