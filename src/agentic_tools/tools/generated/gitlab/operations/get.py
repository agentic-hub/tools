from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitlabCredentials

class GitlabGetToolInput(BaseModel):
    file_path: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path or leave it empty for root folder.")
    tag_name: Optional[str] = Field(None, description="The Git tag the release is associated with")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    issue_number: Optional[float] = Field(None, description="The number of the issue get data of")
    operation: Optional[str] = Field(None, description="Operation")
    as_binary_property: Optional[bool] = Field(None, description="Whether to set the data of the file as binary property instead of returning the raw API response")
    repository: Optional[str] = Field(None, description="The name of the project")
    body: Optional[str] = Field(None, description="The body of the issue")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    project_id: Optional[str] = Field(None, description="The ID or URL-encoded path of the project")
    authentication: Optional[str] = Field(None, description="Authentication")
    additional_parameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    owner: Optional[str] = Field(None, description="User, group or namespace of the project")


class GitlabGetTool(BaseTool):
    name: str = "gitlab_get"
    connector_id: str = "nodes-base.gitlab"
    description: str = "Tool for gitlab get operation - get operation"
    args_schema: type[BaseModel] | None = GitlabGetToolInput
    credentials: Optional[GitlabCredentials] = None
