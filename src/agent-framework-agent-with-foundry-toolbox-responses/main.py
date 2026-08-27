# Copyright (c) Microsoft. All rights reserved.

import asyncio
import os

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from agent_framework_foundry_hosting import FoundryToolbox, ResponsesHostServer
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


async def main():
    credential = DefaultAzureCredential()

    # FoundryToolbox resolves the toolbox endpoint from the environment
    # (TOOLBOX_ENDPOINT, or FOUNDRY_PROJECT_ENDPOINT + TOOLBOX_NAME), authenticates
    # every request with the credential, and transparently forwards the platform
    # per-request call-id to the toolbox. The hosting server enters the agent, which
    # connects the toolbox on first use and closes it at shutdown.
    toolbox = FoundryToolbox(credential)

    # Create the chat client
    client = FoundryChatClient(
        project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=credential,
    )

    agent = Agent(
        client=client,
        instructions=(
            "You are Caldova's Social Media Campaign Assistant, working for the "
            "communication team of Caldova, a pharmaceutical company. Your job is to "
            "draft engaging, accurate, and compliant social media posts that promote "
            "Caldova's pharmaceutical products.\n\n"
            "Tools available to you (via the Foundry toolbox):\n"
            "- file_search: Retrieve accurate product information (names, categories, "
            "prices) from Caldova's official pharmaceutical product catalog. ALWAYS use "
            "file_search to ground any product details you mention. Never invent product "
            "names, claims, or prices.\n"
            "- web_search: Retrieve timely context such as the current season, relevant "
            "awareness or health days, seasonal customer needs, and trending topics that "
            "can make a campaign more relevant and engaging.\n\n"
            "Workflow for each request:\n"
            "1. Use file_search to confirm the exact product(s), category, and price from "
            "the catalog.\n"
            "2. Use web_search to find timely hooks (season, awareness days, current "
            "topics, customer needs) relevant to the product.\n"
            "3. Draft social media post(s) that combine the accurate product info with the "
            "timely context. Offer platform-appropriate variations (e.g., Instagram, "
            "LinkedIn, X) with suitable tone, length, hashtags, and a clear call to action "
            "when asked.\n\n"
            "Guidelines:\n"
            "- Keep messaging factual and grounded in the catalog; do not fabricate "
            "medical claims or efficacy statements.\n"
            "- Be mindful that these are pharmaceutical/health-adjacent products; avoid "
            "misleading health promises and keep copy responsible and compliant.\n"
            "- Cite which product(s) a post refers to and note the source context you "
            "used when helpful."
        ),
        tools=toolbox,
        # History will be managed by the hosting infrastructure, thus there
        # is no need to store history by the service. Learn more at:
        # https://developers.openai.com/api/reference/resources/responses/methods/create
        default_options={"store": False},
    )

    server = ResponsesHostServer(agent)
    await server.run_async()


if __name__ == "__main__":
    asyncio.run(main())
