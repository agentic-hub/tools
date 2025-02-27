from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LdapCredentials

class LdapUpdateToolInput(BaseModel):
    attributes: Optional[Dict[str, Any]] = Field(None, description="Update entry attributes")
    dn: Optional[str] = Field(None, description="The distinguished name of the entry to update")
    node_debug: Optional[bool] = Field(None, description="Debug")
    operation: Optional[str] = Field(None, description="Operation")


class LdapUpdateTool(BaseTool):
    name: str = "ldap_update"
    connector_id: str = "nodes-base.ldap"
    description: str = "Tool for ldap update operation - update operation"
    args_schema: type[BaseModel] | None = LdapUpdateToolInput
    credentials: Optional[LdapCredentials] = None
