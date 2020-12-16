import tempfile
import win32api
import win32print

filename = r'E:\12-15lj\开票模板.xls'
win32api.ShellExecute(
 0,
 "print",
 filename,
 '/d:"%s"' % win32print.GetDefaultPrinter(),
 ".",
 0
)