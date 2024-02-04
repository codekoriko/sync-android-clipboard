import json
import logging
import socket
import sys
from pathlib import Path
from typing import Optional

from dotenv import find_dotenv, load_dotenv
from gist_storage.manage import GistManager

import logging

try:
    from sh import termux_clipboard_get, termux_clipboard_set
except ImportError:
    print('Unable to find termux_clipboard')
    print('Please install or update termux-api')
    print('$ pkg install termux-api')
    sys.exit(2)


class ShareClipboard(object):
    """
    This class is responsible for sharing clipboard content via a Gist.

    It uses the GistManager to push the current clipboard content to a
    specified Gist. This allows for sharing clipboard content across devices or
    networks. The content is encrypted for better privacy.

    Attributes:
        gist_manager (GistManager): An instance of GistManager to manage Gist
        operations.
    """

    def __init__(self, gist_hash: str, filename: str):
        """
        Initializes the ShareClipboard instance.

        Args:
            device_id (str): The ID of the device using this instance.
            gist_hash (str): The hash of the Gist where clipboard content will
            be stored.
            filename (str): The filename under which the clipboard
            content will be stored in the Gist.

        Note:
            It loads environment variables and initializes a GistManager
            instance.
        """
        load_dotenv(find_dotenv())
        self.gist_manager = GistManager(gist_hash, filename)

    def share(self):
        """
        Shares the current clipboard content by pushing it to the Gist.

        Retrieves the current clipboard content using termux_clipboard_get, and
        updates the Gist with this content. Logs the action, truncating the
        logged content for brevity.

        Note:
            If the clipboard content is empty, no action is taken.
        """
        max_content_log = 50
        clipboard_content = termux_clipboard_get() or ''
        if clipboard_content:
            self.gist_manager.push_content(clipboard_content)
            if len(clipboard_content) > max_content_log:
                jest = f'{clipboard_content[:max_content_log]}...'
            else:
                jest = clipboard_content
            logging.info(f'Updated clipboard content: {jest}')
