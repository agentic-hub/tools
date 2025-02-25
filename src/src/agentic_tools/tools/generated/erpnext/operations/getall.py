from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ErpnextGetallToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    docType: Optional[str] = Field(None, description="DocType whose documents to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    documentName: Optional[str] = Field(None, description="The name (ID) of document you would like to get")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class ErpnextGetallTool(BaseTool):
    name = "erpnext_getall"
    description = "Tool for erpNext getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the erpNext getAll operation."""
        # Implement the tool logic here
        return f"Running erpNext getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the erpNext getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
