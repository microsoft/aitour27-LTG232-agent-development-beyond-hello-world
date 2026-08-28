# Caldova hosted agent presenter guide

This guide walks a presenter through generating, debugging, deploying, and showcasing the Caldova social media campaign assistant. Caldova is a fictional pharmaceutical company. Its assistant should support the communications and social media team by drafting posts that promote their products from a supplied catalog.

The assistant uses File Search to ground product details in [pharmaceutical_products.json](agent-framework-agent-with-foundry-toolbox-responses/pharmaceutical_products.json) and Web Search to add timely context such as seasons, awareness days, customer needs, and current topics. Product names, categories, prices, and other catalog facts must come from File Search. Never invent product facts or add unsupported medical or efficacy claims.

## 1. Understand the solution

This sample uses:

- GitHub Copilot CLI to generate and refine the project through an interactive agent workflow.
- The Microsoft Foundry Skill to give Copilot Foundry-specific workflow knowledge. It comes through the Foundry Toolkit integration; do not install a separate skill package.
- Foundry Toolkit for Visual Studio Code to browse resources, authenticate, debug with Agent Inspector, and inspect the deployed agent.
- Microsoft Agent Framework to define the Caldova assistant in Python.
- The OpenAI Responses protocol for local and hosted agent requests.
- Azure Developer CLI (`azd`) to manage the Foundry project, local agent host, toolbox, deployment, invocation, and monitoring.
- A `gpt-5.4-mini` model deployment.
- A Foundry project named `caldova-ltg232-sample`. 

> **NOTE** The Azure Developer CLI project root is this directory, `/src`. Run `azd` commands from `/src` unless a step explicitly changes into the service folder. The checked-in [azure.yaml](azure.yaml) points to `/src/agent-framework-agent-with-foundry-toolbox-responses` as the service folder.

## 2. Review the checked-in files

- [azure.yaml](azure.yaml) is the `azd` project definition. It declares the Microsoft Foundry project, `gpt-5.4-mini` model deployment, hosted agent service, Responses protocol, remote build, Python 3.13 runtime, resource settings, and service environment variables.
- [main.py](agent-framework-agent-with-foundry-toolbox-responses/main.py) creates the Microsoft Agent Framework agent, authenticates with `DefaultAzureCredential`, connects to the Foundry model and toolbox, applies the Caldova campaign instructions, and serves the agent through `ResponsesHostServer`.
- [toolbox.yaml](agent-framework-agent-with-foundry-toolbox-responses/toolbox.yaml) defines File Search and Web Search behind one Foundry toolbox MCP endpoint. Its checked-in vector store ID is project-specific and must be verified before use.
- [requirements.txt](agent-framework-agent-with-foundry-toolbox-responses/requirements.txt) contains the Python packages required by the agent, hosting layer, OpenAI client, and local debugger.
- [pharmaceutical_products.json](agent-framework-agent-with-foundry-toolbox-responses/pharmaceutical_products.json) is the source catalog that must populate the File Search vector store.
- The Dockerfile is an alternate packaging artifact. It is not required by the normal direct-code remote-build path declared in `azure.yaml`.

## 3. Install the prerequisites

Before the session, confirm all of the following:

- An Azure subscription and permissions to create or use Microsoft Foundry resources, deploy a model and hosted agent.
- Access to `gpt-5.4-mini` in a supported Azure region with sufficient quota. Availability, model version, SKU, and capacity can differ by subscription and region.
- A GitHub account with an active GitHub Copilot entitlement.
- Visual Studio Code and PowerShell 6 or later on Windows.
- Git and Python. The hosted runtime is Python 3.13, so a compatible local Python 3.13 installation is recommended.

### Install Foundry Toolkit

In Visual Studio Code, press `Ctrl+Shift+X`, search for **Foundry Toolkit**, select the extension from Microsoft, and install it. Reload Visual Studio Code if prompted.

Alternatively, install it from the UI, by navigating to the extension panel and then searching for **Foundry Toolkit**. Select the extension from Microsoft and click on *Install*.

### Install Azure Developer CLI

Install `azd` on Windows and verify the installation:

```powershell
winget install Microsoft.Azd
azd version
```

See [Install Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) for current installation options and requirements.

### Install GitHub Copilot CLI

Install GitHub Copilot CLI on Windows and verify the installation:

```powershell
winget install GitHub.Copilot
copilot --version
```

As an alternative, users with Node.js 22 or later can install it through npm:

```powershell
npm install -g @github/copilot
copilot --version
```

See [Install GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli) for current instructions.

## 4. Authenticate each tool

Use the same Azure tenant and subscription in Foundry Toolkit and Azure Developer CLI. Keep authentication interactive. Never paste tokens or secrets into prompts, source files, recordings, or chat, and never commit `.env` files or `azd` environment values.

### Authenticate Foundry Toolkit in Visual Studio Code

1. Open Foundry Toolkit from the Activity Bar.
2. In the **My resources** view, select **Set Foundry Project**. 
3. If `caldova-ltg232-sample` already exists in your subscription, choose **Switch Project** and then select that project. Otherwise, the generation and provisioning workflow creates it later.

### Authenticate Azure Developer CLI

From `/src`, sign in interactively:

```powershell
azd auth login
azd auth login --check-status
```

When the account spans multiple tenants, specify the intended tenant without exposing it in a public recording:

```powershell
azd auth login --tenant-id <tenant-id>
azd auth login --check-status
```

Confirm that this is the same tenant used by Foundry Toolkit. Set the subscription on the `azd` environment later rather than hardcoding or inventing an ID.

