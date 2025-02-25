from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class XmlDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    xmlNotice: Optional[str] = Field(None, description="If your XML is inside a binary file, use the 'Extract From File' node to convert it to text first")
    mode: Optional[str] = Field(None, description="From and to what format the data should be converted")
    dataPropertyName: Optional[str] = Field(None, description="Name of the property to which to contains the converted XML data")


class XmlDefaultTool(BaseTool):
    name = "xml_default"
    description = "Tool for xml default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the xml default operation."""
        # Implement the tool logic here
        return f"Running xml default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the xml default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
