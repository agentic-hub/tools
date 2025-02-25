from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BamboohrCredentials(BaseModel):
    """Credentials for bambooHr authentication."""
    bamboo_hr_api: Optional[Dict[str, Any]] = Field(None, description="bambooHrApi")

class BamboohrUploadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[BamboohrCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    category_id: Optional[str] = Field(None, description="Employee Document Category ID")
    location: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    employee_id: Optional[str] = Field(None, description="ID of the employee")
    mobile_phone: Optional[str] = Field(None, description="Mobile Phone")
    file_id: Optional[str] = Field(None, description="ID of the employee file")
    hire_date: Optional[str] = Field(None, description="Hire Date")
    synced: Optional[bool] = Field(None, description="Whether the employee to create was added to a pay schedule synced with Trax Payroll")
    marital_status: Optional[str] = Field(None, description="Marital Status")
    last_name: Optional[str] = Field(None, description="Last Name")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    date_of_birth: Optional[str] = Field(None, description="Date of Birth")
    pay_rate: Optional[Dict[str, Any]] = Field(None, description="Pay Rate")
    binary_property_name: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded. Supported file types: PNG, JPEG.")
    paid_per: Optional[str] = Field(None, description="Pay Per")
    exempt: Optional[str] = Field(None, description="FLSA Overtime Status")
    employee_number: Optional[str] = Field(None, description="Employee Number")
    operation: Optional[str] = Field(None, description="Operation")
    ssn: Optional[str] = Field(None, description="A standard United States Social Security number, with dashes")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    department: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    division: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    gender: Optional[str] = Field(None, description="Gender")
    simplify_output: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    first_name: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    pay_type: Optional[str] = Field(None, description="Pay Type")
    preferred_name: Optional[str] = Field(None, description="Preferred Name")


class BamboohrUploadTool(BaseTool):
    name = "bamboohr_upload"
    description = "Tool for bambooHr upload operation - upload operation"
    
    def __init__(self, credentials: Optional[BamboohrCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the bambooHr upload operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running bambooHr upload operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running bambooHr upload operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the bambooHr upload operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
