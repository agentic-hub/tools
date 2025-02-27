from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GithubCredentials

class GithubGetToolInput(BaseModel):
    file_path: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    review_id: Optional[str] = Field(None, description="ID of the review")
    release_id: Optional[str] = Field(None, description="Release ID")
    issue_number: Optional[float] = Field(None, description="The number of the issue get data of")
    operation: Optional[str] = Field(None, description="Operation")
    pull_request_number: Optional[float] = Field(None, description="The number of the pull request")
    as_binary_property: Optional[bool] = Field(None, description="Whether to set the data of the file as binary property instead of returning the raw API response")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    repository: Optional[str] = Field(None, description="Link")
    body: Optional[str] = Field(None, description="The body of the issue")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    additional_parameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    owner: Optional[str] = Field(None, description="Link")


class GithubGetTool(BaseTool):
    name: str = "github_get"
    connector_id: str = "nodes-base.github"
    description: str = "Tool for github get operation - get operation"
    args_schema: type[BaseModel] | None = GithubGetToolInput
    credentials: Optional[GithubCredentials] = None
