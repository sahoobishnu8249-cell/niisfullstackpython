import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import React, { Component } from 'react'
import App from './App1.jsx'

function Welcome() {
  return <h1>Hello User!</h1>
}
class MyComponent extends Component {
  render() {
    return <p>This is a class component</p>
  }
}

function App() {
  

  return (
    <div>
    <b>Welcome react</b><br/>
    <i>hi</i> 
    <APP1/>
    <Welcome/>
    <MyComponent/>

    </div>
  )
}

export default App
