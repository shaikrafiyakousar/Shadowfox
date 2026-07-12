"""
ShadowFox Python Development Internship
Task 1 - Topic: Inheritance
Author: Shaik Rafiya Kousar
"""

# ---------------------------------------------------------
# Base class: MobilePhone
# ---------------------------------------------------------
class MobilePhone:
    def __init__(self, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = "Touch Screen"
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, number):
        print(f"Incoming call from {number}...")

    def take_a_picture(self):
        print(f"Picture taken using {self.rear_camera} rear camera.")

    def show_specs(self):
        print(f"  Screen Type: {self.screen_type}")
        print(f"  Network Type: {self.network_type}")
        print(f"  Dual Sim: {self.dual_sim}")
        print(f"  Front Camera: {self.front_camera}")
        print(f"  Rear Camera: {self.rear_camera}")
        print(f"  RAM: {self.ram}")
        print(f"  Storage: {self.storage}")


# ---------------------------------------------------------
# Child class: Apple
# ---------------------------------------------------------
class Apple(MobilePhone):
    def __init__(self, model_name, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model_name = model_name
        self.brand = "Apple"

    def face_id_unlock(self):
        print(f"{self.model_name}: Unlocked using Face ID.")


# ---------------------------------------------------------
# Child class: Samsung
# ---------------------------------------------------------
class Samsung(MobilePhone):
    def __init__(self, model_name, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model_name = model_name
        self.brand = "Samsung"

    def fingerprint_unlock(self):
        print(f"{self.model_name}: Unlocked using fingerprint sensor.")


if __name__ == "__main__":
    # Create Apple phone objects
    iphone_14 = Apple("iPhone 14", "5G", True, "12MP", "48MP", "6GB", "128GB")
    iphone_11 = Apple("iPhone 11", "4G", False, "12MP", "12MP", "4GB", "64GB")

    # Create Samsung phone objects
    galaxy_s22 = Samsung("Galaxy S22", "5G", True, "10MP", "50MP", "8GB", "256GB")
    galaxy_m32 = Samsung("Galaxy M32", "4G", True, "20MP", "64MP", "4GB", "64GB")

    for phone in [iphone_14, iphone_11, galaxy_s22, galaxy_m32]:
        print(f"\n{phone.brand} - {phone.model_name}")
        phone.show_specs()
        phone.make_call("+91 9123456780")
        phone.take_a_picture()

    iphone_14.face_id_unlock()
    galaxy_s22.fingerprint_unlock()
