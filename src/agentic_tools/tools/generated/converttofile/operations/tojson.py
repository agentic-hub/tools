from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConverttofileTojsonToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    mode: Optional[str] = Field(None, description="Mode")
    operation: Optional[str] = Field(None, description="Operation")


class ConverttofileTojsonTool(BaseTool):
    name: str = "converttofile_tojson"
    description: str = "Tool for convertToFile toJson operation - toJson operation"
    args_schema: type[BaseModel] | None = ConverttofileTojsonToolInput
