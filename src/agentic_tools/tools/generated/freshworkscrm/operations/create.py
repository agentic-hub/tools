from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshworkscrmCredentials(BaseModel):
    """Credentials for freshworksCrm authentication."""
    freshworks_crm_api: Optional[Dict[str, Any]] = Field(None, description="freshworksCrmApi")

class FreshworkscrmCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[FreshworkscrmCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    appointment_id: Optional[str] = Field(None, description="ID of the appointment to delete")
    sales_activity_type_id: Optional[str] = Field(None, description="ID of a sales activity type for which the sales activity is created. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    description: Optional[str] = Field(None, description="Content of the note")
    from_date: Optional[str] = Field(None, description="Timestamp that denotes the end of sales activity")
    view: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="Last name of the contact")
    from_date: Optional[str] = Field(None, description="Timestamp that denotes the start of appointment. Start date if this is an all-day appointment.")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="ID of the account to delete")
    task_id: Optional[str] = Field(None, description="ID of the task to delete")
    name: Optional[str] = Field(None, description="Name of the account")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    targetable_type: Optional[str] = Field(None, description="Type of the entity for which the note is created")
    end_date: Optional[str] = Field(None, description="Timestamp that denotes the end of sales activity")
    entities: Optional[str] = Field(None, description="entities")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    targetable_id: Optional[str] = Field(None, description="ID of the entity for which note is created. The type of entity is selected in \"Target Type\".")
    end_date: Optional[str] = Field(None, description="Timestamp that denotes the end of appointment. End date if this is an all-day appointment.")
    emails: Optional[str] = Field(None, description="Email addresses of the contact")
    deal_id: Optional[str] = Field(None, description="ID of the deal to delete")
    sales_activity_id: Optional[str] = Field(None, description="ID of the salesActivity to delete")
    first_name: Optional[str] = Field(None, description="First name of the contact")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    owner_id: Optional[str] = Field(None, description="ID of the user who owns the sales activity. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    due_date: Optional[str] = Field(None, description="Timestamp that denotes when the task is due to be completed")
    contact_id: Optional[str] = Field(None, description="ID of the contact to delete")
    note_id: Optional[str] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="Title of the appointment")
    amount: Optional[float] = Field(None, description="Value of the deal")
    attendees: Optional[Dict[str, Any]] = Field(None, description="Attendees")


class FreshworkscrmCreateTool(BaseTool):
    name = "freshworkscrm_create"
    description = "Tool for freshworksCrm create operation - create operation"
    
    def __init__(self, credentials: Optional[FreshworkscrmCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the freshworksCrm create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running freshworksCrm create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running freshworksCrm create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshworksCrm create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
