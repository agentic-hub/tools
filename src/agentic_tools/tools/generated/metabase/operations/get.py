from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MetabaseCredentials

class MetabaseGetToolInput(BaseModel):
    question_id: Optional[str] = Field(None, description="Question ID")
    metric_id: Optional[str] = Field(None, description="Metric ID")
    alert_id: Optional[str] = Field(None, description="Alert ID")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MetabaseGetTool(BaseTool):
    name: str = "metabase_get"
    connector_id: str = "nodes-base.metabase"
    description: str = "Tool for metabase get operation - get operation"
    args_schema: type[BaseModel] | None = MetabaseGetToolInput
    credentials: Optional[MetabaseCredentials] = None
