from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FilemakerCredentials(BaseModel):
    """Credentials for filemaker authentication."""
    file_maker: Optional[Dict[str, Any]] = Field(None, description="fileMaker")

class FilemakerDefaultToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[FilemakerCredentials] = Field(None, description="Custom credentials for authentication")
    offset: Optional[float] = Field(None, description="The record number of the first record in the range of records")
    layout: Optional[str] = Field(None, description="FileMaker Layout Name. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    get_portals: Optional[bool] = Field(None, description="Whether to get portal data as well")
    set_sort: Optional[bool] = Field(None, description="Whether to sort data")
    response_layout: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    fields_parameters_ui: Optional[Dict[str, Any]] = Field(None, description="Fields to define")
    set_script_after: Optional[bool] = Field(None, description="Whether to define a script to be run after the action specified by the API call but before the subsequent sort")
    script_sort: Optional[str] = Field(None, description="The name of the FileMaker script to be run after the action specified by the API call but before the subsequent sort. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    set_script_sort: Optional[bool] = Field(None, description="Whether to define a script to be run after the action specified by the API call but before the subsequent sort")
    script_after_param: Optional[str] = Field(None, description="A parameter for the FileMaker script")
    script_sort_param: Optional[str] = Field(None, description="A parameter for the FileMaker script")
    mod_id: Optional[float] = Field(None, description="The last modification ID. When you use modId, a record is edited only when the modId matches.")
    script_before: Optional[str] = Field(None, description="The name of the FileMaker script to be run after the action specified by the API call and after the subsequent sort. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    queries: Optional[Dict[str, Any]] = Field(None, description="Queries")
    script_after: Optional[str] = Field(None, description="The name of the FileMaker script to be run after the action specified by the API call and after the subsequent sort. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    sort_parameters_ui: Optional[Dict[str, Any]] = Field(None, description="Sort rules")
    action: Optional[str] = Field(None, description="Action")
    script: Optional[str] = Field(None, description="The name of the FileMaker script to be run. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    script_before_param: Optional[str] = Field(None, description="A parameter for the FileMaker script")
    portals: Optional[str] = Field(None, description="The portal result set to return. Use the portal object name or portal table name. If this parameter is omitted, the API will return all portal objects and records in the layout. For best performance, pass the portal object name or portal table name. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    set_script_before: Optional[bool] = Field(None, description="Whether to define a script to be run before the action specified by the API call and after the subsequent sort")
    script_param: Optional[str] = Field(None, description="A parameter for the FileMaker script")
    recid: Optional[float] = Field(None, description="Internal Record ID returned by get (recordid)")


class FilemakerDefaultTool(BaseTool):
    name = "filemaker_default"
    description = "Tool for filemaker default operation - default operation"
    
    def __init__(self, credentials: Optional[FilemakerCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the filemaker default operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running filemaker default operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running filemaker default operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the filemaker default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
