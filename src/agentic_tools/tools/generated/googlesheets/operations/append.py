from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglesheetsCredentials(BaseModel):
    """Credentials for googleSheets authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_sheets_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleSheetsOAuth2Api")

class GooglesheetsAppendToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglesheetsCredentials] = Field(None, description="Custom credentials for authentication")
    auto_map_notice: Optional[str] = Field(None, description="In this mode, make sure the incoming data is named the same as the columns in your Sheet. (Use an 'Edit Fields' node before this node to change it if required.)")
    start_index: Optional[float] = Field(None, description="The row number to delete from, The first row is 1")
    document_id: Optional[Dict[str, Any]] = Field(None, description="Document")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    number_to_delete: Optional[float] = Field(None, description="Number of Rows to Delete")
    columns: Optional[str] = Field(None, description="columns")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    data_mode: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    sheet_name: Optional[str] = Field(None, description="By URL")
    resource: Optional[str] = Field(None, description="Resource")
    column_to_match_on: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    value_to_match_on: Optional[str] = Field(None, description="Value of Column to Match On")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="The name of the sheet")


class GooglesheetsAppendTool(BaseTool):
    name = "googlesheets_append"
    description = "Tool for googleSheets append operation - append operation"
    
    def __init__(self, credentials: Optional[GooglesheetsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleSheets append operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleSheets append operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleSheets append operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleSheets append operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
