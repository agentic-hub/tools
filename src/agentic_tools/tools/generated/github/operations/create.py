from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GithubCreateToolInput(BaseModel):
    filePath: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path.")
    commitMessage: Optional[str] = Field(None, description="Commit Message")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryPropertyName: Optional[str] = Field(None, description="Input Binary Field")
    event: Optional[str] = Field(None, description="The review action you want to perform")
    fileContent: Optional[str] = Field(None, description="The text content of the file")
    issueNumber: Optional[float] = Field(None, description="The number of the issue on which to create the comment on")
    binaryData: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    operation: Optional[str] = Field(None, description="Operation")
    pullRequestNumber: Optional[float] = Field(None, description="The number of the pull request to review")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    repository: Optional[str] = Field(None, description="Link")
    body: Optional[str] = Field(None, description="The body of the issue")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    additionalParameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    title: Optional[str] = Field(None, description="The title of the issue")
    owner: Optional[str] = Field(None, description="Link")
    releaseTag: Optional[str] = Field(None, description="The tag of the release")
    labels: Optional[List[Any]] = Field(None, description="Labels")
    assignees: Optional[List[Any]] = Field(None, description="Assignees")


class GithubCreateTool(BaseTool):
    name = "github_create"
    description = "Tool for github create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the github create operation."""
        # Implement the tool logic here
        return f"Running github create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the github create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
