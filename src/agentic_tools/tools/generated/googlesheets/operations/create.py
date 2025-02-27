from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglesheetsCredentials

class GooglesheetsCreateToolInput(BaseModel):
    start_index: Optional[float] = Field(None, description="The row number to delete from, The first row is 1")
    document_id: Optional[Dict[str, Any]] = Field(None, description="Document")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    sheets_ui: Optional[Dict[str, Any]] = Field(None, description="Sheets")
    number_to_delete: Optional[float] = Field(None, description="Number of Rows to Delete")
    columns: Optional[str] = Field(None, description="columns")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    data_mode: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    resource: Optional[str] = Field(None, description="Resource")
    column_to_match_on: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    value_to_match_on: Optional[str] = Field(None, description="Value of Column to Match On")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="The name of the sheet")


class GooglesheetsCreateTool(BaseTool):
    name: str = "googlesheets_create"
    description: str = "Tool for googleSheets create operation - create operation"
    args_schema: type[BaseModel] | None = GooglesheetsCreateToolInput
    credentials: Optional[GooglesheetsCredentials] = None
