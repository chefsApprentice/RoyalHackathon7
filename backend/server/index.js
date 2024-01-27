// Imports stuff for file
const path =require("path");
const fs = require("fs");
// Creates the basic server
const express = require("express");
const app = express();
const port = 3000;

const FILES_DIR = path.join(__dirname, "./../images");

// Just for testing
app.get("/", (req, res) => {
  res.send("Hello World!");
});

// Main url, recieves img and serves response
app.post("/img", (req, res) => {
  let  image  = req.body;
  console.log("img:", image)
  console.log("type:", typeof(img))

  fs.writeFile(FILES_DIR, image, function (err) {
    if (err) {
      return console.log(err);
    }
    console.log("The file was saved!");
  });

  res.send({
    resRecieved: true,
    result: [1, 2],
  });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
