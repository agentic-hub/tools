from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MondaycomCredentials(BaseModel):
    """Credentials for mondayCom authentication."""
    monday_com_api: Optional[Dict[str, Any]] = Field(None, description="mondayComApi")
    monday_com_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="mondayComOAuth2Api")

class MondaycomChangecolumnvalueToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MondaycomCredentials] = Field(None, description="Custom credentials for authentication")
    item_id: Optional[str] = Field(None, description="The unique identifier of the item to to change column of")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="The column value in JSON format. Documentation can be found <a href=\"https://monday.com/developers/v2#mutations-section-columns-change-column-value\">here</a>.")
    column_id: Optional[str] = Field(None, description="The column's unique identifier. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The board's name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    board_id: Optional[str] = Field(None, description="The unique identifier of the board. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    group_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class MondaycomChangecolumnvalueTool(BaseTool):
    name = "mondaycom_changecolumnvalue"
    description = "Tool for mondayCom changeColumnValue operation - changeColumnValue operation"
    
    def __init__(self, credentials: Optional[MondaycomCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mondayCom changeColumnValue operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mondayCom changeColumnValue operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mondayCom changeColumnValue operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mondayCom changeColumnValue operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
