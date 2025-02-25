from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DiscourseCredentials(BaseModel):
    """Credentials for discourse authentication."""
    discourse_api: Optional[Dict[str, Any]] = Field(None, description="discourseApi")

class DiscourseCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[DiscourseCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Content of the post")
    post_id: Optional[str] = Field(None, description="ID of the post")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    text_color: Optional[str] = Field(None, description="Text color of the category")
    email: Optional[str] = Field(None, description="Email of the user to create")
    usernames: Optional[str] = Field(None, description="Usernames to add to group. Multiples can be defined separated by comma.")
    password: Optional[str] = Field(None, description="The password of the user to create")
    operation: Optional[str] = Field(None, description="Choose an operation")
    color: Optional[str] = Field(None, description="Color of the category")
    name: Optional[str] = Field(None, description="Name of the category")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    username: Optional[str] = Field(None, description="The username of the user to create")
    group_id: Optional[str] = Field(None, description="ID of the group to update")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title of the post")


class DiscourseCreateTool(BaseTool):
    name = "discourse_create"
    description = "Tool for discourse create operation - create operation"
    
    def __init__(self, credentials: Optional[DiscourseCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the discourse create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running discourse create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running discourse create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the discourse create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
