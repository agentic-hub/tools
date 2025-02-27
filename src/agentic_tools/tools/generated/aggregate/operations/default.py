from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AggregateDefaultToolInput(BaseModel):
    aggregate: Optional[str] = Field(None, description="Aggregate")
    fields_to_aggregate: Optional[Dict[str, Any]] = Field(None, description="Fields To Aggregate")
    include: Optional[str] = Field(None, description="Include")
    destination_field_name: Optional[str] = Field(None, description="The name of the output field to put the data in")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fields_to_include: Optional[str] = Field(None, description="Fields To Include")
    fields_to_exclude: Optional[str] = Field(None, description="Fields To Exclude")


class AggregateDefaultTool(BaseTool):
    name: str = "aggregate_default"
    connector_id: str = "nodes-base.aggregate"
    description: str = "Tool for aggregate default operation - default operation"
    args_schema: type[BaseModel] | None = AggregateDefaultToolInput
