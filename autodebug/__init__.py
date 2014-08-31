from __future__ import print_function
import sys
import os


def get_post_mortem(debug_name):
    try:
        if debug_name == "pdb":
            from pdb import post_mortem
        elif debug_name == "ipdb":
            from ipdb import post_mortem
        elif debug_name == "pudb":
            from pudb import post_mortem
        else:
            print("Debugger {} not implemented\n Using pdb instead".format(
                debug_name))
            from pdb import post_mortem

    except ImportError:
        print(
            "You haven't got {} installed. Change AUTO_DEBUG variable.\n"
            "Going to use pdb".format(debug_name)
        )
        from pdb import post_mortem

    return post_mortem


def start_debugger(ex_cls, ex, tb):
    if hasattr(sys, 'ps1') or not sys.stderr.isatty():
        sys.__excepthook__(ex_cls, ex, tb)
        return

    print("There was an error:", ex)

    debug_tool = os.environ.get("AUTO_DEBUG", "pdb")
    pm = get_post_mortem(debug_tool)
    pm(tb)

sys.excepthook = start_debugger
