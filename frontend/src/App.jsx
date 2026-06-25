import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!message.trim()) return;

    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message,
        }),
      });

      const data = await res.json();

      setResponse(data);
    } catch (error) {
      console.error(error);
      alert("Backend connection failed");
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="glass-card">
        <h1>AI Refund Agent</h1>

        <p className="subtitle">
          Smart refund decisions powered by AI
        </p>

        <div className="input-section">
          <input
            type="text"
            placeholder="Example: I want a refund for ORD1003"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />

          <button onClick={handleSubmit}>
            {loading ? "Analyzing..." : "Submit"}
          </button>
        </div>

        {response && (
          <div className="result-card">
            <div
              className={
                response.decision === "APPROVED"
                  ? "decision approved"
                  : "decision denied"
              }
            >
              {response.decision}
            </div>

            <div className="field">
              <h3>Decision</h3>
              <p>{response.decision}</p>
            </div>

            <div className="field">
              <h3>Reason</h3>
              <p>{response.reason}</p>
            </div>

            <div className="field">
              <h3>Explanation</h3>
              <p>{response.explanation}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;