import React, {Component} from 'react'
import axios from 'axios'


class Logout extends Component{
  constructor(props){
  super(props)
//  this.state={

//  }
}
  changeHandler = (event) => {
    this.setState({
    [event.target.name]:event.target.value
    })
  }

  onshandler = (event) => {
    event.preventDefault();
    console.log(this.state);
    axios.post('http://127.0.0.1/api/logout/')
      .then(response => {
        const token2=sessionStorage.getItem('data');
        console.log(token2);
      })
      .catch(error => {
        console.log(error)
      })
  }
  render(){
  //  const {username,password}=this.state
    return(
      <div className="container">
            <button type="submit" onClick={this.onshandler}>
            logout </button>
      </div>
          )
  }


}
export default Logout;
