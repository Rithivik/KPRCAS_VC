const chatWindow = document.getElementById("chatWindow");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const quickReplies = document.getElementById("quickReplies");

function getTime() {
  const now = new Date();
  return now.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}

function addMessage(text, sender) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender);

  if (sender === "bot") {
    const avatar = document.createElement("img");
    avatar.classList.add("avatar-small");
    avatar.src = "/static/kprcas_logo.png";
    avatar.alt = "KPRCAS Logo";
    messageDiv.appendChild(avatar);
  }

  const wrap = document.createElement("div");
  wrap.classList.add("bubble-wrap");

  const bubble = document.createElement("div");
  bubble.classList.add("bubble");
  bubble.textContent = text;

  const time = document.createElement("span");
  time.classList.add("timestamp");
  time.textContent = getTime();

  wrap.appendChild(bubble);
  wrap.appendChild(time);
  messageDiv.appendChild(wrap);

  chatWindow.appendChild(messageDiv);
  chatWindow.scrollTop = chatWindow.scrollHeight;
  return messageDiv;
}

function showTyping() {
  const typingDiv = document.createElement("div");
  typingDiv.classList.add("message", "bot", "typing-indicator");

  const avatar = document.createElement("img");
  avatar.classList.add("avatar-small");
  avatar.src = "/static/kprcas_logo.png";
  avatar.alt = "KPRCAS Logo";

  const wrap = document.createElement("div");
  wrap.classList.add("bubble-wrap");

  const bubble = document.createElement("div");
  bubble.classList.add("bubble");
  bubble.innerHTML = "<span class='dot'></span><span class='dot'></span><span class='dot'></span>";

  wrap.appendChild(bubble);
  typingDiv.appendChild(avatar);
  typingDiv.appendChild(wrap);

  chatWindow.appendChild(typingDiv);
  chatWindow.scrollTop = chatWindow.scrollHeight;
  return typingDiv;
}

async function sendMessage(text) {
  const question = text || userInput.value.trim();
  if (!question) return;

  addMessage(question, "user");
  userInput.value = "";
  quickReplies.style.display = "none";

  const typingDiv = showTyping();

  try {
    const res = await fetch("/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });

    const data = await res.json();
    typingDiv.remove();

    if (data.error) {
      addMessage("Sorry, something went wrong: " + data.error, "bot");
    } else {
      addMessage(data.answer, "bot");
    }
  } catch (err) {
    typingDiv.remove();
    addMessage("Oops, I couldn't connect to the server.", "bot");
  }
}

sendBtn.addEventListener("click", () => sendMessage());
userInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") sendMessage();
});

document.querySelectorAll(".chip").forEach(chip => {
  chip.addEventListener("click", () => sendMessage(chip.textContent));
});