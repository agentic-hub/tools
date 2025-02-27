from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BamboohrCredentials

class BamboohrGetallToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    category_id: Optional[str] = Field(None, description="Employee Document Category ID")
    location: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    employee_id: Optional[str] = Field(None, description="Employee ID")
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


class BamboohrGetallTool(BaseTool):
    name: str = "bamboohr_getall"
    connector_id: str = "nodes-base.bambooHr"
    description: str = "Tool for bambooHr getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = BamboohrGetallToolInput
    credentials: Optional[BamboohrCredentials] = None
