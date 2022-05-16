#! /bin/python3

import dearpygui.dearpygui as dpg
import os
import threading


class Main:
    def start_server_app(self):
        os.system("python3 server_App.py")

    def start_client_app(self):
        os.system("python3 client_App.py")

    def main_window(self):
        dpg.create_context()

        with dpg.window(label="RemoteOS", width=500, height=450):
            dpg.add_text("RemoteOS", pos=(220, 30))
            server_app = threading.Thread(target=self.start_server_app) 
            client_app = threading.Thread(target=self.start_client_app) 
            dpg.add_button(label='server App', pos=(300, 70), height=60, width=100, callback=server_app.start)
            dpg.add_button(label='client App', pos=(100, 70), height=60, width=100, callback=client_app.start)

        dpg.create_viewport(title='RemoteOS', width=500, height=150)

    def run_main(self):
        self.main_window()
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

if __name__ == '__main__':
    Main().run_main()