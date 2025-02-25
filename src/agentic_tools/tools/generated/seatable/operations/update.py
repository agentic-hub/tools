from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SeatableCredentials(BaseModel):
    """Credentials for seaTable authentication."""
    sea_table_api: Optional[Dict[str, Any]] = Field(None, description="seaTableApi")

class SeatableUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SeatableCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    columns_ui: Optional[Dict[str, Any]] = Field(None, description="Add destination column with its value")
    fields_to_send: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    row_id: Optional[str] = Field(None, description="Row ID")
    operation: Optional[str] = Field(None, description="The operation being performed")
    table_name: Optional[str] = Field(None, description="The name of SeaTable table to access. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class SeatableUpdateTool(BaseTool):
    name = "seatable_update"
    description = "Tool for seaTable update operation - update operation"
    
    def __init__(self, credentials: Optional[SeatableCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the seaTable update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running seaTable update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running seaTable update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the seaTable update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
