from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LdapCredentials

class LdapSearchToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    base_dn: Optional[str] = Field(None, description="The distinguished name of the subtree to search in")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    attributes: Optional[Dict[str, Any]] = Field(None, description="Attributes to add to the entry")
    attribute: Optional[str] = Field(None, description="Attribute to search for")
    search_text: Optional[str] = Field(None, description="Text to search for, Use * for a wildcard")
    search_for: Optional[str] = Field(None, description="Directory object class to search for")
    dn: Optional[str] = Field(None, description="The distinguished name of the entry to compare")
    node_debug: Optional[bool] = Field(None, description="Debug")
    operation: Optional[str] = Field(None, description="Operation")
    custom_filter: Optional[str] = Field(None, description="Custom LDAP filter. Escape these chars * ( ) \ with a backslash \"\\".")


class LdapSearchTool(BaseTool):
    name: str = "ldap_search"
    connector_id: str = "nodes-base.ldap"
    description: str = "Tool for ldap search operation - search operation"
    args_schema: type[BaseModel] | None = LdapSearchToolInput
    credentials: Optional[LdapCredentials] = None
