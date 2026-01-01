"""Config flow pour Mon Intégration."""
from typing import Any
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant

from .const import DOMAIN


class MonIntegrationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gère le config flow."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.FlowResult:
        """Gère l'étape user."""
        if user_input is not None:
            return self.async_create_entry(
                title="Mon Intégration",
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )