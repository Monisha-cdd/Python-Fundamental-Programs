# Program 6: Abstraction Example using ABC module
from abc import ABC, abstractmethod

class Features(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class WebApp(Features):
    def login(self):
        print("Login done")

    def logout(self):
        print("Logout done")

w = WebApp()
w.login()
w.logout()
