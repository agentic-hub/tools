from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class JiraChangelogToolInput(BaseModel):
    commentJson: Optional[str] = Field(None, description="The Atlassian Document Format (ADF). Online builder can be found <a href=\"https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/\">here</a>.")
    commentId: Optional[str] = Field(None, description="The ID of the comment")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    issueKey: Optional[str] = Field(None, description="Issue Key")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryProperty: Optional[str] = Field(None, description="Put Output File in Field")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[str] = Field(None, description="Account ID of the user to delete")
    download: Optional[bool] = Field(None, description="Download")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    comment: Optional[str] = Field(None, description="Comment's text")
    jiraVersion: Optional[str] = Field(None, description="Jira Version")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    attachmentId: Optional[str] = Field(None, description="The ID of the attachment")


class JiraChangelogTool(BaseTool):
    name = "jira_changelog"
    description = "Tool for jira changelog operation - changelog operation"
    
    def _run(self, **kwargs):
        """Run the jira changelog operation."""
        # Implement the tool logic here
        return f"Running jira changelog operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the jira changelog operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
