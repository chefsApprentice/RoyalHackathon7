// Imports stuff for file
const path = require("path");
const fs = require("fs");
// const multer = require("multer");
// Creates the basic server
const express = require("express");
const bodyParser = require('body-parser')
const cors = require("cors");
const app = express();
const port = 3000;

app.use(cors());


var urlencodedParser = bodyParser.urlencoded({ extended: false })

const FILES_DIR = path.join(__dirname, "./../images");

// Just for testing
app.get("/", (req, res) => {
  res.send("Hello World!");
});

 app.post("/img", urlencodedParser,  async (req, res) => {
  // console.log("req" + req)
  await console.log(req.body);

});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
