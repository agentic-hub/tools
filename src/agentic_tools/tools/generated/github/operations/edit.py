from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GithubCredentials

class GithubEditToolInput(BaseModel):
    file_path: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path.")
    commit_message: Optional[str] = Field(None, description="Commit Message")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    file_content: Optional[str] = Field(None, description="The text content of the file")
    issue_number: Optional[float] = Field(None, description="The number of the issue edit")
    binary_data: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    operation: Optional[str] = Field(None, description="Operation")
    pull_request_number: Optional[float] = Field(None, description="The number of the pull request")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    edit_fields: Optional[Dict[str, Any]] = Field(None, description="Edit Fields")
    repository: Optional[str] = Field(None, description="Link")
    body: Optional[str] = Field(None, description="The body of the issue")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    additional_parameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    owner: Optional[str] = Field(None, description="Link")


class GithubEditTool(BaseTool):
    name: str = "github_edit"
    description: str = "Tool for github edit operation - edit operation"
    args_schema: type[BaseModel] | None = GithubEditToolInput
    credentials: Optional[GithubCredentials] = None
