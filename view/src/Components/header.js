import React from 'react';
class Header extends React.Component{
  constructor(props){
    super(props);
    this.siteName=props.name;
    this.logo=props.logo;
  }
  Status = (props) =>{
    if (props.userName ==''){
      return(
        <div className="flex-item">
          Login
        </div>
      )
    }
    else {
      return(
        <div className="flex-item">
          Welcome, {props.userName}
        </div>
      )
    }
  }
  Identity = () =>{
    return(
      <div className="flex-item brand-name">
      <a className="navbar-brand">
          <img src={this.logo} alt="Logo"/>
           नेपाल आयल निगम
      </a>
      </div>
    )
  }
  render(){
    console.log("here:");
    console.log(this.siteName);
    return(
      <div className="row row-flex navbar">
        <this.Identity/>
        <this.Status/>
      </div>
    )
    }
};
export default Header;
