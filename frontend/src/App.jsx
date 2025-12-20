import { useState } from "react";
import axios from "axios";

const API = "http://127.0.0.1:8000";

function App() {
  const [prompt, setPrompt] = useState("");
  const [file, setFile] = useState(null);
  const [plan, setPlan] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const runAI = async () => {
    if (!prompt || !file) {
      alert("Enter prompt and upload video");
      return;
    }

    setLoading(true);

    try {
      // 1. Generate plan
      const planRes = await axios.post(`${API}/plan`, {
        prompt: prompt,
      });

      setPlan(planRes.data);

      // 2. Execute video
      const formData = new FormData();
      formData.append("file", file);

      const execRes = await axios.post(`${API}/execute`, formData);

      setResult(execRes.data);
    } catch (err) {
      alert("Error connecting to backend");
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>EditorBrain AI</h2>

      <input
        type="text"
        placeholder="Enter editing prompt"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <br /><br />

      <input
        type="file"
        accept="video/*"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={runAI} disabled={loading}>
        {loading ? "Processing..." : "Run AI Edit"}
      </button>

      {plan && (
        <>
          <h3>AI Edit Plan</h3>
          <pre>{JSON.stringify(plan, null, 2)}</pre>
        </>
      )}

      {result && (
        <>
          <h3>Execution Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </>
      )}
    </div>
  );
}

export default App;
