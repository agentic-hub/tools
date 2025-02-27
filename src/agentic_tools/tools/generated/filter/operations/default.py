from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FilterDefaultToolInput(BaseModel):
    combine_conditions: Optional[str] = Field(None, description="How to combine the conditions: AND requires all conditions to be true, OR requires at least one condition to be true")
    conditions: Optional[Dict[str, Any]] = Field(None, description="The type of values to compare")


class FilterDefaultTool(BaseTool):
    name: str = "filter_default"
    connector_id: str = "nodes-base.filter"
    description: str = "Tool for filter default operation - default operation"
    args_schema: type[BaseModel] | None = FilterDefaultToolInput
