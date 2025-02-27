from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CircleciCredentials

class CircleciGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    pipeline_number: Optional[float] = Field(None, description="The number of the pipeline")
    project_slug: Optional[str] = Field(None, description="Project slug in the form org-name/repo-name")
    vcs: Optional[str] = Field(None, description="Source control system")
    operation: Optional[str] = Field(None, description="Operation")


class CircleciGetTool(BaseTool):
    name: str = "circleci_get"
    connector_id: str = "nodes-base.circleCi"
    description: str = "Tool for circleCi get operation - get operation"
    args_schema: type[BaseModel] | None = CircleciGetToolInput
    credentials: Optional[CircleciCredentials] = None
