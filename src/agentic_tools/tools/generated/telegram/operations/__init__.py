# telegram operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import TelegramCredentials

def get_tools() -> List[BaseTool]:
    """Get all telegram operation tools."""
    tools = []
    from .get import TelegramGetTool
    tools.append(TelegramGetTool())
    from .administrators import TelegramAdministratorsTool
    tools.append(TelegramAdministratorsTool())
    from .member import TelegramMemberTool
    tools.append(TelegramMemberTool())
    from .leave import TelegramLeaveTool
    tools.append(TelegramLeaveTool())
    from .setdescription import TelegramSetdescriptionTool
    tools.append(TelegramSetdescriptionTool())
    from .settitle import TelegramSettitleTool
    tools.append(TelegramSettitleTool())
    from .answerquery import TelegramAnswerqueryTool
    tools.append(TelegramAnswerqueryTool())
    from .answerinlinequery import TelegramAnswerinlinequeryTool
    tools.append(TelegramAnswerinlinequeryTool())
    from .get import TelegramGetTool
    tools.append(TelegramGetTool())
    from .deletemessage import TelegramDeletemessageTool
    tools.append(TelegramDeletemessageTool())
    from .editmessagetext import TelegramEditmessagetextTool
    tools.append(TelegramEditmessagetextTool())
    from .pinchatmessage import TelegramPinchatmessageTool
    tools.append(TelegramPinchatmessageTool())
    from .sendanimation import TelegramSendanimationTool
    tools.append(TelegramSendanimationTool())
    from .sendaudio import TelegramSendaudioTool
    tools.append(TelegramSendaudioTool())
    from .sendchataction import TelegramSendchatactionTool
    tools.append(TelegramSendchatactionTool())
    from .senddocument import TelegramSenddocumentTool
    tools.append(TelegramSenddocumentTool())
    from .sendlocation import TelegramSendlocationTool
    tools.append(TelegramSendlocationTool())
    from .sendmediagroup import TelegramSendmediagroupTool
    tools.append(TelegramSendmediagroupTool())
    from .sendmessage import TelegramSendmessageTool
    tools.append(TelegramSendmessageTool())
    from .sendphoto import TelegramSendphotoTool
    tools.append(TelegramSendphotoTool())
    from .sendsticker import TelegramSendstickerTool
    tools.append(TelegramSendstickerTool())
    from .sendvideo import TelegramSendvideoTool
    tools.append(TelegramSendvideoTool())
    from .unpinchatmessage import TelegramUnpinchatmessageTool
    tools.append(TelegramUnpinchatmessageTool())
    return tools
