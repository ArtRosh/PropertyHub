import React, { useState } from "react";
import { Switch, Route } from "react-router-dom";

function App() {
  const [properties, setProperties] = useState([]);
  const [reviews, setReviews] = useState([]);
  const [images, setImages] = useState([]);

  return (
    <Switch>
      <Route exact path="/">
        <h1>Home</h1>
      </Route>
    </Switch>
  );
}

export default App;