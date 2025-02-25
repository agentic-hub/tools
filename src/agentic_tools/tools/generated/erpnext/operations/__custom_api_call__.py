from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Erpnext__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    docType: Optional[str] = Field(None, description="DocType whose documents to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    documentName: Optional[str] = Field(None, description="The name (ID) of document you would like to get")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class Erpnext__custom_api_call__Tool(BaseTool):
    name = "erpnext___custom_api_call__"
    description = "Tool for erpNext __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def _run(self, **kwargs):
        """Run the erpNext __CUSTOM_API_CALL__ operation."""
        # Implement the tool logic here
        return f"Running erpNext __CUSTOM_API_CALL__ operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the erpNext __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
