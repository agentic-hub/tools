from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ErpnextCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    docType: Optional[str] = Field(None, description="DocType you would like to create. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    documentName: Optional[str] = Field(None, description="The name (ID) of document you would like to get")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class ErpnextCreateTool(BaseTool):
    name = "erpnext_create"
    description = "Tool for erpNext create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the erpNext create operation."""
        # Implement the tool logic here
        return f"Running erpNext create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the erpNext create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
