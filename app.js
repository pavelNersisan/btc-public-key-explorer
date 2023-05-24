document.getElementById("btnSubmit").addEventListener("click", function() {
  const address = document.getElementById("address").value;
  fetch(`https://blockchain.info/rawaddr/${address}`)
    .then(response => response.json())
    .then(data => {
      document.getElementById("response").innerHTML = JSON.stringify(data, null, 2);
    });
});