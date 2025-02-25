from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GsuiteadminCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    makeAdmin: Optional[bool] = Field(None, description="Whether to make a user a super administrator")
    userId: Optional[str] = Field(None, description="The value can be the user's primary email address, alias email address, or unique user ID")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    lastName: Optional[str] = Field(None, description="Last Name")
    email: Optional[str] = Field(None, description="The group's email address. If your account has multiple domains, select the appropriate domain for the email address. The email must be unique")
    password: Optional[str] = Field(None, description="Stores the password for the user account. A minimum of 8 characters is required. The maximum length is 100 characters.")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    username: Optional[str] = Field(None, description="The username that will be set to the user. Example: If you domain is example.com and you set the username to jhon then the user's final email address will be jhon@example.com.")
    groupId: Optional[str] = Field(None, description="Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.")
    domain: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    projection: Optional[str] = Field(None, description="What subset of fields to fetch for this user")
    firstName: Optional[str] = Field(None, description="First Name")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class GsuiteadminCreateTool(BaseTool):
    name = "gsuiteadmin_create"
    description = "Tool for gSuiteAdmin create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the gSuiteAdmin create operation."""
        # Implement the tool logic here
        return f"Running gSuiteAdmin create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gSuiteAdmin create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
