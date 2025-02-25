from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SupabaseCredentials(BaseModel):
    """Credentials for supabase authentication."""
    supabase_api: Optional[Dict[str, Any]] = Field(None, description="supabaseApi")

class SupabaseCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SupabaseCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filter to decide which rows get updated")
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filter_type: Optional[str] = Field(None, description="Select Type")
    data_to_send: Optional[str] = Field(None, description="Data to Send")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    filter_string: Optional[str] = Field(None, description="Filters (String)")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    operation: Optional[str] = Field(None, description="Operation")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://postgrest.org/en/v9.0/api.html#horizontal-filtering-rows\" target=\"_blank\">PostgREST guide</a> to creating filters")
    match_type: Optional[str] = Field(None, description="Must Match")


class SupabaseCreateTool(BaseTool):
    name = "supabase_create"
    description = "Tool for supabase create operation - create operation"
    
    def __init__(self, credentials: Optional[SupabaseCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the supabase create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running supabase create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running supabase create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the supabase create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
