from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MondaycomChangemultiplecolumnvaluesToolInput(BaseModel):
    columnValues: Optional[str] = Field(None, description="The column fields and values in JSON format. Documentation can be found <a href=\"https://monday.com/developers/v2#mutations-section-columns-change-multiple-column-values\">here</a>.")
    itemId: Optional[str] = Field(None, description="Item's ID")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="The update text to add")
    columnId: Optional[str] = Field(None, description="The column's unique identifier. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The board's name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    boardId: Optional[str] = Field(None, description="The unique identifier of the board. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    groupId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class MondaycomChangemultiplecolumnvaluesTool(BaseTool):
    name = "mondaycom_changemultiplecolumnvalues"
    description = "Tool for mondayCom changeMultipleColumnValues operation - changeMultipleColumnValues operation"
    
    def _run(self, **kwargs):
        """Run the mondayCom changeMultipleColumnValues operation."""
        # Implement the tool logic here
        return f"Running mondayCom changeMultipleColumnValues operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mondayCom changeMultipleColumnValues operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
