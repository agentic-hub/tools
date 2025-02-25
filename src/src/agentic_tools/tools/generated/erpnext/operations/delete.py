from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ErpnextDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    docType: Optional[str] = Field(None, description="The type of document you would like to delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    documentName: Optional[str] = Field(None, description="The name (ID) of document you would like to get")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class ErpnextDeleteTool(BaseTool):
    name = "erpnext_delete"
    description = "Tool for erpNext delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the erpNext delete operation."""
        # Implement the tool logic here
        return f"Running erpNext delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the erpNext delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
