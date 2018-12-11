import * as responseHandler from "./response_handler.js";

console.log("main.js connected");

window.addEventListener("load", () => {

  const getPrediction = (form) => {

    // Instantiate a new request object
    let xhr = new XMLHttpRequest();

    // Collect form data
    let fd = new FormData(form);

    // CASE: Success
    xhr.addEventListener("load", e => {
      try {
        let responseObject = JSON.parse(e.target.responseText);

        // Log the response to the console to help debugging
        console.log("Prediction received:");
        console.log(responseObject);

        // Do stuff! This custom function will be defined per-application
        responseHandler.processResponse(responseObject);
      }
      catch(err) {
        let responseContainer = document.getElementById("response-container");
        responseContainer.innerHTML = err.message;
      }
    })

    // CASE: failure
    xhr.addEventListener("error", e => {
      alert(`Something went wrong: ${e}`);
    })

    // Build the request
    xhr.open("POST", "/predict");

    // Send request
    xhr.send(fd);
  }


  // Add the event listener to the form submit
  const form = document.getElementById("input-form");
  form.addEventListener("submit", e => {
    e.preventDefault();
    getPrediction(form);
  })

})
