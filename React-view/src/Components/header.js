// This is the class file for top header of the UI
/*
  Top header should contain logo in leftmost side followed by application name
  On rightmost side there should be UI element indicating if a user is logged in or not
*/
import React from 'react';
import {BrowserRouter,Link} from 'react-router-dom'
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
class Header extends React.Component{
  getIdentity= () => {
    /*
      MESSAGE TO SOORAZ
      get path to application logo and name from API
      I don't think this feature is still built in in backend so just skip this
      If API exist make a api call and provide value in appropriate variables below
    */
    this.logo="https://www.lineacademy.edu.np/media/Partners/MachineerTech.png";
    this.name="नेपाल आयल निगम कर्जा व्यवस्थापन प्रणाली";
  }
  getUserName= () =>{
    /*
      MESSAGE TO SOORAZ
      Get userName if user is logged in
      Set loggedIn variable to true if logged in else set it false.
    */
    this.loggedIn=false;
    this.userName="test user";
  }
  logIn= () =>{

  }
  LogOut= () =>{
    /*
      MESSAGE TO SOORAZ
      make logging out api call and then redirect to login page
      To redirect to li=ogin page just call this.logIN()
    */
    //make api call here
    this.logIN();
  }
  Identity= () =>{
    if(this.loggedIn){
      return(
        <Navbar.Text>
          Logged in as {this.userName}

        </Navbar.Text>
      )
    }
    else{
      return(
      null
    )
  }
}
  render(){
    this.getIdentity();
    this.getUserName();
    console.log(this.name);
    return(
      <Navbar bg="light" expand="lg">
  <Navbar.Brand href="/dashboard">
    <img
      alt=""
      src={this.logo}
      width="120"
      className="d-inline-block"
    />{'   '}
    {this.name}
  </Navbar.Brand>
    <Nav className="mr-auto"></Nav>
  <this.Identity/>
    {
      this.loggedIn===true?<Nav>
      <Nav.Link href="/dashboard/logout">Logout</Nav.Link>
      </Nav>:<Nav>
        <Nav.Link href="/dashboard/login">Login</Nav.Link>
      </Nav>
    }
</Navbar>

    )
  }
}
export default Header;
