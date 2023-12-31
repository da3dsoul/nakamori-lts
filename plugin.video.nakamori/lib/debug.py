# -*- coding: utf-8 -*-
import cProfile
import pstats
import sys
from lib.utils.globalvars import *
from lib import error_handler as eh
from lib.error_handler import ErrorPriority
from lib.proxy.kodi import kodi_proxy

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


has_profiled = False
profile = cProfile.Profile()


def profile_this(func):
    """
    This can be used to profile any function.
    Usage:
    @profile_this
    def function_to_profile(arg, arg2):
        pass
    """

    def profiled_func(*args, **kwargs):
        """
        a small wrapper
        """
        try:
            start_profiling(func)
            result = func(*args, **kwargs)
            stop_profiling()
            return result
        finally:
            pass
    return profiled_func


def start_profiling(func):
    global has_profiled
    has_profiled = True
    profile.enable()


def stop_profiling():
    profile.disable()


def print_profiler():
    global has_profiled
    if not has_profiled:
        return

    has_profiled = False
    global profile
    stream = StringIO()
    sort_by = u'cumulative'
    ps = pstats.Stats(profile, stream=stream).sort_stats(sort_by)
    ps.print_stats(20)
    xbmc.log(u'Profiled Function: \n' + stream.getvalue(), xbmc.LOGWARNING)

    stream = StringIO()
    sort_by = u'time'
    ps = pstats.Stats(profile, stream=stream).sort_stats(sort_by)
    ps.print_stats(20)
    xbmc.log(u'Profiled Function: \n' + stream.getvalue(), xbmc.LOGWARNING)
    profile = cProfile.Profile()


def debug_init():
    """
    start debugger if it's enabled
    also dump argv if spamLog
    :return:
    """
    if plugin_addon.getSetting('remote_debug') == 'true':
        # try pycharm first
        try:
            # noinspection PyUnresolvedReferences
            import pydevd
            # try to connect multiple times...in case we forgot to start it
            # TODO Show a message to the user that we are waiting on the debugger
            connected = False
            tries = 0
            while not connected and tries < 60:
                try:
                    pydevd.settrace(host=plugin_addon.getSetting('remote_ip'), stdoutToServer=True, stderrToServer=True,
                                    port=5678, suspend=False)
                    eh.spam('Connected to debugger')
                    connected = True
                except:
                    tries += 1
                    # we keep this message the same, as kodi will merge them into Previous line repeats...
                    eh.spam('Failed to connect to debugger')
                    kodi_proxy.sleep(1000)
        except (ImportError, NameError):
            eh.log('unable to import pycharm debugger, falling back on the web-pdb')
            try:
                import web_pdb
                web_pdb.set_trace()
            except:
                eh.exception(ErrorPriority.NORMAL, 'Unable to start debugger, disabling it')
                plugin_addon.setSetting('remote_debug', 'false')
        except:
            eh.exception(ErrorPriority.HIGHEST, 'Unable to start debugger')

    eh.spam('argv:', sys.argv)
