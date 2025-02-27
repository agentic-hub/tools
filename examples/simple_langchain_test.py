#!/usr/bin/env python3
"""
Simple LangChain Test

This example demonstrates that the langchain and langchain-community dependencies are working correctly.
"""

import os
import sys
import logging
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def create_search_agent(verbose: bool = False):
    """
    Create an agent that can search the web.

    Args:
        verbose (bool, optional): Whether to enable verbose output. Defaults to False.

    Returns:
        Agent: LangChain agent with search tools
    """
    # Initialize the search tool
    search_tool = DuckDuckGoSearchRun()
    tools = [search_tool]

    # Initialize the language model
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o",
    )

    # Create a prompt template for the agent
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant that can search the web for information.\n\nTools: {tools}\n\nTool Names: {tool_names}",
            ),
            MessagesPlaceholder(variable_name="chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor


def main():
    """Main function to run the search agent example."""
    try:
        # Load environment variables
        load_dotenv()

        # Create search agent
        agent = create_search_agent(verbose=True)

        # Example: Search for information
        logger.info("Example: Searching for information")
        result = agent.invoke({"input": "What is the capital of France?"})
        logger.info(f"Result: {result['output']}")

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
