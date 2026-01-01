"""Platform sensor pour Mon Intégration."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Configure les sensors."""
    async_add_entities([
        MonSensorTemperature(),
        MonSensorHumidite(),
    ])


class MonSensorTemperature(SensorEntity):
    """Sensor exemple pour température."""

    _attr_name = "Mon Sensor Température"
    _attr_unique_id = "mon_integration_temperature"
    _attr_native_unit_of_measurement = "°C"
    _attr_device_class = "temperature"

    def __init__(self):
        """Initialise le sensor."""
        self._attr_native_value = 20.5

    async def async_update(self):
        """Met à jour le sensor."""
        # Ici tu peux ajouter ta logique de mise à jour
        # Pour l'instant, on laisse une valeur statique
        pass


class MonSensorHumidite(SensorEntity):
    """Sensor exemple pour humidité."""

    _attr_name = "Mon Sensor Humidité"
    _attr_unique_id = "mon_integration_humidite"
    _attr_native_unit_of_measurement = "%"
    _attr_device_class = "humidity"

    def __init__(self):
        """Initialise le sensor."""
        self._attr_native_value = 65

    async def async_update(self):
        """Met à jour le sensor."""
        pass