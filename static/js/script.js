function updatePrice(selectId, priceId) {
  var selectElement = document.getElementById(selectId);
  var priceElement = document.getElementById(priceId);
  var selectedValue = selectElement.value;
  priceElement.textContent = "+ " + String.fromCharCode(8377) + " "+ selectedValue;
}
var inputField = document.getElementById("customchassis");
document.getElementById("chassis").addEventListener("change", function () {
if (this.checked) {
    console.log("Selected value/label: " + inputField.value);
}
});

var inputField1 = document.getElementById("customspringCut");
document.getElementById("springCut").addEventListener("change", function () {
    if (this.checked) {
        console.log("Selected value/label: " + inputField1.value);
    }
});

var inputField2 = document.getElementById("custombodyType");

document.getElementById("bodyType").addEventListener("change", function () {
    if (this.checked) {
        console.log("Selected value/label: " + inputField2.value);
    }
});