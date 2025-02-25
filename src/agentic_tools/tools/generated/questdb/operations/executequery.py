from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class QuestdbCredentials(BaseModel):
    """Credentials for questDb authentication."""
    quest_db: Optional[Dict[str, Any]] = Field(None, description="questDb")

class QuestdbExecutequeryToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[QuestdbCredentials] = Field(None, description="Custom credentials for authentication")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    query: Optional[str] = Field(None, description="The SQL query to execute. You can use n8n expressions or $1 and $2 in conjunction with query parameters.")
    operation: Optional[str] = Field(None, description="Operation")


class QuestdbExecutequeryTool(BaseTool):
    name = "questdb_executequery"
    description = "Tool for questDb executeQuery operation - executeQuery operation"
    
    def __init__(self, credentials: Optional[QuestdbCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the questDb executeQuery operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running questDb executeQuery operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running questDb executeQuery operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the questDb executeQuery operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
