import logging

from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from datetime import datetime

from roi.db import Investment
from roi.db import DatabaseRdbms
from roi.db import with_session

logger = logging.getLogger(__name__)


class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = "Base app"
        arguments = [
            (['-t', '--tag'],
                dict(action='store', help='tag of bought unit')),
            (['-c', '--cost'],
                dict(action='store', help='the cost/unit bought for')),
            (['-u', '--currency'],
                dict(action='store', help='the currency bought for')),
            (['-a', '--amount'],
                dict(action='store', help='the amount of units bought')),
            ]

    @expose(hide=True)
    @with_session
    def default(self, session=None):
        self.app.log.info('Listing all investments:')
        for inv in session.query(Investment).all():
            print(inv)

    @expose(help="register a buy order")
    @with_session
    def buy(self, session=None):
        inv = Investment()
        inv.timestamp = datetime.utcnow()
        inv.tag = self.app.pargs.tag
        inv.cost = self.app.pargs.cost
        inv.amount = self.app.pargs.amount
        inv.currency = self.app.pargs.currency
        session.add(inv)
        session.commit()
        self.app.log.info("buy order registered:")
        print(inv)

    @expose(help="register a sale order")
    def sell(self):
        self.app.log.info("Inside sell()")


class RoiApp(CementApp):
    class Meta:
        label = 'roi'
        base_controller = 'base'
        handlers = [BaseController]


def entry():
    DatabaseRdbms()
    with RoiApp() as app:
        app.run()


if __name__ == '__main__':
    entry()
