from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CircleciCredentials

class CircleciTriggerToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    project_slug: Optional[str] = Field(None, description="Project slug in the form org-name/repo-name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    vcs: Optional[str] = Field(None, description="Source control system")
    operation: Optional[str] = Field(None, description="Operation")


class CircleciTriggerTool(BaseTool):
    name: str = "circleci_trigger"
    description: str = "Tool for circleCi trigger operation - trigger operation"
    args_schema: type[BaseModel] | None = CircleciTriggerToolInput
    credentials: Optional[CircleciCredentials] = None
