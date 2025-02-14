from typing import Dict

DEFAULT_HOLIDAYS: Dict[str, str] = {
    "2025-01-01": "元旦",
    "2025-01-28": "春节",
    "2025-01-29": "春节",
    "2025-01-30": "春节",
    "2025-01-31": "春节",
    "2025-02-01": "春节",
    "2025-02-02": "春节",
    "2025-02-03": "春节",
    "2025-02-04": "春节",
    "2025-04-04": "清明节",
    "2025-04-05": "清明节",
    "2025-04-06": "清明节",
    "2025-05-01": "劳动节",
    "2025-05-02": "劳动节",
    "2025-05-03": "劳动节",
    "2025-05-04": "劳动节",
    "2025-05-05": "劳动节",
    "2025-05-31": "端午节",
    "2025-06-01": "端午节",
    "2025-06-02": "端午节",
    "2025-10-01": "国庆节",
    "2025-10-02": "国庆节",
    "2025-10-03": "国庆节",
    "2025-10-04": "国庆节",
    "2025-10-05": "国庆节",
    "2025-10-06": "中秋节",
    "2025-10-07": "国庆节",
    "2025-10-08": "国庆节"
}

DEFAULT_FORCE_WORKDAYS = "0126,0208,0427,0928,1011"

DOMAIN = "hol_asst"
LOGGER_NAME = f"{DOMAIN}_logger"

CONF_USERNAME = "username"
CONF_HOLIDAYS = "holidays"
CONF_FORCE_WORKDAYS = "force_workdays"
CONF_CUSTOM_REST_DAYS = "rest_days"
CONF_TIMEZONE = "timezone"

PLATFORMS = ["sensor"] 


SENSOR_NAME_TODAY = "日期"
SENSOR_NAME_HOLIDAY = "是否为休息日"

STATE_HOLIDAY = "休息日"
STATE_WORKDAY = "工作日"