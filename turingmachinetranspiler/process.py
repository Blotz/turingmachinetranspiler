import logging
import time

from turingmachinelib.state import State, StateAction
from turingmachinelib.structs import MoveAction
from turingmachinelib.pointer import Pointer

logger = logging.getLogger(__name__)


def interpret(model) -> Pointer:
    table: list[State] = []
    table.append(State("INIT"))
    table.append(State("HALT"))
    for s in model.states:
        cur_state_id = s.state_id.name
        next_state_id = s.next_state.name

        cur_state: State = None
        next_state: State = None

        # Get the states
        for s_ in table:
            if cur_state is not None and next_state is not None:
                break

            if s_.get_ident() == cur_state_id:
                cur_state = s_

            if s_.get_ident() == next_state_id:
                next_state = s_

        # If we havent discovered this state already. add it to the table
        if cur_state is None:
            cur_state = State(cur_state_id)
            table.append(cur_state)

        if next_state is None:
            next_state = State(next_state_id)
            table.append(next_state)

        if s.value == "_":
            read_value = None
        else:
            read_value = s.value

        if s.write_value == "_":
            write_value = None
        else:
            write_value = s.write_value

        if s.move == "left":
            move_action = MoveAction.LEFT
        elif s.move == "right":
            move_action = MoveAction.RIGHT
        elif s.move == "print":
            move_action = MoveAction.PRINT
        elif s.move == "none":
            move_action = MoveAction.NONE
        else:
            raise Exception("")

        sa = StateAction(write_value, move_action, next_state)
        cur_state.set_action(read_value, sa)

    p = Pointer(table[0])
    return p


def run(tm_p: Pointer):
    try:
        while True:
            time.sleep(0)
            logging.debug(tm_p.get_state().get_ident())
            tm_p.print_tm()
            input()
            tm_p.compute()
    except Exception:
        pass
