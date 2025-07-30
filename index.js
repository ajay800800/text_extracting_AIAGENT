const express = require("express");
const cors = require("cors");
const multer = require("multer");
const { exec } = require("child_process");
const path = require("path");
const fs = require("fs");

const app = express();
const PORT = process.env.PORT || 5000;


// Enable CORS
app.use(cors());

// Upload folder
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads/");
  },
  filename: (req, file, cb) => {
    const ext = path.extname(file.originalname);
    const filename = Date.now() + ext;
    cb(null, filename);
  },
});

const upload = multer({ storage });


// POST endpoint for file upload
app.post("/extract-text", upload.single("file"), (req, res) => {
  const filePath = path.join(__dirname, req.file.path);

  exec(`python3 extract_text_auto.py "${filePath}"`, (error, stdout, stderr) => {
    // Clean up file
    fs.unlinkSync(filePath);

    if (error) {
      console.error(stderr);
      return res.status(500).json({ error: "Failed to process file" });
    }

    return res.json({ text: stdout });
  });
});

app.listen(PORT, () => {
  console.log(`🟩 Server running at http://localhost:${PORT}`);
});
