import { useState } from 'react'
import { Icon } from 'react-icons-kit'
import { eye } from 'react-icons-kit/feather/eye'
import { eyeOff } from 'react-icons-kit/feather/eyeOff'
import { mail } from 'react-icons-kit/feather/mail'
import { user } from 'react-icons-kit/feather/user'

import '../styles/register.css'

export default function Register() {
  const [showPassword, setShowPassword] = useState(false);
  const [icon, setIcon] = useState(eyeOff)

  function submit(e: React.SyntheticEvent) {
    const target = e.target as typeof e.target & {
      username: { value: string }
    };

    const username = target.username.value; 
    alert(`${username}`)
  }

  function handleToggle() {
    setShowPassword(!showPassword);
    setIcon(!showPassword ? eye : eyeOff)
  }

  return <div>
    <h1 style={{
      fontSize: "64px"
    }}>Create your Concursus.</h1>
    <form id="register-form" onSubmit={submit}>
      <div className="row">
      <div className="input">
        <input required name="username" placeholder="username" type="text" maxLength={50}/>
        <span>
          <Icon icon={user} size={30}/>
        </span>
      </div>
      <div className="input">
        <input required name="password" placeholder="password" type={showPassword ? "text": "password"}/>
        <span onClick={handleToggle}>
          <Icon icon={icon} size={30}/>
        </span>
      </div>
      </div>
      <div className="row">
      <div className="input">
        <input required name="email" placeholder="email" type="email"/>
        <span>
          <Icon icon={mail} size={30}/>
        </span>
      </div>
      <div className="input">
        <input required name="confirm-password" placeholder="confirm password" type={showPassword ? "text": "password"}/>
        <span onClick={handleToggle}>
          <Icon icon={icon} size={30}/>
        </span>
      </div>
      </div>
      <div className="row">
        <div className="input">
          <button>CREATE ACCOUNT</button>
        </div>
        <div className="input">
          <button id="login-instead">LOGIN INSTEAD</button>
        </div>
      </div>
    </form>
  </div>
}
