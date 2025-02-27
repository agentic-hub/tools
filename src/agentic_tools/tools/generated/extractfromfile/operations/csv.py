from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExtractfromfileCsvToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ExtractfromfileCsvTool(BaseTool):
    name: str = "extractfromfile_csv"
    connector_id: str = "nodes-base.extractFromFile"
    description: str = "Tool for extractFromFile csv operation - csv operation"
    args_schema: type[BaseModel] | None = ExtractfromfileCsvToolInput
