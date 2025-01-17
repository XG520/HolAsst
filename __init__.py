import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import (
    DOMAIN,
    LOGGER_NAME
)

_LOGGER = logging.getLogger(f"{LOGGER_NAME}_{__name__}")

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    try:
        await hass.config_entries.async_forward_entry_setup(entry, "sensor")
    except Exception as e:
        _LOGGER.error(f"设置传感器平台时出错 {entry.title}: {e}")
        return False
    return True
