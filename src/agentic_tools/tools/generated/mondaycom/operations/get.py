from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MondaycomGetToolInput(BaseModel):
    itemId: Optional[str] = Field(None, description="Item's ID (Multiple can be added separated by comma)")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="The update text to add")
    columnId: Optional[str] = Field(None, description="The column's unique identifier. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The board's name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    boardId: Optional[str] = Field(None, description="Board unique identifiers. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    groupId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class MondaycomGetTool(BaseTool):
    name = "mondaycom_get"
    description = "Tool for mondayCom get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the mondayCom get operation."""
        # Implement the tool logic here
        return f"Running mondayCom get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mondayCom get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
