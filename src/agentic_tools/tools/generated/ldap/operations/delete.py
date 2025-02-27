from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LdapCredentials

class LdapDeleteToolInput(BaseModel):
    attributes: Optional[Dict[str, Any]] = Field(None, description="Attributes to add to the entry")
    dn: Optional[str] = Field(None, description="The distinguished name of the entry to delete")
    node_debug: Optional[bool] = Field(None, description="Debug")
    operation: Optional[str] = Field(None, description="Operation")


class LdapDeleteTool(BaseTool):
    name: str = "ldap_delete"
    connector_id: str = "nodes-base.ldap"
    description: str = "Tool for ldap delete operation - delete operation"
    args_schema: type[BaseModel] | None = LdapDeleteToolInput
    credentials: Optional[LdapCredentials] = None
