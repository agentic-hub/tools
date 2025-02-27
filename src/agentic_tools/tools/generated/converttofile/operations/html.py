from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConverttofileHtmlToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ConverttofileHtmlTool(BaseTool):
    name: str = "converttofile_html"
    description: str = "Tool for convertToFile html operation - html operation"
    args_schema: type[BaseModel] | None = ConverttofileHtmlToolInput
