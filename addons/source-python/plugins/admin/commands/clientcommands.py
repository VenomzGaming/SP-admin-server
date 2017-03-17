from .manager import command_manager
from .filters import Filter
from ..permissions import check_permission
from ..menus import *

## ============= CREATE OPERATORS ===================

import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

## ============ DECORATE COMMANDS ===================

# @command_manager.add_command('speed', 'b')
# def _change_speed(player, filters, operator, value):
#   op = operators[operator]
    
#   for target in Filter(filters, player):
#       target.speed = op(target.speed, float(value))

# @check_permission('B')
# @command_manager.add_command('health')
# def _change_health(player, filters, operator, value):
#   op = operators[operator]
    
#   for target in Filter(filters, player):
#       target.health = op(target.health, int(value))

# @check_permission('C')
# @command_manager.add_command('gravity')
# def _change_gravity(player, filters, operator, value):
#   op = operators[operator]
    
#   for target in Filter(filters, player):
#       target.gravity = op(target.gravity, float(value))

