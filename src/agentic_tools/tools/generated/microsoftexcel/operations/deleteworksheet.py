from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftexcelCredentials(BaseModel):
    """Credentials for microsoftExcel authentication."""
    microsoft_excel_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftExcelOAuth2Api")

class MicrosoftexcelDeleteworksheetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MicrosoftexcelCredentials] = Field(None, description="Custom credentials for authentication")
    data: Optional[str] = Field(None, description="Raw values for the specified range as array of string arrays in JSON format")
    workbook: Optional[Dict[str, Any]] = Field(None, description="Workbook")
    table: Optional[Dict[str, Any]] = Field(None, description="Table")
    worksheet: Optional[Dict[str, Any]] = Field(None, description="Sheet")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    use_range: Optional[bool] = Field(None, description="Select a Range")
    raw_data: Optional[bool] = Field(None, description="Whether the data should be returned RAW instead of parsed into keys according to their header")
    operation: Optional[str] = Field(None, description="Operation")
    range: Optional[str] = Field(None, description="The range of cells that will be converted to a table")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    data_property: Optional[str] = Field(None, description="The name of the property into which to write the RAW data")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Values to Send")
    data_mode: Optional[str] = Field(None, description="Data Mode")
    resource: Optional[str] = Field(None, description="Resource")
    column_to_match_on: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    value_to_match_on: Optional[str] = Field(None, description="Value of Column to Match On")
    notice: Optional[str] = Field(None, description="This node connects to the Microsoft 365 cloud platform. Use the 'Extract From File' and 'Convert to File' nodes to directly manipulate spreadsheet files (.xls, .csv, etc). <a href=\"/templates/890\" target=\"_blank\">More info</a>.")


class MicrosoftexcelDeleteworksheetTool(BaseTool):
    name = "microsoftexcel_deleteworksheet"
    description = "Tool for microsoftExcel deleteWorksheet operation - deleteWorksheet operation"
    
    def __init__(self, credentials: Optional[MicrosoftexcelCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the microsoftExcel deleteWorksheet operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running microsoftExcel deleteWorksheet operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running microsoftExcel deleteWorksheet operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftExcel deleteWorksheet operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
