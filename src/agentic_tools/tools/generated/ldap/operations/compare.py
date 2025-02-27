from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LdapCredentials

class LdapCompareToolInput(BaseModel):
    value: Optional[str] = Field(None, description="The value to compare")
    attributes: Optional[Dict[str, Any]] = Field(None, description="Attributes to add to the entry")
    id: Optional[str] = Field(None, description="The ID of the attribute to compare")
    dn: Optional[str] = Field(None, description="The distinguished name of the entry to compare")
    node_debug: Optional[bool] = Field(None, description="Debug")
    operation: Optional[str] = Field(None, description="Operation")


class LdapCompareTool(BaseTool):
    name: str = "ldap_compare"
    connector_id: str = "nodes-base.ldap"
    description: str = "Tool for ldap compare operation - compare operation"
    args_schema: type[BaseModel] | None = LdapCompareToolInput
    credentials: Optional[LdapCredentials] = None
