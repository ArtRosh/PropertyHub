import React, {useState} from 'react';
import { useHistory } from 'react-router-dom/cjs/react-router-dom';


function Login({setLogin}){
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const history = useHistory()

    console.log(password)
    console.log(username)
    const handleLogin = (e) => {
    e.preventDefault()
    fetch('/login',{
       method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({username, password})
    })
    .then(res => res.json())
    .then(user => { setLogin(user)})  
    history.push('/')
    }
    
    return (
        <form onSubmit={handleLogin}>
            <label>
                Username:
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    />
            </label>
            <br />
            <label>
                Password:
                <input
                    type='password'
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    />
            </label>
            <br />
            <button type='submit'>Log In</button>
        </form>
    )
    
}   

export default Login