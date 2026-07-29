import pytest
from unittest.mock import AsyncMock, MagicMock
from app.handlers.start import cmd_start

@pytest.mark.asyncio
async def test_cmd_start_greets_new_user():
    message = MagicMock()
    message.from_user.id = 12345
    message.from_user.first_name = "Иван"
    message.answer = AsyncMock()
    state = AsyncMock()

    await cmd_start(message, state)

    message.answer.assert_called_once()
    args, kwargs = message.answer.call_args
    assert "Иван" in args[0]
    assert kwargs.get("reply_markup") is not None
    state.clear.assert_awaited_once()