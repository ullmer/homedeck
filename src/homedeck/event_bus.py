import asyncio
import inspect
from enum import Enum


class EventName(Enum):
    DECK_RELOAD = 'deck-reload'
    DECK_FORCE_RELOAD = 'deck-force-reload'


class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, callback):
        """Subscribe a function (sync or async) to an event."""
        if not callable(callback):
            raise TypeError('Callback must be a callable (function or coroutine function)')

        if event_name not in self.listeners:
            self.listeners[event_name] = []

        self.listeners[event_name].append(callback)

    def unsubscribe(self, event_name, callback):
        """Unsubscribe a function from an event."""
        if event_name in self.listeners:
            self.listeners[event_name].remove(callback)
            if not self.listeners[event_name]:  # Remove event if no more listeners
                del self.listeners[event_name]

    async def publish(self, event_name, *args, **kwargs):
        """Publish an event and notify all subscribers, handling both sync and async functions."""
        if event_name not in self.listeners:
            return

        tasks = []
        for callback in self.listeners[event_name]:
            if inspect.iscoroutinefunction(callback):  # Async function
                tasks.append(callback(*args, **kwargs))
            else:  # Sync function
                callback(*args, **kwargs)

        if tasks:
            await asyncio.gather(*tasks)  # Run async functions concurrently


# Example Usage
def sync_handler(data):
    print(f'Sync handler received: {data}')


async def async_handler(data):
    print(f'Async handler received: {data}')


event_bus = EventBus()
