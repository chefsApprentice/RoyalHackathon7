// Imports stuff for file
const path = require("path");
const fs = require("fs");
const multer = require("multer");
// Creates the basic server
const express = require("express");
const cors = require("cors");
const app = express();
const port = 3000;

app.use(cors());

const FILES_DIR = path.join(__dirname, "./../images");

// Just for testing
app.get("/", (req, res) => {
  res.send("Hello World!");
});

const storageEngine = multer.diskStorage({
  destination: FILES_DIR,
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}--${file.originalname}`);
  },
});

const upload = multer({
  storage: storageEngine,
  limits: { fileSize: 100000000000000 },
});

// Main url, recieves img and serves response
app.post("/img", upload.single("image"), (req, res) => {
  if (req.file) {
    let image = req;
    console.log("img:", image);
    console.log("type:", typeof img);
    res.send("Single file uploaded successfully");
  } else {
    res.status(400).send("Please upload a valid image");
  }

  //   console.log("req", req);

  //   fs.writeFile(FILES_DIR, image, function (err) {
  //     if (err) {
  //       return console.log(err);
  //     }
  //     console.log("The file was saved!");
  //   });

  //   res.send({
  //     resRecieved: true,
  //     result: [1, 2],
  //   });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
