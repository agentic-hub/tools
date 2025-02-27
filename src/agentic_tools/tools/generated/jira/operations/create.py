from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import JiraCredentials

class JiraCreateToolInput(BaseModel):
    comment_json: Optional[str] = Field(None, description="The Atlassian Document Format (ADF). Online builder can be found <a href=\"https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/\">here</a>.")
    summary: Optional[str] = Field(None, description="Summary")
    comment_id: Optional[str] = Field(None, description="The ID of the comment")
    display_name: Optional[str] = Field(None, description="Display Name")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    issue_key: Optional[str] = Field(None, description="Issue Key")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property: Optional[str] = Field(None, description="Put Output File in Field")
    issue_type: Optional[str] = Field(None, description="ID")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Account ID of the user to delete")
    download: Optional[bool] = Field(None, description="Download")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project: Optional[str] = Field(None, description="ID")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    comment: Optional[str] = Field(None, description="Comment's text")
    username: Optional[str] = Field(None, description="Username")
    jira_version: Optional[str] = Field(None, description="Jira Version")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email_address: Optional[str] = Field(None, description="Email Address")
    attachment_id: Optional[str] = Field(None, description="The ID of the attachment")


class JiraCreateTool(BaseTool):
    name: str = "jira_create"
    description: str = "Tool for jira create operation - create operation"
    args_schema: type[BaseModel] | None = JiraCreateToolInput
    credentials: Optional[JiraCredentials] = None
