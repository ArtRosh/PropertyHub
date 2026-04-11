import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Properties from './Properties';
import Reviews from './Reviews';
import Images from './Images';
import NewPropertyForm from './NewPropertyForm';
import NewReviewForm from './NewReviewForm';
import NewImage from './NewImage';
import Login from './Login';
import SignupForm from './SignUp';
import Logout from './Logout';

function App() {
  const [properties, setProperties] = useState([]);
  const [reviews, setReviews] = useState([]);
  const [images, setImages] = useState([]);

  useEffect(() => {
    fetch("/properties")
      .then((res) => res.json())
      .then(setProperties);
  }, []);

  useEffect(() => {
    fetch("/reviews")
      .then((res) => res.json())
      .then(setReviews);
  }, []);

  useEffect(() => {
    fetch("/images")
      .then((res) => res.json())
      .then(setImages);
  }, []);

  return (
    <Switch>
      <Route exact path="/">
        <h1>Home</h1>
      </Route>
    </Switch>
  );
}

export default App;