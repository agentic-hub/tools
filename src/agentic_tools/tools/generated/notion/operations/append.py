from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NotionCredentials(BaseModel):
    """Credentials for notion authentication."""
    notion_api: Optional[Dict[str, Any]] = Field(None, description="notionApi")

class NotionAppendToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[NotionCredentials] = Field(None, description="Custom credentials for authentication")
    database_id: Optional[Dict[str, Any]] = Field(None, description="The Notion Database to get")
    page_id: Optional[Dict[str, Any]] = Field(None, description="The Notion Database Page to update")
    text: Optional[str] = Field(None, description="The text to search for")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    block_ui: Optional[Dict[str, Any]] = Field(None, description="Blocks")
    operation: Optional[str] = Field(None, description="Operation")
    credentials: Optional[str] = Field(None, description="Credentials")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    block_id: Optional[Dict[str, Any]] = Field(None, description="The Notion Block to append blocks to")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    properties_ui: Optional[Dict[str, Any]] = Field(None, description="Properties")
    title: Optional[str] = Field(None, description="Page title. Appears at the top of the page and can be found via Quick Find.")
    notion_notice: Optional[str] = Field(None, description="In Notion, make sure to <a href=\"https://www.notion.so/help/add-and-manage-connections-with-the-api\" target=\"_blank\">add your connection</a> to the pages you want to access.")


class NotionAppendTool(BaseTool):
    name = "notion_append"
    description = "Tool for notion append operation - append operation"
    
    def __init__(self, credentials: Optional[NotionCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the notion append operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running notion append operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running notion append operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the notion append operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
