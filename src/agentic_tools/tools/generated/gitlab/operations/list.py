from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitlabListToolInput(BaseModel):
    filePath: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path or leave it empty for root folder.")
    page: Optional[float] = Field(None, description="Page of results to display")
    tag_name: Optional[str] = Field(None, description="The Git tag the release is associated with")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    issueNumber: Optional[float] = Field(None, description="The number of the issue on which to create the comment on")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    repository: Optional[str] = Field(None, description="The name of the project")
    body: Optional[str] = Field(None, description="The body of the issue")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    projectId: Optional[str] = Field(None, description="The ID or URL-encoded path of the project")
    authentication: Optional[str] = Field(None, description="Authentication")
    additionalParameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    owner: Optional[str] = Field(None, description="User, group or namespace of the project")


class GitlabListTool(BaseTool):
    name = "gitlab_list"
    description = "Tool for gitlab list operation - list operation"
    
    def _run(self, **kwargs):
        """Run the gitlab list operation."""
        # Implement the tool logic here
        return f"Running gitlab list operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gitlab list operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
