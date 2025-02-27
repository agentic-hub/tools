from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LinkedinCredentials

class LinkedinCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    organization: Optional[str] = Field(None, description="URN of Organization as which the post should be posted as")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    person: Optional[str] = Field(None, description="Person as which the post should be posted as. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    authentication: Optional[str] = Field(None, description="Authentication")
    post_as: Optional[str] = Field(None, description="If to post on behalf of a user or an organization")
    text: Optional[str] = Field(None, description="The primary content of the post")
    share_media_category: Optional[str] = Field(None, description="Media Category")
    operation: Optional[str] = Field(None, description="Operation")


class LinkedinCreateTool(BaseTool):
    name: str = "linkedin_create"
    description: str = "Tool for linkedIn create operation - create operation"
    args_schema: type[BaseModel] | None = LinkedinCreateToolInput
    credentials: Optional[LinkedinCredentials] = None
