import logging
import datetime
from typing import  Dict
from .const import (
    LOGGER_NAME
)

_LOGGER = logging.getLogger(f"{LOGGER_NAME}_{__name__}")

async def get_today_info(holidays: Dict[str, str], conf_force_workdays: str, conf_custom_rest_days: str) -> Dict[str, any]:
    today = datetime.date.today()
    today_str = today.strftime("%Y-%m-%d")
    today_weekday = today.weekday()
    today_month_day = today_str[5:].replace('-', '')

    force_workdays = set(date.strip() for date in conf_force_workdays.split(',') if date.strip())
    custom_rest_days = set(date.strip() for date in conf_custom_rest_days.split(',') if date.strip())

    is_holiday = today_weekday in [5, 6] or today_str in holidays

    if today_month_day in force_workdays:
        is_holiday = False

    if today_month_day in custom_rest_days:
        is_holiday = True

    tag = holidays.get(today_str, today.strftime("%A"))

    return {
        "date": today_str,
        "is_holiday": is_holiday,
        "tag": tag
    }