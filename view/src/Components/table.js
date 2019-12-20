import React from 'react';
import {BrowserRouter, Link} from 'react-router-dom';
import * as Btable from 'react-bootstrap/Table';
class Table extends React.Component {
  constructor(props) {
    super(props);
    this.tData=props.tData;
    this.state={
      tData:props.tData,
      tHead:props.tHead,
      tType:props.tType
    }

  }
  state={
    tData:[],
    tHead:[],
    tType:[]
  }


  Thead= () =>{
    const HeadElements = Object.keys(this.state.tHead);
    const requirement = HeadElements.map((key)=>
    <th key={key}>{this.state.tHead[key]}</th>
    )
    return(
      <thead>
        <tr>
          {requirement}
        </tr>
      </thead>
    )

  }

Tbody = () =>{
  
  return(
    <tr>
      Hello
    </tr>
  )
}


  render(){
    return(
      <table>
        <this.Thead/>
        <this.Tbody/>
      </table>
    )
  }
}

export default Table;
