from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from .const import (
    DOMAIN,
    CONF_HOLIDAYS,
    CONF_FORCE_WORKDAYS,
    CONF_CUSTOM_REST_DAYS,
    CONF_TIMEZONE
)

class HolidayDataManager:
    
    def __init__(self, hass: HomeAssistant):
        self.hass = hass
        self._config = {}
    
    async def async_setup(self, config_entry) -> None:
        self._config = dict(config_entry.data)
        
    def get_holidays(self) -> str:
        return self._config.get(CONF_HOLIDAYS, "")
        
    def get_force_workdays(self) -> str:
        return self._config.get(CONF_FORCE_WORKDAYS, "")
        
    def get_rest_days(self) -> str:
        return self._config.get(CONF_CUSTOM_REST_DAYS, "")
        
    def get_timezone(self) -> str:
        return self._config.get(CONF_TIMEZONE, "UTC")