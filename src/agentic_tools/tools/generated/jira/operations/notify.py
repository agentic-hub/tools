from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import JiraCredentials

class JiraNotifyToolInput(BaseModel):
    comment_json: Optional[str] = Field(None, description="The Atlassian Document Format (ADF). Online builder can be found <a href=\"https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/\">here</a>.")
    notification_recipients_restrictions_ui: Optional[Dict[str, Any]] = Field(None, description="Restricts the notifications to users with the specified permissions")
    notification_recipients_json: Optional[str] = Field(None, description="The recipients of the email notification for the issue")
    comment_id: Optional[str] = Field(None, description="The ID of the comment")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    issue_key: Optional[str] = Field(None, description="Issue Key")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property: Optional[str] = Field(None, description="Put Output File in Field")
    notification_recipients_ui: Optional[Dict[str, Any]] = Field(None, description="The recipients of the email notification for the issue")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Account ID of the user to delete")
    download: Optional[bool] = Field(None, description="Download")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    comment: Optional[str] = Field(None, description="Comment's text")
    jira_version: Optional[str] = Field(None, description="Jira Version")
    notification_recipients_restrictions_json: Optional[str] = Field(None, description="Restricts the notifications to users with the specified permissions")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    attachment_id: Optional[str] = Field(None, description="The ID of the attachment")


class JiraNotifyTool(BaseTool):
    name: str = "jira_notify"
    description: str = "Tool for jira notify operation - notify operation"
    args_schema: type[BaseModel] | None = JiraNotifyToolInput
    credentials: Optional[JiraCredentials] = None
