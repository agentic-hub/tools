from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GithubDeleteToolInput(BaseModel):
    filePath: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path.")
    commitMessage: Optional[str] = Field(None, description="Commit Message")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryPropertyName: Optional[str] = Field(None, description="Input Binary Field")
    release_id: Optional[str] = Field(None, description="Release ID")
    issueNumber: Optional[float] = Field(None, description="The number of the issue on which to create the comment on")
    operation: Optional[str] = Field(None, description="Operation")
    pullRequestNumber: Optional[float] = Field(None, description="The number of the pull request")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    repository: Optional[str] = Field(None, description="Link")
    body: Optional[str] = Field(None, description="The body of the issue")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    additionalParameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    owner: Optional[str] = Field(None, description="Link")


class GithubDeleteTool(BaseTool):
    name = "github_delete"
    description = "Tool for github delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the github delete operation."""
        # Implement the tool logic here
        return f"Running github delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the github delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
