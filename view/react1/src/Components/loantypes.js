import React, {Component} from 'react'
import axios from 'axios'
class Loantypes extends Component{
  constructor(props){
  super(props)
  this.state={
  loantypes:[]
  }
}
  changeHandler = (event) => {
    this.setState({
    [event.target.name]:event.target.value
    })
  }

  onshandler = (event) => {
    event.preventDefault();
    console.log(this.state);
    const abc = sessionStorage.getItem('data');
    console.log(abc);
    axios.get('http://127.0.0.1/api/loantypes/',{
      headers:{
        'token': abc,
        'Accept':'application/json',
        'Content-Type':'application/json'
      }
    })
      .then(response => {
        this.setState({loantypes: response.data})
      })
      .catch(error => {
        console.log(error)
      })
  }
  render(){
    return(
      <div className="container">
        List of Loantypee
      <ul>
      {
          this.state.loantypes.map(loantypee =>

            <li key={loantypee.id}>{loantypee.interest}</li>
          )}
      </ul>
          <button onClick={this.onshandler}>submit</button>
      </div>
    );
  }
}
export default Loantypes;
