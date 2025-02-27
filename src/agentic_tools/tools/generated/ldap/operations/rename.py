from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LdapCredentials

class LdapRenameToolInput(BaseModel):
    attributes: Optional[Dict[str, Any]] = Field(None, description="Attributes to add to the entry")
    target_dn: Optional[str] = Field(None, description="The new distinguished name for the entry")
    dn: Optional[str] = Field(None, description="The distinguished name of the entry to rename")
    node_debug: Optional[bool] = Field(None, description="Debug")
    operation: Optional[str] = Field(None, description="Operation")


class LdapRenameTool(BaseTool):
    name: str = "ldap_rename"
    description: str = "Tool for ldap rename operation - rename operation"
    args_schema: type[BaseModel] | None = LdapRenameToolInput
    credentials: Optional[LdapCredentials] = None
