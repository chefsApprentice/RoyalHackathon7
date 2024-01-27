// Imports stuff for file
const path = require("path");
const fs = require("fs");
// const multer = require("multer");
// Creates the basic server
const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const app = express();
const port = 3000;

app.use(cors());
app.use(express.json({ limit: "50mb" }));
app.use(express.urlencoded({ limit: "50mb" }));

const FILES_DIR = path.join(__dirname, "./../images/");

let count = 0;

// Just for testing
app.get("/", (req, res) => {
  res.send("Hello World!");
});

//  app.post("/img", urlencodedParser,  (req, res) => {
app.post("/img", (req, res) => {
  // console.log("req" + req)
  count++;
  let name = FILES_DIR + count + ".png";
  var data = req.body.image.replace(/^data:image\/\w+;base64,/, "");
  var buf = Buffer.from(data, "base64");
  fs.writeFileSync(name, buf /* callback will go here */);
  console.log("file saved");

// await fetch from python

  res.send({
    up: 1,
    down: 3
  })
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
