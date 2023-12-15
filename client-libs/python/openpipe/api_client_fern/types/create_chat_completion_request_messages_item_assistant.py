# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .create_chat_completion_request_messages_item_assistant_content import (
    CreateChatCompletionRequestMessagesItemAssistantContent,
)
from .create_chat_completion_request_messages_item_assistant_function_call import (
    CreateChatCompletionRequestMessagesItemAssistantFunctionCall,
)
from .create_chat_completion_request_messages_item_assistant_tool_calls_item import (
    CreateChatCompletionRequestMessagesItemAssistantToolCallsItem,
)

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreateChatCompletionRequestMessagesItemAssistant(pydantic.BaseModel):
    content: CreateChatCompletionRequestMessagesItemAssistantContent
    function_call: typing.Optional[CreateChatCompletionRequestMessagesItemAssistantFunctionCall]
    tool_calls: typing.Optional[typing.List[CreateChatCompletionRequestMessagesItemAssistantToolCallsItem]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
