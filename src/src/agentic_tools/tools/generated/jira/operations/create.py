from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class JiraCreateToolInput(BaseModel):
    commentJson: Optional[str] = Field(None, description="The Atlassian Document Format (ADF). Online builder can be found <a href=\"https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/\">here</a>.")
    summary: Optional[str] = Field(None, description="Summary")
    commentId: Optional[str] = Field(None, description="The ID of the comment")
    displayName: Optional[str] = Field(None, description="Display Name")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    issueKey: Optional[str] = Field(None, description="Issue Key")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryProperty: Optional[str] = Field(None, description="Put Output File in Field")
    issueType: Optional[str] = Field(None, description="ID")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[str] = Field(None, description="Account ID of the user to delete")
    download: Optional[bool] = Field(None, description="Download")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project: Optional[str] = Field(None, description="ID")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    comment: Optional[str] = Field(None, description="Comment's text")
    username: Optional[str] = Field(None, description="Username")
    jiraVersion: Optional[str] = Field(None, description="Jira Version")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    emailAddress: Optional[str] = Field(None, description="Email Address")
    attachmentId: Optional[str] = Field(None, description="The ID of the attachment")


class JiraCreateTool(BaseTool):
    name = "jira_create"
    description = "Tool for jira create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the jira create operation."""
        # Implement the tool logic here
        return f"Running jira create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the jira create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
