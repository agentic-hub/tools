from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitlabCredentials

class GitlabGetrepositoriesToolInput(BaseModel):
    file_path: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path or leave it empty for root folder.")
    tag_name: Optional[str] = Field(None, description="The Git tag the release is associated with")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    issue_number: Optional[float] = Field(None, description="The number of the issue on which to create the comment on")
    operation: Optional[str] = Field(None, description="Operation")
    repository: Optional[str] = Field(None, description="The name of the project")
    body: Optional[str] = Field(None, description="The body of the issue")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    project_id: Optional[str] = Field(None, description="The ID or URL-encoded path of the project")
    authentication: Optional[str] = Field(None, description="Authentication")
    additional_parameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    owner: Optional[str] = Field(None, description="User, group or namespace of the project")


class GitlabGetrepositoriesTool(BaseTool):
    name: str = "gitlab_getrepositories"
    connector_id: str = "nodes-base.gitlab"
    description: str = "Tool for gitlab getRepositories operation - getRepositories operation"
    args_schema: type[BaseModel] | None = GitlabGetrepositoriesToolInput
    credentials: Optional[GitlabCredentials] = None
