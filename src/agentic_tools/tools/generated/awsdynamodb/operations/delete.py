from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwsdynamodbCredentials(BaseModel):
    """Credentials for awsDynamoDb authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwsdynamodbDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwsdynamodbCredentials] = Field(None, description="Custom credentials for authentication")
    keys_ui: Optional[Dict[str, Any]] = Field(None, description="Item's primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.")
    filter_expression: Optional[str] = Field(None, description="A filter expression determines which items within the Scan results should be returned to you. All of the other results are discarded. Empty value will return all Scan results.")
    select: Optional[str] = Field(None, description="Select")
    operation: Optional[str] = Field(None, description="Operation")
    return_values: Optional[str] = Field(None, description="Use ReturnValues if you want to get the item attributes as they appeared before they were deleted")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    table_name: Optional[str] = Field(None, description="Table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class AwsdynamodbDeleteTool(BaseTool):
    name = "awsdynamodb_delete"
    description = "Tool for awsDynamoDb delete operation - delete operation"
    
    def __init__(self, credentials: Optional[AwsdynamodbCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsDynamoDb delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsDynamoDb delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsDynamoDb delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsDynamoDb delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
