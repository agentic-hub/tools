from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitlabDeleteToolInput(BaseModel):
    filePath: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path or leave it empty for root folder.")
    commitMessage: Optional[str] = Field(None, description="Commit Message")
    tag_name: Optional[str] = Field(None, description="The Git tag the release is associated with")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    issueNumber: Optional[float] = Field(None, description="The number of the issue on which to create the comment on")
    operation: Optional[str] = Field(None, description="Operation")
    repository: Optional[str] = Field(None, description="The name of the project")
    body: Optional[str] = Field(None, description="The body of the issue")
    branch: Optional[str] = Field(None, description="Name of the new branch to create. The commit is added to this branch.")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    projectId: Optional[str] = Field(None, description="The ID or URL-encoded path of the project")
    authentication: Optional[str] = Field(None, description="Authentication")
    additionalParameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    owner: Optional[str] = Field(None, description="User, group or namespace of the project")


class GitlabDeleteTool(BaseTool):
    name = "gitlab_delete"
    description = "Tool for gitlab delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the gitlab delete operation."""
        # Implement the tool logic here
        return f"Running gitlab delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gitlab delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
