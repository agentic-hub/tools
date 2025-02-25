from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitlabCreateToolInput(BaseModel):
    filePath: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path or leave it empty for root folder.")
    commitMessage: Optional[str] = Field(None, description="Commit Message")
    tag_name: Optional[str] = Field(None, description="The Git tag the release is associated with")
    assignee_ids: Optional[List[Any]] = Field(None, description="Assignees")
    binaryPropertyName: Optional[str] = Field(None, description="Input Binary Field")
    due_date: Optional[str] = Field(None, description="Due Date for issue")
    fileContent: Optional[str] = Field(None, description="The text content of the file")
    issueNumber: Optional[float] = Field(None, description="The number of the issue on which to create the comment on")
    operation: Optional[str] = Field(None, description="Operation")
    binaryData: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    repository: Optional[str] = Field(None, description="The name of the project")
    body: Optional[str] = Field(None, description="The body of the issue")
    branch: Optional[str] = Field(None, description="Name of the new branch to create. The commit is added to this branch.")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    projectId: Optional[str] = Field(None, description="The ID or URL-encoded path of the project")
    authentication: Optional[str] = Field(None, description="Authentication")
    additionalParameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    title: Optional[str] = Field(None, description="The title of the issue")
    owner: Optional[str] = Field(None, description="User, group or namespace of the project")
    releaseTag: Optional[str] = Field(None, description="The tag of the release")
    labels: Optional[List[Any]] = Field(None, description="Labels")


class GitlabCreateTool(BaseTool):
    name = "gitlab_create"
    description = "Tool for gitlab create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the gitlab create operation."""
        # Implement the tool logic here
        return f"Running gitlab create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gitlab create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
