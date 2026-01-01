"""Platform todo pour Mon Intégration."""
from homeassistant.components.todo import TodoItem, TodoItemStatus, TodoListEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Configure les todo lists."""
    async_add_entities([MaTodoList()])


class MaTodoList(TodoListEntity):
    """Todo list exemple."""

    _attr_name = "Ma Liste de Tâches"
    _attr_unique_id = "mon_integration_todo_list"

    def __init__(self):
        """Initialise la todo list."""
        self._items = [
            TodoItem(
                uid="1",
                summary="Tâche exemple 1",
                status=TodoItemStatus.NEEDS_ACTION,
            ),
            TodoItem(
                uid="2",
                summary="Tâche exemple 2",
                status=TodoItemStatus.COMPLETED,
            ),
        ]

    @property
    def todo_items(self) -> list[TodoItem]:
        """Retourne la liste des items."""
        return self._items

    async def async_create_todo_item(self, item: TodoItem) -> None:
        """Ajoute un nouvel item."""
        item.uid = str(len(self._items) + 1)
        self._items.append(item)
        self.async_write_ha_state()

    async def async_update_todo_item(self, item: TodoItem) -> None:
        """Met à jour un item existant."""
        for i, existing_item in enumerate(self._items):
            if existing_item.uid == item.uid:
                self._items[i] = item
                break
        self.async_write_ha_state()

    async def async_delete_todo_items(self, uids: list[str]) -> None:
        """Supprime des items."""
        self._items = [item for item in self._items if item.uid not in uids]
        self.async_write_ha_state()