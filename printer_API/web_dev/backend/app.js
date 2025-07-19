// // server.js
// const express = require("express");
// const cors = require("cors");
// const { spawn } = require('child_process');

// const app = express();
// const PORT = 3000;

// // Middleware
// app.use(cors());
// app.use(express.json());

// // Handle POST request
// app.post("/api/send", (req, res) => {
//   console.log("Received:", req.body);
//   const pythonProcess = spawn('python', ['../../BOM-TRACE/printer.py']);

//   res.json({ reply: "Request received on backend!" });
// });

// app.listen(PORT, () => {
//   console.log(`Server running at http://localhost:${PORT}`);
// });

const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");
const path = require("path");

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

app.post("/api/send", (req, res) => {
  const { printer_ip, label_width, label_height } = req.body;

  console.log("Received request from frontend:");
  console.log(`Printer IP: ${printer_ip}`);
  console.log(`Label Width: ${label_width}`);
  console.log(`Label Height: ${label_height}`);

  const scriptPath = path.resolve(__dirname, '../../BOM-TRACE/printer.py');

  const pythonProcess = spawn('python3', [scriptPath, printer_ip, label_width, label_height]);

  let output = "";
  let errorOutput = "";

  pythonProcess.stdout.on("data", (data) => {
    output += data.toString();
  });

  pythonProcess.stderr.on("data", (data) => {
    errorOutput += data.toString();
  });

  pythonProcess.on("close", (code) => {
    console.log(`Python process exited with code ${code}`);
    if (code === 0) {
      res.json({ reply: "Print successful", output });
    } else {
      res.status(500).json({ error: "Python script error", details: errorOutput });
    }
  });

  pythonProcess.on("error", (error) => {
    console.error("Failed to start Python process:", error);
    res.status(500).json({ error: "Failed to start Python process" });
  });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
