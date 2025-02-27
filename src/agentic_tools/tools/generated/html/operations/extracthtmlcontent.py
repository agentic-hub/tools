from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HtmlExtracthtmlcontentToolInput(BaseModel):
    source_data: Optional[str] = Field(None, description="If HTML should be read from binary or JSON data")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    extraction_values: Optional[Dict[str, Any]] = Field(None, description="Extraction Values")
    operation: Optional[str] = Field(None, description="Operation")
    data_property_name: Optional[str] = Field(None, description="Input Binary Field")


class HtmlExtracthtmlcontentTool(BaseTool):
    name: str = "html_extracthtmlcontent"
    description: str = "Tool for html extractHtmlContent operation - extractHtmlContent operation"
    args_schema: type[BaseModel] | None = HtmlExtracthtmlcontentToolInput
