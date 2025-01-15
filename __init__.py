"""Holiday Assistant integration."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .data_manager import HolidayDataManager
from .const import DOMAIN, PLATFORM
from .sensor import HolidaySensor
from typing import Callable

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Holiday Assistant from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    
    await hass.config_entries.async_forward_entry_setup(entry, PLATFORM)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(entry, PLATFORM)
    hass.data[DOMAIN].pop(entry.entry_id)
    return True

def create_holiday_sensor(callback: Callable) -> HolidaySensor:
    """创建假日传感器实例
    
    Args:
        callback: 回调函数,用于获取假日数据
        
    Returns:
        HolidaySensor实例
    """
    return HolidaySensor(callback)

__all__ = ["HolidaySensor", "create_holiday_sensor"]