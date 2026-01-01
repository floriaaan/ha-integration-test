"""Config flow pour Mon Intégration."""
from typing import Any
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, CONF_API_KEY


class MonIntegrationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gère le config flow."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.FlowResult:
        """Gère l'étape user."""
        errors = {}
        
        if user_input is not None:
            # Validation de la clé API (optionnel: ajouter votre logique de validation ici)
            api_key = user_input.get(CONF_API_KEY, "").strip()
            
            if not api_key:
                errors[CONF_API_KEY] = "api_key_required"
            else:
                # Créer l'entrée de configuration
                return self.async_create_entry(
                    title="Mon Intégration",
                    data={CONF_API_KEY: api_key},
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_API_KEY): cv.string,
            }),
            errors=errors,
        )