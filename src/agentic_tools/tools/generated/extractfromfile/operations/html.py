from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExtractfromfileHtmlToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ExtractfromfileHtmlTool(BaseTool):
    name: str = "extractfromfile_html"
    connector_id: str = "nodes-base.extractFromFile"
    description: str = "Tool for extractFromFile html operation - html operation"
    args_schema: type[BaseModel] | None = ExtractfromfileHtmlToolInput
