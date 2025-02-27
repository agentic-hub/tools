# ldap operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import LdapCredentials

def get_tools() -> List[BaseTool]:
    """Get all ldap operation tools."""
    tools = []
    from .compare import LdapCompareTool
    tools.append(LdapCompareTool())
    from .create import LdapCreateTool
    tools.append(LdapCreateTool())
    from .delete import LdapDeleteTool
    tools.append(LdapDeleteTool())
    from .rename import LdapRenameTool
    tools.append(LdapRenameTool())
    from .search import LdapSearchTool
    tools.append(LdapSearchTool())
    from .update import LdapUpdateTool
    tools.append(LdapUpdateTool())
    return tools
