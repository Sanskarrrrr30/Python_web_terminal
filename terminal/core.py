import os
import sys
import io
import contextlib
from terminal import commands, system_utils

class Terminal:
    def __init__(self):
        self.cwd = os.getcwd()

    def execute(self, user_input):
        if not user_input.strip():
            return ""
        parts = user_input.strip().split()
        cmd, args = parts[0], parts[1:]

        # Capture output
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            if cmd in commands.command_map:
                commands.command_map[cmd](self, *args)
            elif cmd in system_utils.system_command_map:
                system_utils.system_command_map[cmd](*args)
            elif cmd == "exit":
                return "Exiting terminal..."
            else:
                print(f"Unknown command: {cmd}")

        return buffer.getvalue().strip()
