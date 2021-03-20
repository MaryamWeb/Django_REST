import axios from 'axios';
import React, {useState} from 'react';

const Login=()=>{
    const [username, setUsername]          = useState("") 
    const [password, setPassword]          = useState("")     

    const handleLogin = (e) => {  
        e.preventDefault();
        const logUser={ username, password}
        axios
          .post('http://localhost:7000/api-token-auth/?format=json', logUser)
          .then((res) => {
               console.log(res)
            } )  
        }
    return(
        <>
            <div className="col-md-12">
                <div className="form-group col-md-6 mx-auto">
                    <input type="username" className="form-control" placeholder="username*" onChange={(e) => setUsername(e.target.value)} value={username}/>
                </div>
                <div className="form-group col-md-6 mx-auto">
                    <input type="password" className="form-control" placeholder="Password *" onChange={(e) => setPassword(e.target.value)} value={password}/>
                </div>
                <div className="form-group col-md-6 mx-auto">
                    <input type="submit" value="Login" onClick={handleLogin}/>
                </div>
            </div>
        </>
    )
}

export default Login