## Before you're done

This repo has been created for your AI Tour 2027 session. Here's how to get it ready.

**Easiest path — use the agent (recommended):**

- Open GitHub Copilot Chat and say `help me initialize repo`. The agent will walk you through getting the README populated.
- When you're ready to publish, say `help me finalize repo`. The agent will clean up unused folders, validate everything, and remove this "Before you're done" section and other extra stuff that attendees don't need to see.
- Curious how it works? Read the [agent workflow](.github/AGENT-WORKFLOW.md).

**Doing it manually?**

Fill in the sections below yourself, then:

- Delete any placeholder folders you don't need (`data/`, `infra/`, etc.)
- Delete this "Before you're done" section
- Delete `.github/agents/`, `.github/tests/`, `.github/copilot-instructions.md`, and `.github/AGENT-WORKFLOW.md` — these are template tooling, not part of your published repo

**Folder conventions:**

- Attendee step-by-step guidance goes in `instructions/`. If you use MkDocs or a docs site instead, put it in `docs/` and link to it from this README.
- Reference material and background reading go in `docs/`.
- Presenter notes, deck link, recordings, and re-delivery materials go in `delivery-resources/`. Fill in [`delivery-resources/README.md`](delivery-resources/README.md).
- You can add a `.devcontainer/` folder if needed.

---

<a name="start-building"></a>

<p align="center">
<img src="img/banner-ai-tour-27.png" alt="Microsoft AI Tour 2027" width="100%"/>
</p>

# [Microsoft AI Tour 2027](https://aitour.microsoft.com)

## 🔥 LTG232: Agent development beyond Hello World

### Session description

Building AI agents often involves far more than writing code: configuring tools,
debugging behavior, testing integrations, and deploying to production. In this
talk, we'll explore how GitHub Copilot, Microsoft Foundry Skill, and Foundry
Toolkit enable an end-to-end agent development workflow entirely within Visual
Studio Code.

### 🚀 Getting started

#### In a guided session

If you're following along during a live session:

1. Review the Caldova pharmaceutical business scenario
2. Explore the agent implementation in [`src/`](src/README.md)
3. Review the supporting sample inputs in [`data/`](data/README.md)

#### On your own

If you're learning at your own pace:

1. Clone this repository
2. Review the sample agent implementation in [`src/`](src/README.md)
3. Use the supporting inputs in [`data/`](data/README.md) to explore the scenario

### 🎯 Learning outcomes

By the end of this session, you will be able to:

- Explain how GitHub Copilot, Microsoft Foundry Skill, and Foundry Toolkit support the AI agent development lifecycle in Visual Studio Code
- Use GitHub Copilot and Microsoft Foundry Skill to configure and debug an AI agent in Visual Studio Code
- Test agent integrations and prepare an AI agent for production deployment from Visual Studio Code

### 💻 Technologies used

- GitHub Copilot
- Microsoft Foundry Skill
- Foundry Toolkit
- Visual Studio Code

### 📚 Continue your learning

Pick your next step based on your learning style:

| Resource | What you'll get |
|----------|-----------------|
| **[Microsoft Learn](https://learn.microsoft.com)** | Official documentation and guided learning paths on these topics |
| **[AI Tour 2027 Resource Center](https://aka.ms/aitour27-resource-center)** | Additional session repos and materials from AI Tour 2027 |
| **[Microsoft Foundry Community](https://aka.ms/MicrosoftFoundryDiscord-AITour27)** | Connect with other learners and experts in our Discord community |

### 🌟 Microsoft Learn MCP Server

<!-- Remove this section if the Microsoft Learn MCP Server is not relevant to the session. -->

The Microsoft Learn MCP Server gives your AI agent direct access to Microsoft's official documentation — grounded, up-to-date answers about the topics in this session.

**GitHub Copilot CLI** — Install with:

```shell
copilot plugin install microsoftdocs/mcp
```

**VS Code** — One-click install:  
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Learn_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft-learn&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D)

For more information, visit the [Learn MCP Server repo](https://aka.ms/learnmcp).

### 👥 Content owners

<table>
<tr>
    <td align="center"><a href="https://github.com/carlotta94c">
        <img src="https://github.com/carlotta94c.png" width="100px;" alt="Carlotta Castelluccio"/><br />
        <sub><b>Carlotta Castelluccio</b></sub></a><br />
            <a href="https://github.com/carlotta94c" title="talk">📢</a>
    </td>
</tr></table>

### Deliver this session

Presenters and re-delivery partners can find the deck, recordings, presenter
notes, and delivery guidance in [`delivery-resources/`](delivery-resources/README.md).

### ⚖️ Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.

Any use of third-party trademarks or logos are subject to those third-party's policies.
