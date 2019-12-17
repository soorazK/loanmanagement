// This is the class file for top header of the UI
/*
  Top header should contain logo in leftmost side followed by application name
  On rightmost side there should be UI element indicating if a user is logged in or not
*/
import React from 'react';
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
    this.loggedIn=true;
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
  Identity = () =>{
    return(
      <div className="identity"><img className="logo" width="100px" src={this.logo} alt="Logo"></img><h3 className="app-name">{this.name}</h3></div>
    )
  }
  Status= () =>{
    if(this.loggedIn){
      return(
        <div className="user-detail">
          <i className="icon-user"></i>
          <p className="user-name">  Welcome, {this.userName}</p>
          <button className="logout" onClick={this.logOut}>Logout</button>
        </div>
      )
    }
    return(
      <div className="user-detail">
        <i className="icon-user"></i>
        <button className="login" onClick={this.logIn}>Login</button>
      </div>
    )
  }
  render(){
    this.getIdentity();
    this.getUserName();
    console.log(this.name);
    return(
      <div>
      <this.Identity />
      <this.Status />
      </div>
    )
  }
}
export default Header;
