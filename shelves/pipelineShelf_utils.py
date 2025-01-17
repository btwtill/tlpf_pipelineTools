
SHELF_NAME = "tlpf_shelf"

# Logging module is used to print output to user
import logging

LOG = logging.getLogger(__name__)


# Import python modules used in this script
import os
import sys
import subprocess
import importlib


# Inherit shelf base class module whose functions we "override" to build our tlpf_toolkit shelf
from tlpf_pipelineTools.shelves import shelf_base

importlib.reload(shelf_base)

# Import maya modules
import maya.cmds as cmds


# GLOBAL script variables referred to throughout this script
ICON_DIR = os.path.join(os.path.dirname(__file__), "pipelineTools_icons")
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "shelf_user_utils_scripts")
PLATFORM = sys.platform


sys.path.append(SCRIPTS_DIR)


def reload_shelf(shelf_name=SHELF_NAME):
    """Reloads shelf"""
    try:
        from tlpf_pipelineTools.shelves import shelf_base

        importlib.reload(shelf_base)

        from tlpf_pipelineTools.shelves import riggingShelf_utils

        importlib.reload(riggingShelf_utils)

        riggingShelf_utils.load(name=SHELF_NAME)

        LOG.info("Successfully reloaded {} shelf".format(SHELF_NAME))
        return True
    except:
        LOG.error("Error reloading shelf")
        return


from tlpf_pipelineTools.UITemplates import maya_UI_Template
importlib.reload(maya_UI_Template)

class loadPiplineShelf(shelf_base._shelf):
    def build(self):
    
        #Test UI
        self.addButton(label="testUI", icon=ICON_DIR + "/testUi.png", command=maya_UI_Template.openWindow)
        
        # Separator
        self.addButton(label="", icon=ICON_DIR + "/sep.png", command="")