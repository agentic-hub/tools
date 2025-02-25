# slack operations
from typing import List
from langchain.tools import BaseTool
from .. import SlackCredentials

def get_tools() -> List[BaseTool]:
    """Get all slack operation tools."""
    tools = []
    from .archive import SlackArchiveTool
    tools.append(SlackArchiveTool())
    from .close import SlackCloseTool
    tools.append(SlackCloseTool())
    from .create import SlackCreateTool
    tools.append(SlackCreateTool())
    from .get import SlackGetTool
    tools.append(SlackGetTool())
    from .getall import SlackGetallTool
    tools.append(SlackGetallTool())
    from .history import SlackHistoryTool
    tools.append(SlackHistoryTool())
    from .invite import SlackInviteTool
    tools.append(SlackInviteTool())
    from .join import SlackJoinTool
    tools.append(SlackJoinTool())
    from .kick import SlackKickTool
    tools.append(SlackKickTool())
    from .leave import SlackLeaveTool
    tools.append(SlackLeaveTool())
    from .member import SlackMemberTool
    tools.append(SlackMemberTool())
    from .open import SlackOpenTool
    tools.append(SlackOpenTool())
    from .rename import SlackRenameTool
    tools.append(SlackRenameTool())
    from .replies import SlackRepliesTool
    tools.append(SlackRepliesTool())
    from .setpurpose import SlackSetpurposeTool
    tools.append(SlackSetpurposeTool())
    from .settopic import SlackSettopicTool
    tools.append(SlackSettopicTool())
    from .unarchive import SlackUnarchiveTool
    tools.append(SlackUnarchiveTool())
    from .delete import SlackDeleteTool
    tools.append(SlackDeleteTool())
    from .getpermalink import SlackGetpermalinkTool
    tools.append(SlackGetpermalinkTool())
    from .search import SlackSearchTool
    tools.append(SlackSearchTool())
    from .post import SlackPostTool
    tools.append(SlackPostTool())
    from .update import SlackUpdateTool
    tools.append(SlackUpdateTool())
    from .add import SlackAddTool
    tools.append(SlackAddTool())
    from .delete import SlackDeleteTool
    tools.append(SlackDeleteTool())
    from .getall import SlackGetallTool
    tools.append(SlackGetallTool())
    from .get import SlackGetTool
    tools.append(SlackGetTool())
    from .getall import SlackGetallTool
    tools.append(SlackGetallTool())
    from .upload import SlackUploadTool
    tools.append(SlackUploadTool())
    from .add import SlackAddTool
    tools.append(SlackAddTool())
    from .get import SlackGetTool
    tools.append(SlackGetTool())
    from .remove import SlackRemoveTool
    tools.append(SlackRemoveTool())
    from .info import SlackInfoTool
    tools.append(SlackInfoTool())
    from .getall import SlackGetallTool
    tools.append(SlackGetallTool())
    from .getprofile import SlackGetprofileTool
    tools.append(SlackGetprofileTool())
    from .getpresence import SlackGetpresenceTool
    tools.append(SlackGetpresenceTool())
    from .updateprofile import SlackUpdateprofileTool
    tools.append(SlackUpdateprofileTool())
    from .create import SlackCreateTool
    tools.append(SlackCreateTool())
    from .disable import SlackDisableTool
    tools.append(SlackDisableTool())
    from .enable import SlackEnableTool
    tools.append(SlackEnableTool())
    from .getall import SlackGetallTool
    tools.append(SlackGetallTool())
    from .update import SlackUpdateTool
    tools.append(SlackUpdateTool())
    return tools
