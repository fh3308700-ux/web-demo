const multer = require('multer');
const path = require('path');

// Set up multer to store the file temporarily in /tmp directory
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, '/tmp/uploads');  // Store temporarily in /tmp/uploads directory
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname));  // Add timestamp to file name
  },
});

const upload = multer({ storage: storage }).single('file');

module.exports = (req, res) => {
  upload(req, res, (err) => {
    if (err) {
      return res.status(500).json({ error: 'Error uploading file' });
    }

    const file = req.file;
    if (!file) {
      return res.status(400).json({ error: 'No file uploaded' });
    }

    // Temporary file path where the file is saved
    const filePath = `/tmp/uploads/${file.filename}`;
    console.log('File uploaded to:', filePath);

    // Respond with the file's temporary path or success message
    return res.status(200).json({
      message: 'File uploaded successfully',
      filePath: filePath,
    });
  });
};
