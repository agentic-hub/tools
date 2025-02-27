from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitlabCredentials

class GitlabEditToolInput(BaseModel):
    file_path: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path or leave it empty for root folder.")
    commit_message: Optional[str] = Field(None, description="Commit Message")
    tag_name: Optional[str] = Field(None, description="The Git tag the release is associated with")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    file_content: Optional[str] = Field(None, description="The text content of the file")
    issue_number: Optional[float] = Field(None, description="The number of the issue edit")
    operation: Optional[str] = Field(None, description="Operation")
    binary_data: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    edit_fields: Optional[Dict[str, Any]] = Field(None, description="Edit Fields")
    repository: Optional[str] = Field(None, description="The name of the project")
    body: Optional[str] = Field(None, description="The body of the issue")
    branch: Optional[str] = Field(None, description="Name of the new branch to create. The commit is added to this branch.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    project_id: Optional[str] = Field(None, description="The ID or URL-encoded path of the project")
    authentication: Optional[str] = Field(None, description="Authentication")
    additional_parameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    owner: Optional[str] = Field(None, description="User, group or namespace of the project")


class GitlabEditTool(BaseTool):
    name: str = "gitlab_edit"
    connector_id: str = "nodes-base.gitlab"
    description: str = "Tool for gitlab edit operation - edit operation"
    args_schema: type[BaseModel] | None = GitlabEditToolInput
    credentials: Optional[GitlabCredentials] = None
