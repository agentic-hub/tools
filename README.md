# AgenticHub

**One library for all connectors for LangChain**

AgenticHub is a comprehensive collection of standardized tools and connectors for LangChain-powered AI agents. It provides a unified interface to interact with 90+ external services and APIs, eliminating the need to manage multiple libraries and dependencies.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Available Connectors](#available-connectors)
- [Contributing](#contributing)
- [Development](#development)
- [License](#license)

## 🔍 Overview

AgenticHub solves the fragmentation problem in the LangChain ecosystem by providing a single, well-maintained library that includes connectors for dozens of popular services and APIs. Instead of hunting down, installing, and managing multiple connector libraries with inconsistent interfaces, you can use AgenticHub as your one-stop solution for all agent tool needs.

## ✨ Features

- **90+ Pre-built Connectors**: Access tools for databases, APIs, cloud services, and more
- **Standardized Interface**: Consistent API design across all connectors
- **LangChain Integration**: Seamless integration with LangChain's agent framework
- **Automatic Tool Generation**: Tools are generated from standardized configurations
- **Production Ready**: Built for reliability and performance in production environments
- **Extensible**: Easily add your own custom connectors

## 🚀 Installation

```bash
pip install agentic-tools
```

## 🔧 Usage

### Basic Usage

```python
from agentic_tools import get_all_tools
from langchain.agents import AgentExecutor, create_react_agent
from langchain.llms import OpenAI

# Get all available tools
tools = get_all_tools()

# Or select specific tools
from agentic_tools.tools.generated import GoogleSheetsReadTool, SlackSendMessageTool

tools = [
    GoogleSheetsReadTool(),
    SlackSendMessageTool()
]

# Create a LangChain agent with the tools
llm = OpenAI(temperature=0)
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# Run the agent
agent_executor.run("Update our Google Sheet with yesterday's sales data")
```

## 📊 Available Connectors

AgenticHub includes connectors for:

### Cloud Services
- AWS (DynamoDB, SNS, SQS, Transcribe, Textract)
- Google (BigQuery, Drive, Sheets, Firebase, Ads)
- Microsoft (Excel, Teams, Dynamics CRM, Graph)

### Databases
- MongoDB
- MySQL
- Elasticsearch
- Snowflake
- Supabase
- CrateDB

### Communication
- Discord
- Slack
- Gmail
- Mailchimp
- Twilio
- Plivo
- Webhook

### Productivity
- Todoist
- Zoom
- Notion
- Salesforce
- QuickBooks
- Odoo
- ERPNext

### And many more...

See the [full list of connectors](#) for details on all available tools.

## 👥 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Submit a pull request

## 🧪 Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/agentic-hub.git
cd agentic-hub

# Install dependencies
pip install poetry
poetry install
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
