from __future__ import annotations

import pytz
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
import voluptuous as vol
import re
import json
from typing import Any
from .const import (
    DOMAIN,
    DEFAULT_HOLIDAYS,
    CONF_HOLIDAYS,
    CONF_FORCE_WORKDAYS,
    CONF_CUSTOM_REST_DAYS,
    CONF_TIMEZONE,
    DEFAULT_FORCE_WORKDAYS
)

DATE_PATTERN = "^(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])$"

class HolAsstConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult:
        errors = {}
        
        if user_input is not None:
            try:
                if user_input[CONF_HOLIDAYS]:
                    holidays = json.loads(user_input[CONF_HOLIDAYS])
                    if not isinstance(holidays, dict):
                        errors[CONF_HOLIDAYS] = "invalid_json"
            except json.JSONDecodeError:
                errors[CONF_HOLIDAYS] = "invalid_json"
            
            if not errors:
                return self.async_create_entry(
                    title="Holiday Assistant",
                    data=user_input
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Optional(
                    CONF_HOLIDAYS, 
                    default=json.dumps(DEFAULT_HOLIDAYS, ensure_ascii=False)
                ): str,
                vol.Optional(
                    CONF_FORCE_WORKDAYS,
                    default=DEFAULT_FORCE_WORKDAYS
                ): str,
                vol.Optional(CONF_CUSTOM_REST_DAYS, default=""): str,
                vol.Required(CONF_TIMEZONE, default="Asia/Shanghai"): vol.In(
                    sorted(pytz.all_timezones)
                )
            }),
            errors=errors
        )