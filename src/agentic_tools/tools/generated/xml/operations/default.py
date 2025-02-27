from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class XmlDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    xml_notice: Optional[str] = Field(None, description="If your XML is inside a binary file, use the 'Extract From File' node to convert it to text first")
    mode: Optional[str] = Field(None, description="From and to what format the data should be converted")
    data_property_name: Optional[str] = Field(None, description="Name of the property to which to contains the converted XML data")


class XmlDefaultTool(BaseTool):
    name: str = "xml_default"
    connector_id: str = "nodes-base.xml"
    description: str = "Tool for xml default operation - default operation"
    args_schema: type[BaseModel] | None = XmlDefaultToolInput
