from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import JiraCredentials

class JiraGetToolInput(BaseModel):
    comment_json: Optional[str] = Field(None, description="The Atlassian Document Format (ADF). Online builder can be found <a href=\"https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/\">here</a>.")
    comment_id: Optional[str] = Field(None, description="The ID of the comment")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    issue_key: Optional[str] = Field(None, description="Issue Key")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property: Optional[str] = Field(None, description="Put Output File in Field")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Account ID of the user to retrieve")
    download: Optional[bool] = Field(None, description="Download")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    comment: Optional[str] = Field(None, description="Comment's text")
    jira_version: Optional[str] = Field(None, description="Jira Version")
    simplify_output: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    attachment_id: Optional[str] = Field(None, description="The ID of the attachment")


class JiraGetTool(BaseTool):
    name: str = "jira_get"
    connector_id: str = "nodes-base.jira"
    description: str = "Tool for jira get operation - get operation"
    args_schema: type[BaseModel] | None = JiraGetToolInput
    credentials: Optional[JiraCredentials] = None
