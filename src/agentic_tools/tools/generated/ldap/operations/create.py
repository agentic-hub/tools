from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LdapCredentials

class LdapCreateToolInput(BaseModel):
    attributes: Optional[Dict[str, Any]] = Field(None, description="Attributes to add to the entry")
    dn: Optional[str] = Field(None, description="The distinguished name of the entry to create")
    node_debug: Optional[bool] = Field(None, description="Debug")
    operation: Optional[str] = Field(None, description="Operation")


class LdapCreateTool(BaseTool):
    name: str = "ldap_create"
    connector_id: str = "nodes-base.ldap"
    description: str = "Tool for ldap create operation - create operation"
    args_schema: type[BaseModel] | None = LdapCreateToolInput
    credentials: Optional[LdapCredentials] = None
