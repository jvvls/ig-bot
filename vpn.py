from pywinauto import Desktop, Application
import time

class VPN:
    def __init__(self):
        self.app_path = r'C:\Program Files\Privax\HMA VPN\Vpn.exe'
        self.app = None
        self.dialog = None
        self.panel0 = None
        self.connect_button = None
        self.change_ip_button = None
        self.start_app() # precisa de tratamento para app ligado + VPN desligado
        self.ensure_connected()

    def start_app(self):
        self.app = Application(backend="uia").start(self.app_path)
        self.dialog = Desktop(backend="uia").HMA
        self.panel0 = self.dialog.Pane
        self.connect_button = self.panel0.ConnectButton
        self.change_ip_button = self.panel0.Button5

    def get_vpn_state(self):
        return self.connect_button.get_toggle_state()

    def connect_disconnect_vpn(self):
        self.connect_button.click()

    def change_ip(self):
        self.change_ip_button.click()

    def ensure_connected(self):
        if self.get_vpn_state() == 0:  
            self.connect_disconnect_vpn()  
    
    def refresh_ip(self):
        self.connect_disconnect_vpn()
        time.sleep(3)
        self.connect_disconnect_vpn()

if __name__ == "__main__":
    vpn = VPN()
    print("Initial VPN state:", vpn.get_vpn_state())
    #vpn.change_ip()
    print("VPN state after changing IP:", vpn.get_vpn_state())
    vpn.refresh_ip()
    