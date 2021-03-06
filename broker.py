"""
trading-server is a multi-asset, multi-strategy, event-driven execution
and backtesting platform (OEMS) for trading common markets.

Copyright (C) 2020  Sam Breznikar <sam@sdbgroup.io>

Licensed under GNU General Public License 3.0 or later.

Some rights reserved. See LICENSE.md, AUTHORS.md.
"""


class Broker:
    """
    Broker consumes Order events, executes orders, then creates and places
    Fill events in the event queue post-transaction.
    """

    def __init__(self, exchanges, logger):
        self.exchanges = exchanges
        self.logger = logger
        self.live_trading = False
