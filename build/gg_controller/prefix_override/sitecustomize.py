import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nobel/Gujrat_Government_Hexapod/gg_hexapod_ws/install/gg_controller'
