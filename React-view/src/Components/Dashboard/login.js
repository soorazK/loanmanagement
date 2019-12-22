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
import Cookie from 'js-cookie';
import axios from 'axios';
class Login extends React.Component{
  constructor (props){
    super(props);
    this.state={
      loggedIn: Cookie.get('loggedIn'),
      token: Cookie.get('token')
    };
    this.checkLogin=this.checkLogin.bind(this);
    this.changeHandler=this.changeHandler.bind(this);
    this.login=this.login.bind(this);
  };

  checkLogin = () =>{
    if(this.state.loggedIn){
      this.props.history.push('/dashboard');
    }
  }
  changeHandler = (event) =>{
    let name=event.target.name;
    let value=event.target.value;
    this.setState({
      [name]: [value]
    });
  }
  async login(){
    /*
      MESSAGE TO SOORAZ
      check if there is any login error message in session
      if yes set loginError to true and put error message in errorMessage
    */

        const data = {
        username :this.state.username,
        password :this.state.password
      };
    axios.post(`http://127.0.0.1/api/login`, { data })
      .then(res => {
        console.log(res);
        console.log(res.data);
      })

    
  }
showLoginError= () =>{
  if(this.state.loginError){
    return(
      <div className="form-element">
        <p className="error">{this.state.errorMessage}</p>
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
          <i className="icon-user icon-5x"></i>
      <Form.Text className="text-danger">
        <this.showLoginError/>
      </Form.Text>
    <Form.Group controlId="formBasicEmail">
      <Form.Label>Username</Form.Label>
      <Form.Control type="text" name="username" onChange={this.changeHandler} placeholder="Enter username" />
    </Form.Group>

    <Form.Group controlId="formBasicPassword">
      <Form.Label>Password</Form.Label>
      <Form.Control type="password" name="password" onChange={this.changeHandler} placeholder="Password" />
    </Form.Group>
    <Form.Group controlId="formBasicCheckbox">
      <Form.Check type="checkbox"  name="long" onChange={this.changeHandler} label="Keep Me Logged In" />
    </Form.Group>
    <Button variant="primary" onClick={this.login}>
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
    return(
      <this.Form/>
    )
  }
}
export default Login;
