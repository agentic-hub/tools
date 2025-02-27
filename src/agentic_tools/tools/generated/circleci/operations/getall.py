from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CircleciCredentials

class CircleciGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    project_slug: Optional[str] = Field(None, description="Project slug in the form org-name/repo-name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    vcs: Optional[str] = Field(None, description="Source control system")
    operation: Optional[str] = Field(None, description="Operation")


class CircleciGetallTool(BaseTool):
    name: str = "circleci_getall"
    description: str = "Tool for circleCi getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = CircleciGetallToolInput
    credentials: Optional[CircleciCredentials] = None
