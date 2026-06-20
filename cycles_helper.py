import bpy

def get_devices():
    prefs = bpy.context.preferences
    # Refresh Device List
    prefs.addons['cycles'].preferences.get_devices()
    cycles_prefs = prefs.addons['cycles'].preferences
    return cycles_prefs.devices

def setup_devices(use_cpu,use_cuda):
    devices = get_devices()
    for device in devices:
        print(device)

