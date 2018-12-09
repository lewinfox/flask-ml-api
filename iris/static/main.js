console.log("main.js connected");

window.addEventListener("load", () => {

  const getPrediction = (form) => {
    let xhr = new XMLHttpRequest();

    // Collect form data
    let fd = new FormData(form);

    // Convert to JS object so it can be converted to JSON
    let fd_object = {};
    fd.forEach((value, key) => {
      fd_object[key] = value;
    });
    let fd_json = JSON.stringify(fd_object);

    // CASE: Success
    xhr.addEventListener("load", e => {
      console.log(e.target.resposeText);
      let responseObject = JSON.parse(e.target.responseText);
      console.log(responseObject);
      processResponse(responseObject);
    })

    // CASE: failure
    xhr.addEventListener("error", e => {
      alert("Something went wrong");
    })

    // Build the request
    xhr.open("POST", "/predict");

    // Send request
    xhr.send(fd_json);
  }

  const processResponse = data => {
    console.log(data);
    const pred_species = data.pred_class;
    const pred_prob = data.pred_prob
    let responseContainer = document.getElementById("response-container");
    let outputHTML = `
      <p><strong>Predicted class:</strong> ${pred_species}
      <br>
      <strong>Probability:</strong> ${pred_prob}
      </p>
      `
    responseContainer.innerHTML = outputHTML;
  }

  // Add the event listener to the form submit
  const form = document.getElementById("input-form");
  form.addEventListener("submit", e => {
    e.preventDefault();
    console.log("click");
    getPrediction(form);
  })

})
