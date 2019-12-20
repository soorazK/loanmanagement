import React from 'react';
import Table from '../table.js';
import * as tData from '../data.json';

let tHead=
  {
    _id: 'SN',
    index: 'Index',
    guid: 'GuId',
    isActive: 'Active',
    balance: 'Balance',
    picture: 'Image'
  };
  let tType=
    {
      _id: 'text',
      index: 'text',
      guid: 'text',
      isActive: 'bool',
      balance: 'text',
      picture: 'image'
    };
class LoanList extends React.Component {
render (){
  return(
    <div><Table tData={tData} tHead={tHead} tType={tType}/></div>
  )
}
}
export default LoanList;
