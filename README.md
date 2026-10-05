# Codewords

> Your local AI coding partner.

Codewords is a private, local-first AI coding IDE and agent for Windows.

Write code, explore your project, search and edit files, run commands and tests, and work with an AI agent — all from one application.

Codewords runs its AI locally using [Ollama](https://ollama.com/), so your source code stays on your machine. No cloud account, API key, or monthly subscription is required.

## ✨ Features

- 🤖 **Local AI coding agent** — Ask the agent to understand, modify, debug, and improve your project.
- 🧠 **Project memory** — Persistent project knowledge, sessions, tasks, and custom skills.
- 🛠️ **Powerful agent tools** — Read, search, edit, create, move and delete files, run commands, run tests, inspect code, and work with Git.
- 📋 **Planning & tasks** — Break large coding jobs into plans and track multi-step work.
- 👨‍💻 **Specialists** — Explorer, Architect, Debugger, Reviewer, and Tester helpers for focused analysis.
- 🔍 **Find & Replace** — Match case, whole word, regex, selection and workspace-wide search and replacement.
- 💻 **Built-in terminal** — Run PowerShell/cmd commands directly inside your workspace.
- 📝 **Code editor** — Tabs, syntax highlighting, line numbers, undo/redo, zoom, and support for 25+ languages.
- 🔐 **Safety & permissions** — Risk-based command permissions, approval for dangerous actions, diffs, backups, and a Stop button.
- 🌐 **Git integration** — Inspect status, diffs, history, blame, and more through the AI agent.
- 📴 **Works offline** — After the initial Ollama/model setup, Codewords can work without an internet connection.

## 🧠 How it works

Codewords combines a desktop code editor with a local AI agent.

You describe what you want in natural language:

> "Find the authentication bug and fix it."

The agent can then:

1. Explore your project.
2. Read the relevant files.
3. Search for related code.
4. Plan the required changes.
5. Edit the files.
6. Run tests or diagnostics.
7. Check the result.
8. Explain what it changed.

You stay in control of actions that could affect your system or project.

## 🔒 Local & private

Codewords is designed to keep your source code on your computer.

The AI communicates with Ollama through your local machine (`127.0.0.1`). Your project is not sent to a remote AI API during normal local operation.

Internet access is only required for the initial setup and for network-related commands that you explicitly allow.

## ⚙️ Requirements

- Windows 10 / 11
- Internet connection for the first setup
- Approximately 20 GB of free disk space for the default AI model
- 32 GB RAM recommended
- A dedicated GPU is strongly recommended for faster AI responses

Codewords can use other models available in Ollama as well.

## 🚀 Getting started

1. Download the latest `Codewords.exe` from **Releases**.
2. Place it somewhere on your computer.
3. Launch Codewords.
4. Complete the first-time Ollama/model setup.
5. Open your project folder.
6. Make sure the AI status shows `● local`.
7. Ask the agent what you want to accomplish.

For the complete documentation, see the **[Codewords v5.0 User Guide](docs/User%20Guide.pdf)**.

## 🛡️ Safety

Codewords classifies agent commands by risk:

| Level | Examples | Default |
|---|---|---|
| READ | `ls`, `git status`, reading files | Automatic |
| WRITE | `mkdir`, file changes, `git commit` | Configurable |
| NETWORK | `pip install`, `git pull` | Approval required |
| DANGEROUS | `rm -rf`, `DROP TABLE`, `git reset --hard` | Always asks |

File changes can be reviewed through diffs, dangerous commands always require confirmation, and the agent can be stopped at any time.

## 📚 Documentation

The User Guide covers:

- Getting started
- Editor
- Find & Replace
- Terminal
- AI agent
- Agent tools
- Planning and tasks
- Specialists
- Memory and sessions
- Skills
- Safety and permissions
- Settings
- Keyboard shortcuts
- Troubleshooting

## 🧩 Built with

- Python
- Tkinter
- Ollama
- Local AI models
- Windows

## 📄 License

Codewords is released under the MIT License.

## 👨‍💻 Author

**FreddyDeveloper**

- GitHub: https://github.com/FreddyDeveloper
- Website: https://freddydeveloper.com

---

**Codewords v5.0**

*Write it. Ask it. Ship it — all on your own machine.*
