from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglesheetsAppendToolInput(BaseModel):
    autoMapNotice: Optional[str] = Field(None, description="In this mode, make sure the incoming data is named the same as the columns in your Sheet. (Use an 'Edit Fields' node before this node to change it if required.)")
    startIndex: Optional[float] = Field(None, description="The row number to delete from, The first row is 1")
    documentId: Optional[Dict[str, Any]] = Field(None, description="Document")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    numberToDelete: Optional[float] = Field(None, description="Number of Rows to Delete")
    columns: Optional[str] = Field(None, description="columns")
    fieldsUi: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    dataMode: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    sheetName: Optional[str] = Field(None, description="By URL")
    resource: Optional[str] = Field(None, description="Resource")
    columnToMatchOn: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    valueToMatchOn: Optional[str] = Field(None, description="Value of Column to Match On")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="The name of the sheet")


class GooglesheetsAppendTool(BaseTool):
    name = "googlesheets_append"
    description = "Tool for googleSheets append operation - append operation"
    
    def _run(self, **kwargs):
        """Run the googleSheets append operation."""
        # Implement the tool logic here
        return f"Running googleSheets append operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleSheets append operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
