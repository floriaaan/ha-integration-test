"""Platform todo pour Mon Intégration."""
import aiohttp
import random
from datetime import datetime, timedelta
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
        self._items = []
        self._item_counter = 0
        self._api_url = "https://jsonplaceholder.typicode.com/todos"

    def _get_random_expiration(self) -> str:
        """Génère une date d'expiration aléatoire entre aujourd'hui et 7 jours."""
        random_days = random.randint(0, 7)
        expiration = datetime.now() + timedelta(days=random_days)
        return expiration.isoformat()

    async def async_added_to_hass(self) -> None:
        """Chargé dans Home Assistant, initialise les données."""
        await self._load_mock_data()

    async def _load_mock_data(self) -> None:
        """Charge les données depuis l'API externe."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self._api_url}?_limit=5") as resp:
                    if resp.status == 200:
                        todos = await resp.json()
                        for todo in todos:
                            self._items.append(
                                TodoItem(
                                    uid=str(todo["id"]),
                                    summary=todo["title"],
                                    status=TodoItemStatus.COMPLETED if todo["completed"] else TodoItemStatus.NEEDS_ACTION,
                                    due=self._get_random_expiration(),
                                )
                            )
                            self._item_counter = max(self._item_counter, todo["id"])
                        self.async_write_ha_state()
        except Exception:
            # En cas d'erreur, initialiser avec des tâches par défaut
            self._items = [
                TodoItem(
                    uid="1",
                    summary="Tâche exemple 1",
                    status=TodoItemStatus.NEEDS_ACTION,
                    due=self._get_random_expiration(),
                ),
                TodoItem(
                    uid="2",
                    summary="Tâche exemple 2",
                    status=TodoItemStatus.COMPLETED,
                    due=self._get_random_expiration(),
                ),
            ]
            self._item_counter = 2
            self.async_write_ha_state()

    @property
    def todo_items(self) -> list[TodoItem]:
        """Retourne la liste des items."""
        return self._items

    async def async_create_todo_item(self, item: TodoItem) -> None:
        """Ajoute un nouvel item."""
        self._item_counter += 1
        item.uid = str(self._item_counter)
        # Ajouter une date d'expiration aléatoire par défaut si pas présente
        if not item.due:
            item.due = self._get_random_expiration()
        self._items.append(item)
        self.async_write_ha_state()

    async def async_update_todo_item(self, item: TodoItem) -> None:
        """Met à jour un item existant."""
        for i, existing_item in enumerate(self._items):
            if existing_item.uid == item.uid:
                # Préserver la date d'expiration existante si pas de nouvelle
                if not item.due:
                    item.due = existing_item.due
                self._items[i] = item
                break
        self.async_write_ha_state()

    async def async_delete_todo_items(self, uids: list[str]) -> None:
        """Supprime des items."""
        original_count = len(self._items)
        self._items = [item for item in self._items if item.uid not in uids]
        if len(self._items) < original_count:
            self.async_write_ha_state()