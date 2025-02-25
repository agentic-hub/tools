from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglesheetsDeletespreadsheetToolInput(BaseModel):
    startIndex: Optional[float] = Field(None, description="The row number to delete from, The first row is 1")
    documentId: Optional[Dict[str, Any]] = Field(None, description="Document")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    numberToDelete: Optional[float] = Field(None, description="Number of Rows to Delete")
    columns: Optional[str] = Field(None, description="columns")
    fieldsUi: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    dataMode: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    resource: Optional[str] = Field(None, description="Resource")
    columnToMatchOn: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    valueToMatchOn: Optional[str] = Field(None, description="Value of Column to Match On")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="The name of the sheet")


class GooglesheetsDeletespreadsheetTool(BaseTool):
    name = "googlesheets_deletespreadsheet"
    description = "Tool for googleSheets deleteSpreadsheet operation - deleteSpreadsheet operation"
    
    def _run(self, **kwargs):
        """Run the googleSheets deleteSpreadsheet operation."""
        # Implement the tool logic here
        return f"Running googleSheets deleteSpreadsheet operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleSheets deleteSpreadsheet operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
