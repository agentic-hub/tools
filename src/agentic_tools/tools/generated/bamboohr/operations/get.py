from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BamboohrGetToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    categoryId: Optional[str] = Field(None, description="Employee Document Category ID")
    location: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    employeeId: Optional[str] = Field(None, description="Employee ID")
    format: Optional[str] = Field(None, description="The output format for the report")
    mobilePhone: Optional[str] = Field(None, description="Mobile Phone")
    fileId: Optional[str] = Field(None, description="ID of the employee file")
    hireDate: Optional[str] = Field(None, description="Hire Date")
    synced: Optional[bool] = Field(None, description="Whether the employee to create was added to a pay schedule synced with Trax Payroll")
    maritalStatus: Optional[str] = Field(None, description="Marital Status")
    lastName: Optional[str] = Field(None, description="Last Name")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    dateOfBirth: Optional[str] = Field(None, description="Date of Birth")
    payRate: Optional[Dict[str, Any]] = Field(None, description="Pay Rate")
    binaryPropertyName: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded. Supported file types: PNG, JPEG.")
    paidPer: Optional[str] = Field(None, description="Pay Per")
    exempt: Optional[str] = Field(None, description="FLSA Overtime Status")
    employeeNumber: Optional[str] = Field(None, description="Employee Number")
    operation: Optional[str] = Field(None, description="Operation")
    ssn: Optional[str] = Field(None, description="A standard United States Social Security number, with dashes")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    department: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    reportId: Optional[str] = Field(None, description="ID of the report. You can get the report number by hovering over the report name on the reports page and grabbing the ID.")
    division: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    gender: Optional[str] = Field(None, description="Gender")
    simplifyOutput: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    firstName: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    payType: Optional[str] = Field(None, description="Pay Type")
    preferredName: Optional[str] = Field(None, description="Preferred Name")


class BamboohrGetTool(BaseTool):
    name = "bamboohr_get"
    description = "Tool for bambooHr get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the bambooHr get operation."""
        # Implement the tool logic here
        return f"Running bambooHr get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the bambooHr get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
