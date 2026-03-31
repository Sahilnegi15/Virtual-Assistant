import React, { useState } from "react";

function AssistantUI() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [mode, setMode] = useState("single");

  const API_BASE = "http://127.0.0.1:8000";

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setResponse("");

    try {
      const endpoint = mode === "multi" ? "/multi-agent" : "/ask";
      const res = await fetch(`${API_BASE}${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      setResponse(data.answer);
      setHistory((prev) => [{ q: question, a: data.answer }, ...prev]);
      setQuestion("");
    } catch {
      setResponse("❌ Error: Backend not reachable");
    }
    setLoading(false);
  };

  const runAutomation = async () => {
    setLoading(true);
    try {
      await fetch(`${API_BASE}/run-task`);
      alert("✅ Automation task executed!");
    } catch {
      alert("❌ Failed to run automation");
    }
    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🧠 Smart AI Assistant</h1>

      {/* Mode Toggle */}
      <div style={styles.modeToggle}>
        <button
          onClick={() => setMode("single")}
          style={mode === "single" ? styles.activeBtn : styles.btn}
        >
          Single Agent
        </button>
        <button
          onClick={() => setMode("multi")}
          style={mode === "multi" ? styles.activeBtn : styles.btn}
        >
          Multi-Agent
        </button>
      </div>

      {/* Ask Question Box */}
      <div style={styles.askBox}>
        <input
          type="text"
          placeholder="Ask a question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          style={styles.input}
        />
        <button onClick={handleAsk} style={styles.askBtn}>
          Ask
        </button>
      </div>

      {/* Automation */}
      <button onClick={runAutomation} style={styles.autoBtn}>
        ⚙️ Run Automation Task
      </button>

      {/* Loading */}
      {loading && <p style={styles.loading}>⏳ Thinking...</p>}

      {/* Response */}
      {response && (
        <div style={styles.responseBox}>
          <h3>Response:</h3>
          <p>{response}</p>
        </div>
      )}

      {/* History */}
      <div style={styles.history}>
        <h3>📜 History</h3>
        {history.map((item, index) => (
          <div key={index} style={styles.historyItem}>
            <strong>Q:</strong> {item.q}
            <br />
            <strong>A:</strong> {item.a}
          </div>
        ))}
      </div>
    </div>
  );
}

export default AssistantUI;

const styles = {
  container: {
    padding: "2rem",
    maxWidth: "800px",
    margin: "auto",
    fontFamily: "Arial",
    backgroundColor: "#000",
    color: "#fff",
    minHeight: "100vh",
  },
  title: {
    textAlign: "center",
    marginBottom: "1rem",
  },
  modeToggle: {
    marginBottom: "1rem",
    textAlign: "center",
  },
  btn: {
    padding: "8px 15px",
    marginRight: "10px",
    cursor: "pointer",
    background: "#444",
    color: "#fff",
    border: "none",
    borderRadius: "4px",
  },
  activeBtn: {
    padding: "8px 15px",
    marginRight: "10px",
    background: "#007bff",
    color: "#fff",
    cursor: "pointer",
    border: "none",
    borderRadius: "4px",
  },
  askBox: {
    display: "flex",
    gap: "10px",
    marginBottom: "1rem",
    padding: "1rem",
    backgroundColor: "#111",
    borderRadius: "8px",
    border: "1px solid #333",
  },
  input: {
    flex: 1,
    padding: "10px",
    fontSize: "16px",
    borderRadius: "4px",
    border: "1px solid #555",
    backgroundColor: "#222",
    color: "#fff",
  },
  askBtn: {
    padding: "10px 20px",
    cursor: "pointer",
    background: "#28a745",
    color: "#fff",
    border: "none",
    borderRadius: "4px",
  },
  autoBtn: {
    marginBottom: "1rem",
    padding: "10px",
    background: "#ff9800",
    color: "#fff",
    cursor: "pointer",
    border: "none",
    borderRadius: "4px",
  },
  loading: {
    textAlign: "center",
    marginTop: "1rem",
  },
  responseBox: {
    marginTop: "1rem",
    padding: "1rem",
    background: "#111",
    borderRadius: "8px",
  },
  history: {
    marginTop: "2rem",
  },
  historyItem: {
    padding: "10px",
    borderBottom: "1px solid #333",
  },
};