### Authenticate GitHub Copilot CLI

Start the interactive CLI:

```powershell
copilot
```

On first launch, Copilot prompts for `/login` when authentication is required. Follow the browser or device instructions. Then enable autopilot using `/autopilot`. Check `copilot --help` and the in-product help because the exact control and interface may evolve.

## 5. Generate the project with Copilot CLI

The repository already contains the generated output. Presenters are recommended to showcase live the creation process of the project and then walk through the existing code in the source folder, for the sake of time and reliability. The following steps show how to generate the project from scratch.

1. Open the repository root in Visual Studio Code.
2. Open a PowerShell terminal.
3. Change to the `azd` project root and launch Copilot CLI:

```powershell
Set-Location .\src
copilot
```

4. Enable autopilot through the Copilot CLI using the `/autopilot` command.
5. Submit this prompt:

>Create a deployable Microsoft Foundry hosted agent solution for Caldova’s communication team. The agent will act as a social media campaign assistant that drafts posts promoting Caldova’s pharmaceutical products. Use a `gpt-5.4-mini` model instance. 
>Configure the agent to use a Microsoft Foundry toolbox containing:
>   - File Search to retrieve accurate product information from the supplied pharmaceutical product catalog. Use ‘pharmaceutical_products.json’ as product catalog.
>  - Web Search to retrieve timely context such as the current season, relevant awareness days, customer needs, and current topics that could inform the campaign.
>When you provision the resources, name the Foundry project caldova-ltg232-sample. If a project with that name already exists, use it without provisioning a new one. 
>When implementation is complete, open the generated project folder in Visual Studio Code.


Copilot uses the Microsoft Foundry Skill supplied through the Foundry Toolkit integration to apply Foundry-specific generation and deployment workflows. No manual skill package installation is required. If available, GPT-5.6-sol is recommended for running the prompt above. 

## 6. Inspect and configure the generated project

Running the prompt above should result in:
- The creation of a new workspace, including a coded hosted-agent, similar to what is included in this repo.
- The provisioning of a Foundry project named `caldova-ltg232-sample` with a `gpt-5.4-mini` model deployment, a toolbox with File Search and Web Search, and a hosted agent service.
- The initialization of a new environment in the `azd` project root, with a `.env` file containing the Foundry project and toolbox endpoints, and the model deployment name. Do not commit this file or its values.

## 9. Run and invoke the agent locally

Use two PowerShell terminals in Visual Studio Code. Stop any other process already listening on port 8088 before starting.

### Terminal 1: start the local Responses server

From `/src`:

```powershell
azd ai agent run
```

Wait for the ready message before invoking the agent.

### Terminal 2: invoke the local agent

From `/src`:

```powershell
azd ai agent invoke --local "We want to run a social media campaign for Caldova next month. Create three post options promoting products that are relevant to customers at that time of year."
```

Verify the response against these criteria:

- It contains three distinct post options.
- Every synthetic product fact is grounded through File Search in the supplied catalog (see data/pharmaceutical_products.json).
- Timely seasonal, awareness-day, customer-need, or current-topic context comes from Web Search.
- It avoids invented product details and unsupported medical or efficacy claims.
- The local logs and tool calls show File Search and Web Search activity, arguments, outputs, latency, and any errors.

## 10. Debug with Agent Inspector

Stop the earlier `azd ai agent run` process before starting a debug session so both processes do not compete for port 8088.

Press `F5`, or open **Run and Debug**, and choose the local agent HTTP server configuration. Then open Agent Inspector. Alternatively, press `Ctrl+Shift+P` and search for **Open Agent Inspector**.  You should see a chat interface to interact with your local agent.

> **TIP**: If you don't see the playground within Agent Inspector, you are probably missing some configuration. Open a new chat with Copilot in VS Code and ask the following prompt: "Add the Visual Studio Code debugging configuration needed to run this agent with Agent Inspector. Create `.vscode/tasks.json` and `.vscode/launch.json` at the repository workspace root."

Use a Caldova product campaign prompt such as:

```text
Create three grounded developer-focused posts for a Caldova campaign next month. Use catalog facts and current seasonal context, and avoid unsupported medical claims.
```

In Agent Inspector, examine model and tool spans, File Search and Web Search arguments and outputs, latency, errors, and the evidence grounding each product statement. Confirm that catalog retrieval and timely web context are both visible before presenting the final response.

## 11. Deploy the hosted agent

When  you are done with testing, stop the local agent and click on the **Deploy** button on the top right corner of the screen. this will trigger a deployment process that will push your hosted agent code to your Foundry project.

## 12. Showcase the deployed solution

Once completed, you can see the deployed solution by navigating to Foundry Toolkit UI -> Agents -> Hosted Agents. From there you can also open a playground that will let you interact with the remote agent, to double check behavior consistency with the local one.

## 14. Clean up carefully

`azd down` removes resources managed by the current environment and can be destructive. Verify the selected environment, tenant, subscription, project binding, and resource scope before considering cleanup. Do not run it when reusing a shared Foundry project.

For a disposable environment that you own and have verified, review the current `azd down` help and confirmation behavior before running:

```powershell
azd env list
azd env get-values
azd down
```

Never use cleanup as part of the live showcase unless deletion is the explicit goal and every affected resource has been reviewed.

## 15. Official references

- [Install Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)
- [Install GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli)
- [Azure Developer CLI documentation](https://learn.microsoft.com/azure/developer/azure-developer-cli/)
- [Microsoft Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Microsoft Agent Framework documentation](https://learn.microsoft.com/agent-framework/)
- [Foundry Toolkit for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)
