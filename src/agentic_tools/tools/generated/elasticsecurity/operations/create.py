from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ElasticsecurityCredentials

class ElasticsecurityCreateToolInput(BaseModel):
    issue_types: Optional[str] = Field(None, description="Comma-separated list of numerical types of the IBM Resilient issue to create for this case")
    category: Optional[str] = Field(None, description="Category of the ServiceNow ITSM issue to create for this case")
    severity_code: Optional[float] = Field(None, description="Severity code of the IBM Resilient issue to create for this case")
    comment_id: Optional[str] = Field(None, description="ID of the case comment to retrieve")
    urgency: Optional[str] = Field(None, description="Urgency of the ServiceNow ITSM issue to create for this case")
    tag: Optional[str] = Field(None, description="Tag to attach to the case. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    impact: Optional[str] = Field(None, description="Impact of the ServiceNow ITSM issue to create for this case")
    case_id: Optional[str] = Field(None, description="Case ID")
    email: Optional[str] = Field(None, description="Jira-registered email")
    connector_type: Optional[str] = Field(None, description="Connector Type")
    api_url: Optional[str] = Field(None, description="URL of the third-party instance")
    issue_type: Optional[str] = Field(None, description="Type of the Jira issue to create for this case")
    password: Optional[str] = Field(None, description="ServiceNow ITSM password")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Connectors allow you to send Elastic Security cases into other systems (only ServiceNow, Jira, or IBM Resilient)")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    api_key_secret: Optional[str] = Field(None, description="IBM Resilient API key secret")
    org_id: Optional[str] = Field(None, description="IBM Resilient organization ID")
    comment: Optional[str] = Field(None, description="Comment")
    username: Optional[str] = Field(None, description="ServiceNow ITSM username")
    api_token: Optional[str] = Field(None, description="Jira API token")
    severity: Optional[str] = Field(None, description="Severity of the ServiceNow ITSM issue to create for this case")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    priority: Optional[str] = Field(None, description="Priority of the Jira issue to create for this case")
    title: Optional[str] = Field(None, description="Title")
    project_key: Optional[str] = Field(None, description="Jira Project Key")
    api_key_id: Optional[str] = Field(None, description="IBM Resilient API key ID")
    connector_id: Optional[str] = Field(None, description="Connectors allow you to send Elastic Security cases into other systems (only ServiceNow, Jira, or IBM Resilient). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class ElasticsecurityCreateTool(BaseTool):
    name: str = "elasticsecurity_create"
    connector_id: str = "nodes-base.elasticSecurity"
    description: str = "Tool for elasticSecurity create operation - create operation"
    args_schema: type[BaseModel] | None = ElasticsecurityCreateToolInput
    credentials: Optional[ElasticsecurityCredentials] = None
