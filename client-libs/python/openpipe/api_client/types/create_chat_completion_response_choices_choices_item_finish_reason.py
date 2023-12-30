# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CreateChatCompletionResponseChoicesChoicesItemFinishReason(str, enum.Enum):
    LENGTH = "length"
    FUNCTION_CALL = "function_call"
    TOOL_CALLS = "tool_calls"
    STOP = "stop"
    CONTENT_FILTER = "content_filter"

    def visit(
        self,
        length: typing.Callable[[], T_Result],
        function_call: typing.Callable[[], T_Result],
        tool_calls: typing.Callable[[], T_Result],
        stop: typing.Callable[[], T_Result],
        content_filter: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateChatCompletionResponseChoicesChoicesItemFinishReason.LENGTH:
            return length()
        if self is CreateChatCompletionResponseChoicesChoicesItemFinishReason.FUNCTION_CALL:
            return function_call()
        if self is CreateChatCompletionResponseChoicesChoicesItemFinishReason.TOOL_CALLS:
            return tool_calls()
        if self is CreateChatCompletionResponseChoicesChoicesItemFinishReason.STOP:
            return stop()
        if self is CreateChatCompletionResponseChoicesChoicesItemFinishReason.CONTENT_FILTER:
            return content_filter()
