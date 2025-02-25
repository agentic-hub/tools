from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglesheetsCredentials(BaseModel):
    """Credentials for googleSheets authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_sheets_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleSheetsOAuth2Api")

class GooglesheetsClearToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglesheetsCredentials] = Field(None, description="Custom credentials for authentication")
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
    name = "googlesheets_clear"
    description = "Tool for googleSheets clear operation - clear operation"
    
    def __init__(self, credentials: Optional[GooglesheetsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleSheets clear operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleSheets clear operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleSheets clear operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleSheets clear operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
