# 🧠 Desktop AI Agent with MCP & LangChain

This project is a **local desktop AI agent** built using **LangChain** and the **Model Context Protocol (MCP)**.  
It combines **custom Python tools** with **MCP servers** to let an LLM safely interact with the local system, external services, and persistent memory.

---

## ✨ What this agent can do

The agent can intelligently decide when to:
- 🗂️ Read/write files on the local filesystem
- 🖥️ Execute system commands
- 🔍 Search the web (DuckDuckGo)
- 📊 Inspect running processes & system info
- 🧠 Store and recall memory/context
- 🌐 Control a browser using Playwright
- 🐙 Interact with GitHub
- ☁️ Access Google Drive
- 🧩 Reason step-by-step for complex tasks (sequential thinking)

All tools are exposed through **MCP** and dynamically loaded into the agent.

---

## 🏗️ Architecture Overview

### MCP Tool Servers
The agent connects to multiple MCP servers using `MultiServerMCPClient`:

- **Filesystem** – Local file access
- **Playwright** – Browser automation
- **Memory** – Persistent context storage
- **Sequential Thinking** – Structured reasoning
- **GitHub** – Repository interaction
- **Google Drive** – File access

These servers are started via `npx` or custom Python MCP servers.

---

### Custom Python Tools
Alongside MCP tools, the agent includes native Python tools such as:
- DuckDuckGo search
- Command execution
- Process & system monitoring

Both MCP tools and Python tools are merged into a single toolset at runtime.

---

### LangGraph + LangChain Agent
- Uses a system prompt defining the agent as a desktop assistant
- Dynamically decides when to call tools
- Maintains conversation state in memory
- Runs in an interactive CLI loop

---


📄 License

This project is for experimentation and learning purposes.

