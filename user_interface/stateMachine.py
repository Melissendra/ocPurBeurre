class AbstractStateMachine:
    """State class uses to create the user's menu path"""

    def __init__(self):
        """Initialization of a new state machine"""
        self._next_state = self.handle_start

    def start(self):
        """We start the new machine and begin by the first menu which is handle by the method handle_start """
        while self._next_state:
            self._next_state = self._next_state()

