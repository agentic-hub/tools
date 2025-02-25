from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PostgresCredentials(BaseModel):
    """Credentials for postgres authentication."""
    postgres: Optional[Dict[str, Any]] = Field(None, description="postgres")

class PostgresUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PostgresCredentials] = Field(None, description="Custom credentials for authentication")
    table: Optional[str] = Field(None, description="By Name")
    values_to_send: Optional[Dict[str, Any]] = Field(None, description="Values to Send")
    operation: Optional[str] = Field(None, description="Operation")
    schema: Optional[str] = Field(None, description="By Name")
    where: Optional[Dict[str, Any]] = Field(None, description="If not set, all rows will be selected")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    columns: Optional[str] = Field(None, description="columns")
    data_mode: Optional[str] = Field(None, description="Whether to map node input properties and the table data automatically or manually")
    resource: Optional[str] = Field(None, description="Resource")
    combine_conditions: Optional[str] = Field(None, description="How to combine the conditions defined in \"Select Rows\": AND requires all conditions to be true, OR requires at least one condition to be true")
    column_to_match_on: Optional[str] = Field(None, description="The column to compare when finding the rows to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\" target=\"_blank\">expression</a>.")
    value_to_match_on: Optional[str] = Field(None, description="Rows with a value in the specified \"Column to Match On\" that corresponds to the value in this field will be updated")
    notice: Optional[str] = Field(None, description="
		In this mode, make sure incoming data fields are named the same as the columns in your table. If needed, use an 'Edit Fields' node before this node to change the field names.
		")


class PostgresUpdateTool(BaseTool):
    name = "postgres_update"
    description = "Tool for postgres update operation - update operation"
    
    def __init__(self, credentials: Optional[PostgresCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the postgres update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running postgres update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running postgres update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the postgres update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
