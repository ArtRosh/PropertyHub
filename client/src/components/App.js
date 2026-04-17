import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Properties from './Properties'
import NewPropertyForm from './NewPropertyForm'
import Images from './Images'
import NewImage from './NewImage'
import Reviews from './Reviews'
import NewReviewForm from './NewReviewForm.js'
import Login from "./Login.js";
import NavBar from "./NavBar.js";
import SignupForm from "./SignUp.js";
import Logout from "./Logout.js";
import { DarkModeProvider } from "./DarkModeContext.js";
import SiteTitle from "../SiteTitle.js";
import "../index.css";


function App() {

  

  const [properties, setProperties] = useState([])
  const [reviews, setReviews] = useState([])
  const [images, setImages] = useState([])
  const [login, setLogin] = useState([])
  const [signup, setSignup] = useState([])
  const [logout, setLogout] = useState([]) 
  
  useEffect(() => {
    fetch('/properties')
    .then((res) => res.json())
    .then((data) => setProperties(data))
  }, [])

  useEffect(() => {
    fetch('/reviews')
    .then((res) => res.json())
    .then((data) => setReviews(data))
  }, [])

  useEffect(() => {
    fetch('/images')
    .then((res) => res.json())
    .then((data) => setImages(data))
  }, [])
  

  
  return (
    <DarkModeProvider className='.dark'>
    <div className="background-container">
      <div className="background-image"></div>
    </div>
  
  <Switch>
    <Route exact path='/'>
    
      <SiteTitle/> 
      <NavBar/>
    </Route>
    <Route exact path= '/login'>
      <Login login = {login} setLogin = {setLogin}/>
  </Route>
  <Route exact path = '/signup'>
      <SignupForm signup = {signup} setSignUp = {setSignup}/>
  </Route>
  <Route exact path = '/logout'>
      <Logout logout = {logout} setLogout = {setLogout}/>
  </Route>
  <Route exact path = '/properties'>
      <Properties properties = {properties} setProperties = {setProperties} setImages={setImages} setReviews={setReviews}/>
  </Route>
  <Route exact path = '/newproperty'>
      <NewPropertyForm setProperties = {setProperties}/>
  </Route>
  <Route exact path = '/properties/:id/reviews'>
      <Reviews reviews = {reviews} setReviews={setReviews} />
  </Route>
        <Route exact path = '/newreview'>
          <NewReviewForm setReviews = {setReviews}/>
        </Route>
        <Route exact path = '/properties/:id/images'>
          <Images images = {images} setImages = {setImages}/>
        </Route>
        <Route exact path = '/newimage'>
          <NewImage setImages = {setImages}/>
        </Route>
      </Switch>
  </DarkModeProvider>
  
  );
}

export default App;
        

       
        