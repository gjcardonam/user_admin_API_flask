let input = document.getElementById("fileID");
let CSVname = document.getElementById("CSVname");
let submit = document.getElementById("submit");

input.addEventListener("change", () => {
  let inputFile = document.querySelector("input[type=file]").files[0];

  CSVname.innerText = inputFile.name;
  submit.style.display = "";
});
