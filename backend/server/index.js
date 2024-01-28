// Imports stuff for file
const path = require("path");
const fs = require("fs");
// const multer = require("multer");
// Creates the basic server
const express = require("express");
// const bodyParser = require("body-parser");
const cors = require("cors");
const app = express();
const port = 3000;
// Python runner
const { spawn } = require("child_process");

// Middleware so taht we cant
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
  const name = FILES_DIR + "1.png";
  const data = req.body.image.replace(/^data:image\/\w+;base64,/, "");
  const buf = Buffer.from(data, "base64");
  fs.writeFileSync(name, buf /* callback will go here */);
  console.log("file saved");

  // await fetch from python
  const python = spawn("python", ["-u", "../model3.py"]);
  let dataToSend = "";

    // python.stderr.on("data", function (data) {
    //   console.log("Pipe data from python script ...", data.toString());
    //   // dataToSend.push(data.toString());
    // });

  python.stdout.on("data", function (data) {
    console.log("Pipe data from python script ...", data.toString());
    dataToSend = data.toString();
  });
  // in close event we are sure that stream from child process is closed
  python.on("close", (code) => {
    console.log(`child process close all stdio with code ${code}`);

    // send data to browser
    // res.send(dataToSend);

    if (dataToSend == "Up") {
      res.send({ up: 1, down: 0 });
    } else if (dataToSend == "Down") {
      res.send({ up: 0, down: 1 });
    } else {
      res.send({ up: 0, down: 0 });
    }

  });

});

// Starts express on a port
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
