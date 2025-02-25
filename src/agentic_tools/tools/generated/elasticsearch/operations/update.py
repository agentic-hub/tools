from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ElasticsearchCredentials(BaseModel):
    """Credentials for elasticsearch authentication."""
    elasticsearch_api: Optional[Dict[str, Any]] = Field(None, description="elasticsearchApi")

class ElasticsearchUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ElasticsearchCredentials] = Field(None, description="Custom credentials for authentication")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    index_id: Optional[str] = Field(None, description="ID of the document to update")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    data_to_send: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    document_id: Optional[str] = Field(None, description="ID of the document to update")
    operation: Optional[str] = Field(None, description="Operation")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")


class ElasticsearchUpdateTool(BaseTool):
    name = "elasticsearch_update"
    description = "Tool for elasticsearch update operation - update operation"
    
    def __init__(self, credentials: Optional[ElasticsearchCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the elasticsearch update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running elasticsearch update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running elasticsearch update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the elasticsearch update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
