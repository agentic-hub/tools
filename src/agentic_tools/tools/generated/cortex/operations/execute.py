from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CortexCredentials(BaseModel):
    """Credentials for cortex authentication."""
    cortex_api: Optional[Dict[str, Any]] = Field(None, description="cortexApi")

class CortexExecuteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CortexCredentials] = Field(None, description="Custom credentials for authentication")
    json_object: Optional[bool] = Field(None, description="Choose between providing JSON object or seperated attributes")
    object_data: Optional[str] = Field(None, description="Entity Object (JSON)")
    resource: Optional[str] = Field(None, description="Choose a resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    observable_value: Optional[str] = Field(None, description="Enter the observable value")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    entity_type: Optional[str] = Field(None, description="Choose the Data type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    responder: Optional[str] = Field(None, description="Choose the responder. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    analyzer: Optional[str] = Field(None, description="Choose the analyzer. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    observable_type: Optional[str] = Field(None, description="Choose the observable type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Parameters")
    tlp: Optional[str] = Field(None, description="The TLP of the analyzed observable")
    operation: Optional[str] = Field(None, description="Choose an operation")


class CortexExecuteTool(BaseTool):
    name = "cortex_execute"
    description = "Tool for cortex execute operation - execute operation"
    
    def __init__(self, credentials: Optional[CortexCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the cortex execute operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running cortex execute operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running cortex execute operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cortex execute operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
