# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta


class ShipmentOut(metaclass=PoolMeta):
    __name__ = 'stock.shipment.out'

    @classmethod
    def __setup__(cls):
        super().__setup__()

        customer_domain = ('customer', '=', True)
        if cls.customer.domain:
            cls.customer.domain += [customer_domain]
        else:
            cls.customer.domain = [customer_domain]
