from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Mondaycom__custom_api_call__ToolInput(BaseModel):
    itemId: Optional[str] = Field(None, description="The unique identifier of the item to add update to")
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


class Mondaycom__custom_api_call__Tool(BaseTool):
    name = "mondaycom___custom_api_call__"
    description = "Tool for mondayCom __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def _run(self, **kwargs):
        """Run the mondayCom __CUSTOM_API_CALL__ operation."""
        # Implement the tool logic here
        return f"Running mondayCom __CUSTOM_API_CALL__ operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mondayCom __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
