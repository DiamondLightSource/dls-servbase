# Use standard logging in this module.
import logging

# Exceptions.
from dls_servbase_api.exceptions import NotFound

# Class managing list of things.
from dls_servbase_api.things import Things

logger = logging.getLogger(__name__)


# -----------------------------------------------------------------------------------------


class Datafaces(Things):
    """
    List of available dls_servbase_datafaces.
    """

    # ----------------------------------------------------------------------------------------
    def __init__(self, name=None):
        Things.__init__(self, name)

    # ----------------------------------------------------------------------------------------
    def build_object(self, specification):
        """"""

        dls_servbase_dataface_class = self.lookup_class(specification["type"])

        try:
            dls_servbase_dataface_object = dls_servbase_dataface_class(specification)
        except Exception as exception:
            raise RuntimeError(
                "unable to build dls_servbase_dataface object for type %s"
                % (dls_servbase_dataface_class)
            ) from exception

        return dls_servbase_dataface_object

    # ----------------------------------------------------------------------------------------
    def lookup_class(self, class_type):
        """"""

        if class_type == "dls_servbase_lib.datafaces.aiohttp":
            from dls_servbase_lib.datafaces.aiohttp import Aiohttp

            return Aiohttp

        elif class_type == "dls_servbase_lib.datafaces.aiosqlite":
            from dls_servbase_lib.datafaces.aiosqlite import Aiosqlite

            return Aiosqlite

        raise NotFound(
            "unable to get dls_servbase_dataface class for type %s" % (class_type)
        )
