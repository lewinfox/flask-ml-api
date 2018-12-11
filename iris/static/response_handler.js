// This is a custom function that is used to handle the model output. It should
// contain all the the code necessary to present the data to the user
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

export {processResponse};
