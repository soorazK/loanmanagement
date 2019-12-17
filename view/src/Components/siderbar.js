import React from 'react';

class Sidebar extends react.component {
  constructor(props) {
    super(props);
  }
  submenu = (props) =>{
    return(
      <div onClick={props.click}>
      {props.menuName}
      </div>
    )
  }

  menu = (props) =>{
    
  }

  render(){

  }
}
