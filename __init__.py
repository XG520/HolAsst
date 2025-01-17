import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_component import async_remove_platforms
from .const import (
    DOMAIN,
    LOGGER_NAME,
    PLATFORMS
)

_LOGGER = logging.getLogger(f"{LOGGER_NAME}_{__name__}")

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    try:
        await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    except Exception as e:
        _LOGGER.error(f"设置传感器平台时出错 {entry.title}: {e}")
        return False
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    try:
        unload_ok = await async_remove_platforms(hass, entry, PLATFORMS)
        if unload_ok:
            # 清理集成的数据
            hass.data[DOMAIN].pop(entry.entry_id, None)
        return unload_ok
    except Exception as e:
        _LOGGER.error(f"卸载集成时出错 {entry.title}: {e}")
        return False