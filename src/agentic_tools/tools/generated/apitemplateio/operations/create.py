from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ApitemplateioCredentials(BaseModel):
    """Credentials for apiTemplateIo authentication."""
    api_template_io_api: Optional[Dict[str, Any]] = Field(None, description="apiTemplateIoApi")

class ApitemplateioCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ApitemplateioCredentials] = Field(None, description="Custom credentials for authentication")
    image_template_id: Optional[str] = Field(None, description="ID of the image template to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    download: Optional[bool] = Field(None, description="Name of the binary property to which to write the data of the read file")
    resource: Optional[str] = Field(None, description="Resource")
    properties_json: Optional[str] = Field(None, description="Properties (JSON)")
    properties_ui: Optional[Dict[str, Any]] = Field(None, description="Properties")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    pdf_template_id: Optional[str] = Field(None, description="ID of the PDF template to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    binary_property: Optional[str] = Field(None, description="Put Output File in Field")
    overrides_json: Optional[str] = Field(None, description="Overrides (JSON)")
    operation: Optional[str] = Field(None, description="Operation")
    overrides_ui: Optional[Dict[str, Any]] = Field(None, description="Overrides")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class ApitemplateioCreateTool(BaseTool):
    name = "apitemplateio_create"
    description = "Tool for apiTemplateIo create operation - create operation"
    
    def __init__(self, credentials: Optional[ApitemplateioCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the apiTemplateIo create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running apiTemplateIo create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running apiTemplateIo create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the apiTemplateIo create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
