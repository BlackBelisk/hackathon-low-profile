import intento
import conectandoDispositivo

devices = conectandoDispositivo.get_connected_devices()
dev0 = devices[0]
intento.start_scrcpy(dev0)
intento.launch_app("uy.com.hsbc.hsbcuruguay",dev0)
