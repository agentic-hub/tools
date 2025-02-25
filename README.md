# Agentic Tools Hub

A centralized platform for managing and generating tools for AI agents. This project standardizes connection implementations, reduces development overhead, and simplifies long-term maintenance complexity.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Tool Generation](#tool-generation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Development](#development)
- [Deployment](#deployment)
- [License](#license)

## 🔍 Overview

Agentic Tools Hub provides a unified infrastructure to manage multiple agent connections and tools. This centralization simplifies authentication, enforces consistent security protocols, and streamlines the integration of diverse systems. For developers, this means fewer custom integrations and a robust foundation to build upon.

## ✨ Features

- **Unified Tool Management**: Centralized repository for all agent tools
- **Tool Generation Engine**: Automatically generate tool implementations from configuration files
- **LangChain Integration**: Seamless integration with LangChain's tool ecosystem
- **Standardized Interfaces**: Consistent API design across all tools
- **Extensible Architecture**: Easily add new tool types and capabilities

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- Poetry (for dependency management)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/agentic-hub.git
   cd agentic-hub
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## 🔧 Usage

### Basic Usage

```python
from agentic_tools import get_all_tools

# Get all available tools
tools = get_all_tools()

# Use tools with your agent
agent = Agent(tools=tools)
```

### Integrating with LangChain

```python
from langchain.agents import AgentExecutor, create_react_agent
from langchain.llms import OpenAI
from agentic_tools import get_all_tools

# Get tools from the hub
tools = get_all_tools()

# Create a LangChain agent with the tools
llm = OpenAI(temperature=0)
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# Run the agent
agent_executor.run("Use the tools to accomplish a task")
```

## 🛠️ Tool Generation

The Agentic Tools Hub includes a powerful tool generation engine that can create tool implementations from configuration files.

### Generating Tools

1. Create a configuration file in JSON format in the `src/generator/engine_config` directory
2. Run the generator:

```python
from generator.generator_engine import Generator

generator = Generator("MyToolGenerator")
generator.generate("src/generator/engine_config")
```

### Configuration Format

Tool configurations should follow this basic structure:

```json
{
  "name": "MyTool",
  "description": "A tool that does something useful",
  "operations": [
    {
      "name": "operation_name",
      "description": "What this operation does",
      "parameters": {
        "param1": {
          "type": "string",
          "description": "Description of parameter"
        }
      }
    }
  ]
}
```

## 📁 Project Structure

```
agentic-hub/
├── src/
│   ├── agentic_tools/       # Main package
│   │   ├── tools/           # Tool implementations
│   │   │   ├── base/        # Base tool classes
│   │   │   └── generated/   # Generated tool implementations
│   │   └── toolkit/         # Tool organization and management
│   └── generator/           # Tool generation engine
├── tests/                   # Test suite
├── pyproject.toml           # Project configuration
└── README.md                # This file
```

## 👥 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Submit a pull request

### Contribution Guidelines

- Follow the existing code style and conventions
- Write tests for new features
- Update documentation for any changes
- Keep pull requests focused on a single feature or bug fix

## 🧪 Development

### Setting Up Development Environment

```bash
# Install dependencies
poetry install
```

### Code Style

This project follows PEP 8 style guidelines. You can check your code style with:

```bash
poetry run flake8
```

## 🚀 Deployment

This project uses GitHub Actions for continuous integration and deployment. For detailed information about the deployment process, see [DEPLOYMENT.md](DEPLOYMENT.md).

### Quick Deployment Guide

1. **Automatic Linting**: Linting runs automatically on push to main and pull requests
2. **Version Bumping**: Use the Version Bump workflow in GitHub Actions to increment the version
3. **Deployment to PyPI**: Create a new GitHub Release to trigger deployment to PyPI

### Required Secrets

To enable deployment to PyPI, add the following secret to your GitHub repository:
- `PYPI_TOKEN`: Your PyPI API token with upload permissions

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
