from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ErpnextGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    docType: Optional[str] = Field(None, description="The type of document you would like to get. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    documentName: Optional[str] = Field(None, description="The name (ID) of document you would like to get")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class ErpnextGetTool(BaseTool):
    name = "erpnext_get"
    description = "Tool for erpNext get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the erpNext get operation."""
        # Implement the tool logic here
        return f"Running erpNext get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the erpNext get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
