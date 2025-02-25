from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ElasticsecurityCreateToolInput(BaseModel):
    issueTypes: Optional[str] = Field(None, description="Comma-separated list of numerical types of the IBM Resilient issue to create for this case")
    category: Optional[str] = Field(None, description="Category of the ServiceNow ITSM issue to create for this case")
    severityCode: Optional[float] = Field(None, description="Severity code of the IBM Resilient issue to create for this case")
    commentId: Optional[str] = Field(None, description="ID of the case comment to retrieve")
    urgency: Optional[str] = Field(None, description="Urgency of the ServiceNow ITSM issue to create for this case")
    tag: Optional[str] = Field(None, description="Tag to attach to the case. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    impact: Optional[str] = Field(None, description="Impact of the ServiceNow ITSM issue to create for this case")
    caseId: Optional[str] = Field(None, description="Case ID")
    email: Optional[str] = Field(None, description="Jira-registered email")
    connectorType: Optional[str] = Field(None, description="Connector Type")
    apiUrl: Optional[str] = Field(None, description="URL of the third-party instance")
    issueType: Optional[str] = Field(None, description="Type of the Jira issue to create for this case")
    password: Optional[str] = Field(None, description="ServiceNow ITSM password")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Connectors allow you to send Elastic Security cases into other systems (only ServiceNow, Jira, or IBM Resilient)")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    apiKeySecret: Optional[str] = Field(None, description="IBM Resilient API key secret")
    orgId: Optional[str] = Field(None, description="IBM Resilient organization ID")
    comment: Optional[str] = Field(None, description="Comment")
    username: Optional[str] = Field(None, description="ServiceNow ITSM username")
    apiToken: Optional[str] = Field(None, description="Jira API token")
    severity: Optional[str] = Field(None, description="Severity of the ServiceNow ITSM issue to create for this case")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    priority: Optional[str] = Field(None, description="Priority of the Jira issue to create for this case")
    title: Optional[str] = Field(None, description="Title")
    projectKey: Optional[str] = Field(None, description="Jira Project Key")
    apiKeyId: Optional[str] = Field(None, description="IBM Resilient API key ID")
    connectorId: Optional[str] = Field(None, description="Connectors allow you to send Elastic Security cases into other systems (only ServiceNow, Jira, or IBM Resilient). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class ElasticsecurityCreateTool(BaseTool):
    name = "elasticsecurity_create"
    description = "Tool for elasticSecurity create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the elasticSecurity create operation."""
        # Implement the tool logic here
        return f"Running elasticSecurity create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the elasticSecurity create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
