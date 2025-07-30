import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://localhost:5000/extract-text", formData, {
      headers: { "Content-Type": "multipart/form-data" }
    });

    setText(res.data.text);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>📄 Text Extractor</h2>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload} disabled={!file}>Extract Text</button>
      <pre style={{ whiteSpace: "pre-wrap", marginTop: 20 }}>{text}</pre>
    </div>
  );
}

export default App;
