# AgenticHub

**One library for all connectors for LangChain**

AgenticHub is a comprehensive collection of standardized tools and connectors for LangChain-powered AI agents. It provides a unified interface to interact with 90+ external services and APIs, eliminating the need to manage multiple libraries and dependencies.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Available Connectors](#available-connectors)
  - [Cloud Services](#cloud-services)
  - [Databases & Data Management](#databases--data-management)
  - [Communication & Messaging](#communication--messaging)
  - [Productivity & Project Management](#productivity--project-management)
  - [Marketing & Analytics](#marketing--analytics)
  - [E-commerce & Payment](#e-commerce--payment)
  - [Security & Identity](#security--identity)
  - [CI/CD & DevOps](#cicd--devops)
  - [Utilities & File Operations](#utilities--file-operations)
  - [Full Alphabetical List](#full-alphabetical-list)
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
from agentic_tools.tools import GoogleSheetsReadTool, SlackSendMessageTool

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
- **AWS**: DynamoDB, SNS, SQS, Transcribe, Textract
- **Google**: BigQuery, Drive, Sheets, Firebase Realtime Database, Ads, Contacts
- **Microsoft**: Excel, Teams, Dynamics CRM, Graph Security
- **Cisco**: Webex

### Databases & Data Management
- MongoDB
- MySQL
- Elasticsearch
- Snowflake
- Supabase
- CrateDB
- NocoDB
- Baserow
- Kafka
- Spreadsheet File Operations

### Communication & Messaging
- Discord
- Gmail
- Mailchimp
- Plivo
- Webhook
- Rocket.Chat
- Microsoft Teams
- Mandrill
- SMS77
- Pushbullet
- Pushover
- Pushcut
- MQTT
- SIGNL4

### Productivity & Project Management
- Todoist
- Zoom
- Salesforce
- QuickBooks
- Odoo
- ERPNext
- Taiga
- Kitemaker
- Invoice Ninja
- KoboToolbox
- Contentful
- Storyblok
- Strapi
- G Suite Admin

### Marketing & Analytics
- Mailchimp
- GetResponse
- ConvertKit
- Sendy
- Automizy
- PostHog
- Iterable
- Facebook Graph API
- LinkedIn
- Google Ads
- Medium

### E-commerce & Payment
- PayPal
- Paddle
- Wise (formerly TransferWise)
- DHL

### Security & Identity
- Bitwarden
- TOTP (Time-based One-Time Password)
- Security Scorecard
- The Hive Project
- Sentry.io

### CI/CD & DevOps
- CircleCI
- Travis CI
- Splunk
- Zammad

### Utilities & File Operations
- Read PDF
- Write Binary File
- Move Binary Data
- Extract From File
- HTML Processing
- iCal
- Mail Check
- Email Read IMAP
- Rename Keys
- Sort
- Split in Batches
- If (Conditional Logic)
- Execute Workflow
- UpLead
- Interval
- UProc
- Home Assistant
- Open Thesaurus
- Demio
- Oura

### Full Alphabetical List
1. AWS DynamoDB
2. AWS SNS
3. AWS SQS
4. AWS Transcribe
5. AWS Textract
6. Automizy
7. Baserow
8. Bitwarden
9. CircleCI
10. Cisco Webex
11. Contentful
12. ConvertKit
13. CrateDB
14. Demio
15. DHL
16. Discord
17. Drift
18. Elasticsearch
19. Email Read IMAP
20. ERPNext
21. Execute Workflow
22. Extract From File
23. Facebook Graph API
24. Gmail
25. Google Ads
26. Google BigQuery
27. Google Contacts
28. Google Drive
29. Google Firebase Realtime Database
30. Google Sheets
31. GetResponse
32. G Suite Admin
33. Home Assistant
34. HTML Processing
35. iCal
36. If (Conditional Logic)
37. Interval
38. Invoice Ninja
39. Iterable
40. Kafka
41. Kitemaker
42. KoboToolbox
43. LinkedIn
44. Mail Check
45. Mailchimp
46. Mandrill
47. Medium
48. Microsoft Dynamics CRM
49. Microsoft Excel
50. Microsoft Graph Security
51. Microsoft Teams
52. MongoDB
53. Move Binary Data
54. MQTT
55. MySQL
56. NocoDB
57. Odoo
58. Onfleet
59. Open Thesaurus
60. Oura
61. Paddle
62. PayPal
63. Plivo
64. PostHog
65. Pushbullet
66. Pushcut
67. Pushover
68. QuickBooks
69. Read PDF
70. Rename Keys
71. Rocket.Chat
72. Salesforce
73. SCADE Tools
74. Security Scorecard
75. Sendy
76. Sentry.io
77. SIGNL4
78. SMS77
79. Snowflake
80. Sort
81. Split in Batches
82. Splunk
83. Spreadsheet File
84. Storyblok
85. Strapi
86. Supabase
87. Taiga
88. The Hive
89. The Hive Project
90. Todoist
91. TOTP
92. Travis CI
93. UpLead
94. UProc
95. Webhook
96. Wise
97. Write Binary File
98. Zammad
99. Zoom

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
