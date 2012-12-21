#my_debugger.py


from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
	def __init__(self):
		pass
		
	def load(self, path_to_exe):
		creation_flags = DEBUG_PROCESSS
		startupinfo = STARTUPINFO()
		processinfo = PROCESS_INFORMATION()
		startupinfo.dwFlags = 0x1
		startupinfo.wShowWindow = 0x0
		startupinfo.cb = sizeof(startupinfo)
		if kernel32.CreateProcessA(path_to_exe,
									None,
									None,
									None,
									None,
									creation_flags,
									None,
									None,
									byref(startupinfo),
									byref(processinfo)):
			print "PID:%d"%processinfo.dwProcessId
		else:
			print "Error 0x%08x"%kernel32.GetLastError()
