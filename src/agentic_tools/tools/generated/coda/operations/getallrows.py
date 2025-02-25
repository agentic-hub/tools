from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CodaGetallrowsToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    docId: Optional[str] = Field(None, description="ID of the doc. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tableId: Optional[str] = Field(None, description="The table to get the rows from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    columnId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    rowId: Optional[str] = Field(None, description="ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected")
    operation: Optional[str] = Field(None, description="Operation")
    viewId: Optional[str] = Field(None, description="The view to get the row from")


class CodaGetallrowsTool(BaseTool):
    name = "coda_getallrows"
    description = "Tool for coda getAllRows operation - getAllRows operation"
    
    def _run(self, **kwargs):
        """Run the coda getAllRows operation."""
        # Implement the tool logic here
        return f"Running coda getAllRows operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the coda getAllRows operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
