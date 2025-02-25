from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendinblueCredentials(BaseModel):
    """Credentials for sendInBlue authentication."""
    send_in_blue_api: Optional[Dict[str, Any]] = Field(None, description="sendInBlueApi")

class SendinblueUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SendinblueCredentials] = Field(None, description="Custom credentials for authentication")
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    update_attributes: Optional[Dict[str, Any]] = Field(None, description="Array of attributes to be updated")
    update_attribute_category_list: Optional[Dict[str, Any]] = Field(None, description="List of the values and labels that the attribute can take")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    update_attribute_category: Optional[str] = Field(None, description="Category of the attribute")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    update_attribute_name: Optional[str] = Field(None, description="Name of the existing attribute")
    update_attribute_value: Optional[str] = Field(None, description="Value of the attribute to update")


class SendinblueUpdateTool(BaseTool):
    name = "sendinblue_update"
    description = "Tool for sendInBlue update operation - update operation"
    
    def __init__(self, credentials: Optional[SendinblueCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the sendInBlue update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running sendInBlue update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running sendInBlue update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendInBlue update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
