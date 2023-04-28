import React from "react"
import ReactDOM from "react-dom/client"
import App from "./src/App"
import "./styles.css"
import { BrowserRouter } from "react-router-dom"
import GradientMotionBackground from "./src/GradientBg"
import Footer from "./src/pages/Footer"

const root = ReactDOM.createRoot(document.getElementById("root"))
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
      <GradientMotionBackground/>
      <Footer/>
    </BrowserRouter>
  </React.StrictMode>
)