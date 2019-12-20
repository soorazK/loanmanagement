// This is the class file for user login system
// The URL for this page is "/dashboard/login"
/*
  This page should contain a user login Form
  user should be able to login with user name and Password
  should have provivsion to restore forgotten password link
*/
import React from 'react';
import {BrowserRouter, Link} from 'react-router-dom';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
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
      Check if the radio button KEEP ME LOGGED IN is checked or not
      Increase cookie storage time if clicked to 24-48hr
    */
  }
  readError= () =>{
    /*
      MESSAGE TO SOORAZ
      check if there is any login error message in session
      if yes set loginError to true and put error message in errorMessage
    */
    this.loginError=false;
    this.errorMessage="Sample Message";
  }
showLoginError= () =>{
  console.log(this.loginError);
  if(this.loginError){
    return(
      <div className="form-element">
        <p className="error">{this.errorMessage}</p>
      </div>
    )
  }
  else{
    return(
      null
    )
  }
}
  Form= () =>{
    return(
      <BrowserRouter>
        <Form>
          <i class="icon-user icon-large"></i>
      <Form.Text className="text-danger">
        <this.showLoginError/>
      </Form.Text>
    <Form.Group controlId="formBasicEmail">
      <Form.Label>Username</Form.Label>
      <Form.Control type="username" placeholder="Enter username" />
    </Form.Group>

    <Form.Group controlId="formBasicPassword">
      <Form.Label>Password</Form.Label>
      <Form.Control type="password" placeholder="Password" />
    </Form.Group>
    <Form.Group controlId="formBasicCheckbox">
      <Form.Check type="checkbox" label="  Keep Me Logged In" />
    </Form.Group>
    <Button variant="primary" type="submit">
      Login
    </Button>
    <Form.Group >
      <Link to="/dashboard/help">Need Help?</Link>
      <Link to="/dashboard/resetpassword">Forgot Password</Link>
    </Form.Group>
  </Form>
      </BrowserRouter>
    )
  }
  render(){
    this.checkLogin();
    this.readError();
    return(
      <this.Form/>
    )
  }
}
export default Login;
