from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GristCredentials(BaseModel):
    """Credentials for grist authentication."""
    grist_api: Optional[Dict[str, Any]] = Field(None, description="gristApi")

class GristUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GristCredentials] = Field(None, description="Custom credentials for authentication")
    doc_id: Optional[str] = Field(None, description="In your document, click your profile icon, then Document Settings, then copy the value under \"This document's ID\"")
    table_id: Optional[str] = Field(None, description="ID of table to operate on. If unsure, look at the Code View.")
    fields_to_send: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    data_to_send: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    row_id: Optional[str] = Field(None, description="ID of the row to update")
    operation: Optional[str] = Field(None, description="Operation")


class GristUpdateTool(BaseTool):
    name = "grist_update"
    description = "Tool for grist update operation - update operation"
    
    def __init__(self, credentials: Optional[GristCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the grist update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running grist update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running grist update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the grist update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
