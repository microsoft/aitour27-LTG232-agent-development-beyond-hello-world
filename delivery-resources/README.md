# Delivery resources

Presenter, re-delivery, and train-the-trainer materials for this session.

## Core materials

| Item | Link | Notes |
|---|---|---|
| Delivery deck | coming soon | Public URL required before publication |
| Attendee landing page | [Session README](../README.md) | Public starting point |

## Delivery checklist

- Review the session README
- Review the attendee instructions
- Open the deck
- Review the presenter guidance below
- Review live demo reproducibility guidance
- Validate any required environment or setup

## Session preparation

- Review the attendee entry point from the root README.
- Review the delivery deck.
- Validate the required environment and setup.

## Run of show

1. Explain when an agent needs to become an application and why teams need
	custom logic, source control, automated setup, hosted deployment, and
	application integration.
2. Start GitHub Copilot CLI by running `copilot` in the Visual Studio Code
	terminal, then enable autopilot.
3. Use Microsoft Foundry Skill and Foundry Toolkit to generate a hosted social
	media campaign assistant for Caldova.
4. Inspect the generated agent code, toolbox, deployment definition, and
	Foundry resources.
5. Run and invoke the agent locally with the Azure Developer CLI (`azd`).
6. Open Agent Inspector from the command palette, and test a pharmaceutical product campaign request.
7. Deploy the agent to the Cloud. 

## Demo reproducibility

The demo creates a coded social media campaign assistant for Caldova, a
fictional pharmaceutical company. The assistant helps a communications and
social media team draft campaign posts that promote Caldova
pharmaceutical products. File Search grounds product claims in the supplied
synthetic `pharmaceutical_products.json` data, while Web Search supplies timely
seasonal, awareness, customer, and current-topic context. 

### Pre-requisites

- GitHub Copilot CLI
- Visual Studio Code with Foundry Toolkit extension installed
- Azure Developer CLI (`azd`) installed
- Python 3.11 installed

### Generate the hosted agent

In the Visual Studio Code terminal, run `copilot` to start GitHub Copilot CLI
and enable autopilot. Use a prompt based on the following:

>Create a deployable Microsoft Foundry hosted agent solution for Caldova’s >communication team. The agent will act as a social media campaign assistant that >drafts posts promoting Caldova’s pharmaceutical products. Use a `gpt-5.4-mini` >model instance. 
>Configure the agent to use a Microsoft Foundry toolbox containing:
>   - File Search to retrieve accurate product information from the supplied >pharmaceutical product catalog. Use ‘pharmaceutical_products.json’ as product >catalog.
>   - Web Search to retrieve timely context such as the current season, relevant >awareness days, customer needs, and current topics that could inform the campaign.
>When you provision the resources, name the Foundry project caldova-ltg232-sample. >If a project with that name already exists, use it without provisioning a new >one. 
>When implementation is complete, open the generated project folder in Visual >Studio Code.
>
>Reuse the `caldova-ltg232-sample` Foundry project if it already exists. During
>the generated-code walkthrough, show how:
>
>- `main.py` contains the core agent logic built with Microsoft Agent Framework
>	and the OpenAI Responses protocol.
>- `toolbox.yaml` defines Web Search and File Search over
>	`pharmaceutical_products.json` behind an MCP endpoint.
>- `azure.yaml` and the generated infrastructure and Bicep files drive hosted
>	deployment.
>- Foundry Toolkit connects the local project to the Foundry resources and model
>	`gpt-5.4-mini`.

GitHub Copilot takes a few minutes to generate the code. So we recommend 
you showcase live the process of generating the code and then walk through the generated code included in the /src folder of this repository. Towards the end, you can check the status of the agent creation process and show the results if complete.

### Test locally with azd

Open a terminal in Visual Studio Code and run the following command to start the agent locally:

```shell
azd ai agent run
```

In another terminal, invoke it with the campaign request:

```shell
azd ai agent invoke --local "We want to run a social media campaign for Caldova next month. Create three post options promoting products that are relevant to customers at that time of year."
```

Verify that the response provides three distinct, campaign post
options. Product details must come only from the supplied synthetic data, while
timely context should come from Web Search. The response should clearly
separate grounded product facts from current seasonal, awareness, customer, or
topic context and avoid unsupported medical claims.

### Debug with Agent Inspector

Ask GitHub Copilot:
Open Agent Inspector from the command palette (Ctrl+Shift+P) using `Foundry: Open Agent Inspector`, and re-submit the sample prompt:

>We want to run a social media campaign for Caldova next month. Create three post options promoting products that are relevant to customers at that time of year

Inspect the tool calling logs to confirm that File Search retrieves product details from
`pharmaceutical_products.json`, Web Search supplies current context, and the
final response remains grounded in those tool results. 

## Support

Content owner or contact: [Carlotta Castelluccio](https://github.com/carlotta94c)
