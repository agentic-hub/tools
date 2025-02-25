from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MondaycomChangecolumnvalueToolInput(BaseModel):
    itemId: Optional[str] = Field(None, description="The unique identifier of the item to to change column of")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="The column value in JSON format. Documentation can be found <a href=\"https://monday.com/developers/v2#mutations-section-columns-change-column-value\">here</a>.")
    columnId: Optional[str] = Field(None, description="The column's unique identifier. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The board's name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    boardId: Optional[str] = Field(None, description="The unique identifier of the board. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    groupId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class MondaycomChangecolumnvalueTool(BaseTool):
    name = "mondaycom_changecolumnvalue"
    description = "Tool for mondayCom changeColumnValue operation - changeColumnValue operation"
    
    def _run(self, **kwargs):
        """Run the mondayCom changeColumnValue operation."""
        # Implement the tool logic here
        return f"Running mondayCom changeColumnValue operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mondayCom changeColumnValue operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
