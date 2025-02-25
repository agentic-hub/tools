from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglesheetsClearToolInput(BaseModel):
    keepFirstRow: Optional[bool] = Field(None, description="Keep First Row")
    startIndex: Optional[float] = Field(None, description="The row number to delete from, The first row is 1")
    documentId: Optional[Dict[str, Any]] = Field(None, description="Document")
    operation: Optional[str] = Field(None, description="Operation")
    range: Optional[str] = Field(None, description="The table range to read from or to append data to. See the Google <a href=\"https://developers.google.com/sheets/api/guides/values#writing\">documentation</a> for the details. If it contains multiple sheets it can also be added like this: \"MySheet!A:F\"")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    numberToDelete: Optional[float] = Field(None, description="Number of Rows to Delete")
    columns: Optional[str] = Field(None, description="columns")
    fieldsUi: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    dataMode: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    rowsToDelete: Optional[float] = Field(None, description="Number of Rows to Delete")
    sheetName: Optional[str] = Field(None, description="By URL")
    resource: Optional[str] = Field(None, description="Resource")
    columnsToDelete: Optional[float] = Field(None, description="Number of Columns to Delete")
    columnToMatchOn: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    valueToMatchOn: Optional[str] = Field(None, description="Value of Column to Match On")
    authentication: Optional[str] = Field(None, description="Authentication")
    clear: Optional[str] = Field(None, description="What to clear")
    title: Optional[str] = Field(None, description="The name of the sheet")


class GooglesheetsClearTool(BaseTool):
    name = "googlesheets_clear"
    description = "Tool for googleSheets clear operation - clear operation"
    
    def _run(self, **kwargs):
        """Run the googleSheets clear operation."""
        # Implement the tool logic here
        return f"Running googleSheets clear operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleSheets clear operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
