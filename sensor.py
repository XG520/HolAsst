import logging
import json
from datetime import timedelta
from homeassistant.helpers.event import async_track_time_change, async_track_time_interval
from homeassistant.helpers.entity import Entity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .utils import get_today_info
from .const import (
    DOMAIN,
    CONF_USERNAME,
    CONF_HOLIDAYS,
    CONF_FORCE_WORKDAYS,
    CONF_CUSTOM_REST_DAYS,
    LOGGER_NAME,
)

_LOGGER = logging.getLogger(f"{LOGGER_NAME}_{__name__}")


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    holidays_str = entry.data.get(CONF_HOLIDAYS)
    force_workdays = entry.data.get(CONF_FORCE_WORKDAYS)
    rest_days = entry.data.get(CONF_CUSTOM_REST_DAYS)
    username = entry.data.get(CONF_USERNAME)

    try:
        holidays = json.loads(holidays_str)
        if not isinstance(holidays, dict):
            raise ValueError(f"Parsed holidays is not a dictionary: {holidays}")
    except (json.JSONDecodeError, ValueError) as e:
        _LOGGER.error(f"Failed to parse holidays: {e}")
        return False

    date_entity = DateEntity(username)
    is_holiday_entity = IsHolidayEntity(username)
    tag_entity = TagEntity(username)

    entities = [date_entity, is_holiday_entity, tag_entity]
    async_add_entities(entities)

    async def update_entities(time=None):
        _LOGGER.info("Updating holiday info...")
        data = await get_today_info(holidays, force_workdays, rest_days)
        if data:
            date_entity.update_state(data['date'])
            is_holiday_entity.update_state(data['is_holiday'])
            tag_entity.update_state(data['tag'])
            _LOGGER.info(f"Entities updated: {data}")
        else:
            _LOGGER.warning("No data returned from get_today_info.")

    # async_track_time_interval(hass, update_entities, timedelta(hours=2))
    async_track_time_change(hass, update_entities, hour=0, minute=0, second=0)
    
    await update_entities()

    return True


class BaseEntity(Entity):

    def __init__(self, username):
        self._username = username
        self._state = None

    @property
    def should_poll(self) -> bool:
        return False

    @property
    def device_info(self) -> dict:
        cat = (
            "　　　　　／＞　　フ\n"
            "　　 　 　　　 　 __\n"
            "　　　　　| 　_　 _l\n"
            "　　 　 　　　 　 __\n"
            "　 　　　／` ミ＿xノ\n"
            "　　 　 　　　 　 __\n"
            "　　 　 /　　　 　 |\n"
            "　　 　 　　　 　 __\n"
            "　　　 /　 ヽ　　 ﾉ\n"
            "　　 　 　　　 　 __\n"
            "　 　 │　|　|　|　| \n"
            "　　 　 　　　　 　 __\n"
            "　／￣|　 |　|　|　| \n"
            "　　　 　 　　　　 　 __\n"
            "　|　 (￣ヽ＿_ヽ_)__)\n"
            "　　 　 　　　 　 __\n"
            "　＼二つ"
            
        )
        return {
            "identifiers": {(DOMAIN, self._username)},
            "name": self._username,
            "manufacturer": "XG520",
            "model": cat,
        }

    @property
    def unique_id(self) -> str:
        raise NotImplementedError

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def state(self):
        return self._state

    def update_state(self, state):
        self._state = state
        self.async_write_ha_state()


class DateEntity(BaseEntity):

    def __init__(self, username):
        super().__init__(username)
        self._state = "Unknown"

    @property
    def unique_id(self) -> str:
        return f"date_{self._username}"
    
    @property
    def icon(self) -> str:
        return "mdi:calendar-account"

    @property
    def name(self) -> str:
        return "日期"


class IsHolidayEntity(BaseEntity):

    def __init__(self, username):
        super().__init__(username)
        self._state = "Unknown"

    @property
    def unique_id(self) -> str:
        return f"is_holiday_{self._username}"
    
    @property
    def icon(self) -> str:
        if self._state == "True":
            return "mmdi:coffee"
        else:
            return "mdi:briefcase"

    @property
    def name(self) -> str:
        return "今天是否为休息日"


class TagEntity(BaseEntity):

    def __init__(self, username):
        super().__init__(username)
        self._state = "Unknown"

    @property
    def unique_id(self) -> str:
        return f"tag_{self._username}"
    
    @property
    def icon(self) -> str:
        return "mdi:calendar-weekend"

    @property
    def name(self) -> str:
        return "Tag"
