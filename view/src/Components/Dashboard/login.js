// This is the class file for user login system
// The URL for this page is "/dashboard/login"
/*
  This page should contain a user login Form
  user should be able to login with user name and Password
  should have provivsion to restore forgotten password link
*/
import React from 'react';
import {BrowserRouter, Link} from 'react-router-dom';
class Login extends React.Component{
  checkLogin= () =>{
    /*
      MESSAGE TO SOORAZ
      check if user is already logged in
      If yes then redirect user to previous page using BrowserRouter
      else do nothing
    */
  }

  logIn= () =>{
    /*
      MESSAGE TO SOORAZ
      get username and password from form and make api call
      if login succesful set session login, clear login error and redirect to previous page using BrowserRouter modules
      if login invalid redirect to this same page with error message in session
    */
  }
  readError= () =>{
    /*
      MESSAGE TO SOORAZ
      check if there is any login error message in session
      if yes set loginError to true and put error message in errorMessage
    */
    this.lgoinError=false;
    this.errorMessage="Sample Message";
  }
loginError= () =>{
  if(this.loginError){
    return(
      <div className="form-element">
        <p className="error">{this.errorMessage}</p>
      </div>
    )
  }
}
  Form= () =>{
    return(
      <BrowserRouter>
      <div className="form-container">
        <form method="post" action="#">
          <div className="form-element">
            <i classNAme="icon-user"></i>
          </div>
          <this.loginError/>
          <div className="form-element">
            <label>Username</label>
            <input type="text" placeholder="Username" name="username"></input>
          </div>
          <div className="form-element">
            <label>Password</label>
            <input type="password" placeholder="password" name="password"></input>
          </div>
          <div className="form-element">
            <button className="login" onClick={this.logIn}>Login</button>
          </div>
          <div className="message"><Link to="/dashboard/help">Need Help?</Link>  <Link to="/dashboard/resetpassword">Forgot Password?</Link></div>
        </form>
      </div>
      </BrowserRouter>
    )
  }
  render(){
    this.checkLogin();
    return(
      <this.Form/>
    )
  }
}
export default Login;
