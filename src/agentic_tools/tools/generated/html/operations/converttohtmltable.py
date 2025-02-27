from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HtmlConverttohtmltableToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    extraction_values: Optional[Dict[str, Any]] = Field(None, description="Extraction Values")
    operation: Optional[str] = Field(None, description="Operation")
    data_property_name: Optional[str] = Field(None, description="Input Binary Field")


class HtmlConverttohtmltableTool(BaseTool):
    name: str = "html_converttohtmltable"
    connector_id: str = "nodes-base.html"
    description: str = "Tool for html convertToHtmlTable operation - convertToHtmlTable operation"
    args_schema: type[BaseModel] | None = HtmlConverttohtmltableToolInput
