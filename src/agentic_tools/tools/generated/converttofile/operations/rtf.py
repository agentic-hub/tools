from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConverttofileRtfToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ConverttofileRtfTool(BaseTool):
    name: str = "converttofile_rtf"
    connector_id: str = "nodes-base.convertToFile"
    description: str = "Tool for convertToFile rtf operation - rtf operation"
    args_schema: type[BaseModel] | None = ConverttofileRtfToolInput
