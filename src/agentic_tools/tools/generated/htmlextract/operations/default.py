from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HtmlextractDefaultToolInput(BaseModel):
    source_data: Optional[str] = Field(None, description="If HTML should be read from binary or JSON data")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    extraction_values: Optional[Dict[str, Any]] = Field(None, description="Extraction Values")
    data_property_name: Optional[str] = Field(None, description="Input Binary Field")


class HtmlextractDefaultTool(BaseTool):
    name: str = "htmlextract_default"
    connector_id: str = "nodes-base.htmlExtract"
    description: str = "Tool for htmlExtract default operation - default operation"
    args_schema: type[BaseModel] | None = HtmlextractDefaultToolInput
