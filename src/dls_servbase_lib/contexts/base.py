import logging

# Utilities.
from dls_utilpack.callsign import callsign

# Base class for a Thing which has a name and traits.
from dls_servbase_api.thing import Thing

logger = logging.getLogger(__name__)


class Base(Thing):
    """ """

    # ----------------------------------------------------------------------------------------
    def __init__(self, thing_type, specification=None, predefined_uuid=None):
        Thing.__init__(self, thing_type, specification, predefined_uuid=predefined_uuid)

        # Reference to object which is a server, such as BaseAiohttp.
        self.server = None

        self.context_specification = self.specification().get("context", {})

    # ----------------------------------------------------------------------------------------
    async def is_process_started(self):
        """"""

        if self.server is None:
            raise RuntimeError(f"{callsign(self)} a process has not been defined")

        return await self.server.is_process_started()

    # ----------------------------------------------------------------------------------------
    async def is_process_alive(self):
        """"""

        if self.server is None:
            raise RuntimeError(f"{callsign(self)} a process has not been defined")

        return await self.server.is_process_alive()

    # ----------------------------------------------------------------------------------------
    async def __aenter__(self):
        """ """

        await self.aenter()

    # ----------------------------------------------------------------------------------------
    async def __aexit__(self, type, value, traceback):
        """ """

        await self.aexit()
