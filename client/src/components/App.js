import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";

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