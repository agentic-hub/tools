from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglesheetsCredentials

class GooglesheetsClearToolInput(BaseModel):
    keep_first_row: Optional[bool] = Field(None, description="Keep First Row")
    start_index: Optional[float] = Field(None, description="The row number to delete from, The first row is 1")
    document_id: Optional[Dict[str, Any]] = Field(None, description="Document")
    operation: Optional[str] = Field(None, description="Operation")
    range: Optional[str] = Field(None, description="The table range to read from or to append data to. See the Google <a href=\"https://developers.google.com/sheets/api/guides/values#writing\">documentation</a> for the details. If it contains multiple sheets it can also be added like this: \"MySheet!A:F\"")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    number_to_delete: Optional[float] = Field(None, description="Number of Rows to Delete")
    columns: Optional[str] = Field(None, description="columns")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    data_mode: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    rows_to_delete: Optional[float] = Field(None, description="Number of Rows to Delete")
    sheet_name: Optional[str] = Field(None, description="By URL")
    resource: Optional[str] = Field(None, description="Resource")
    columns_to_delete: Optional[float] = Field(None, description="Number of Columns to Delete")
    column_to_match_on: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    value_to_match_on: Optional[str] = Field(None, description="Value of Column to Match On")
    authentication: Optional[str] = Field(None, description="Authentication")
    clear: Optional[str] = Field(None, description="What to clear")
    title: Optional[str] = Field(None, description="The name of the sheet")


class GooglesheetsClearTool(BaseTool):
    name: str = "googlesheets_clear"
    connector_id: str = "nodes-base.googleSheets"
    description: str = "Tool for googleSheets clear operation - clear operation"
    args_schema: type[BaseModel] | None = GooglesheetsClearToolInput
    credentials: Optional[GooglesheetsCredentials] = None
