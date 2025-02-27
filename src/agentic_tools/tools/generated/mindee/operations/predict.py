from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MindeeCredentials

class MindeePredictToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    api_version: Optional[str] = Field(None, description="Which Mindee API Version to use")
    raw_data: Optional[bool] = Field(None, description="Whether to return the data exactly in the way it got received from the API")
    operation: Optional[str] = Field(None, description="Operation")


class MindeePredictTool(BaseTool):
    name: str = "mindee_predict"
    description: str = "Tool for mindee predict operation - predict operation"
    args_schema: type[BaseModel] | None = MindeePredictToolInput
    credentials: Optional[MindeeCredentials] = None
