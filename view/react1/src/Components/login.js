import React, {Component} from 'react'
import axios from 'axios'


class Login extends Component{
  constructor(props){
  super(props)
  this.state={
    username:'',
    password:''
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
    axios.post('http://127.0.0.1/api/login/',this.state)
      .then(response => {
        const token1 = response.data.token;
        console.log(token1);
        sessionStorage.setItem('data',token1  );
        const token2= sessionStorage.getItem('data');
        console.log(token2);
      })
      .catch(error => {
        console.log(error)
      })
  }
  render(){
    const {username,password}=this.state
    return(
      <div className="container">
        <form onSubmit={this.onshandler}>
          <div className="form_element">
            Enter username:
            <input
              type="text"
              name="username"
              onChange={this.changeHandler}
              value={username}/>
            </div>
            <div className="form_element">

              Enter password:
              <input
                type="text"
                name="password"
                onChange={this.changeHandler}
                value={password} />
            </div>
            <button type="submit">
            submit </button>
        </form>
      </div>
          )
  }


}
export default Login;
