import { useState } from "react";
import axios from "axios";
import AnimatedBackground from "./components/AnimatedBackground";
import "./App.css";
import robotImg from "./assets/robot.png";


function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([
    { type: "bot", text: "Hi 👋" },
    { type: "bot", text: "How can I help you today?" }
  ]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMsg = message;
    setChat(prev => [...prev, { type: "user", text: userMsg }]);
    setMessage("");

    try {
      const res = await axios.post("http://localhost:5000/chat", {
        message: userMsg
      });

      setChat(prev => [...prev, { type: "bot", text: res.data.reply }]);
    } catch {
      setChat(prev => [...prev, { type: "bot", text: "Server error" }]);
    }
  };

  return (
    <div className="app">

      <AnimatedBackground />

      <div className="heading">ChatBot-AI</div>
      <img src={robotImg} alt="robot" className="right-image" />


      <div className="chat-box">

        <div className="messages">
          {chat.map((msg, i) => (
            <div key={i} className={msg.type}>
              {msg.text}
            </div>
          ))}
        </div>

        <div className="input-area">
          <input
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Ask anything"
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <button onClick={sendMessage}>➤</button>
        </div>

      </div>

    </div>
  );
}

export default App;
