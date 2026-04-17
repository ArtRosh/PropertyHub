import React, { useEffect } from "react";
import "./SiteTitle.css";

const SiteTitle = () => {
    useEffect(() => {
      const titleElement = document.getElementById("site-title");
      const titleText = titleElement.innerText;
      titleElement.innerText = "";
  
      for (let i = 0; i < titleText.length; i++) {
        const span = document.createElement("span");
        const letter = document.createTextNode(titleText[i]);
        span.appendChild(letter);
        span.classList.add("handwriting");
        span.style.animationDelay = `${i * 0.1}s`;
        titleElement.appendChild(span);
      }
    }, []);
  
    return (
      <div className="site-title-container">
        <h1 id="site-title">PropertyHub</h1>
      </div>
    );
  
};
  
  export default SiteTitle;
