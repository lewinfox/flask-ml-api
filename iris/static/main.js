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
        console.log("Prediction received:");
        console.log(responseObject);
        processResponse(responseObject);
      }
      catch(err) {
        let responseContainer = document.getElementById("response-container");
        responseContainer.innerHTML = err.message;
      }
    })

    // CASE: failure
    xhr.addEventListener("error", e => {
      alert("Something went wrong");
    })

    // Build the request
    xhr.open("POST", "/predict");

    // Send request
    xhr.send(fd);
  }

  const processResponse = data => {
    const pred_species = data.pred_class;
    const pred_prob = `${data.pred_prob * 100}%`
    let responseContainer = document.getElementById("response-container");
    let outputHTML = `
      <p><strong>Predicted class:</strong> ${pred_species}
      <br>
      <strong>Prediction confidence:</strong> ${pred_prob}
      </p>
      `
    responseContainer.innerHTML = outputHTML;
    responseContainer.classList.remove("invisible");
  }

  // Add the event listener to the form submit
  const form = document.getElementById("input-form");
  form.addEventListener("submit", e => {
    e.preventDefault();
    getPrediction(form);
  })

})
