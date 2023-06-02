import asyncio

# Use standard logging in this module.
import logging

from dls_utilpack.require import require

# Things created in the context.
from dls_servbase_api.guis.guis import dls_servbase_guis_get_default

# Base class for cli subcommands.
from dls_servbase_cli.subcommands.base import ArgKeywords, Base

# Servbase context creator.
from dls_servbase_lib.datafaces.context import Context as DlsServbaseDatafaceContext

# Servbase context creator.
from dls_servbase_lib.guis.context import Context as GuiContext

logger = logging.getLogger()


# --------------------------------------------------------------
class Service(Base):
    """
    Start single service and keep running until ^C or remotely requested shutdown.
    """

    def __init__(self, args, mainiac):
        super().__init__(args)

    # ----------------------------------------------------------------------------------------
    def run(self):
        """ """

        # Run in asyncio event loop.
        asyncio.run(self.__run_coro())

    # ----------------------------------------------------------
    async def __run_coro(self):
        """"""

        # Load the configuration.
        multiconf = self.get_multiconf(vars(self._args))
        configuration = await multiconf.load()

        # Get the specfication we want out of the configuration.
        specification = require(
            "configuration",
            configuration,
            "dls_servbase_dataface_specification",
        )

        # Context always starts as coro.
        if "context" not in specification:
            specification["context"] = {}

        specification["context"]["start_as"] = "coro"

        # Make the servbase service context from the specification in the configuration.
        servbase_context = DlsServbaseDatafaceContext(specification)

        # Open the servbase context which starts the service process.
        async with servbase_context:
            # Wait for the coro to finish.
            await servbase_context.server.wait_for_shutdown()

    # ----------------------------------------------------------
    def add_arguments(parser):

        parser.add_argument(
            "--configuration",
            "-c",
            help="Configuration file.",
            type=str,
            metavar="yaml filename",
            default=None,
            dest=ArgKeywords.CONFIGURATION,
        )

        return parser
