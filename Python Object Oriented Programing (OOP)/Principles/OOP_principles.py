#encapsulation

    #public attributes - can be accessed from both inside and outside the class they are defined in; available for anyone

    #private attributes - only accessible within the class they are defined in (marked by two underscores at the beginnin of their name); hidden away

    #protected attributes - accessible within the class and subclass (marked by one underscore at the beginning of it's name); not immediately visible but can be found by those who know where to look

class Smartphone:
    def __init__(self, model, serial_num, OS):
        self.model = model #public
        self.__serial_num = serial_num #private
        self._OS = OS #protected

    def show_info(self):
        print(f'Model: {self.model}')
        print(f'Serial number: N/A')
        print(f"Operating System: {self._OS}")

    #getters act as 'read-only' window to private attributes
    def get_serial_number(self):
        return self.__serial_num
    
    #setters allow 'write' access to private attributes
    def set_serial(self, new_number):
        self.__serial_num = new_number

my_phone = Smartphone('IPhone 11', '1ASD5ASAD', 'iOS 12')

print(my_phone.model) #Output: IPhone 11
#print(my_phone.__serial_num) #Output: AttributeError: 'Smartphone' object has no attribute '__serial_num'
print(my_phone._OS) #Output: iOS 12

print(my_phone.get_serial_number())

my_phone.set_serial(123456)
print(my_phone.get_serial_number())


#Subclasses

class Smartphone:
    def __init__(self, model):
        self.model = model

    def make_call(self, number):
        print(f'Making a call to {number}')

    def send_message(self, number, message):
        print(f"Sending following to {number}: '{message}'")

class SmartCamera(Smartphone): #inherits from smartphone
    def __init__(self, model, camera_resolution):
        super().__init__(model) #call to the superclass constructor
        self.camera_resolution = camera_resolution

    def take_photo(self):
        print(f'Taking a picture with {self.camera_resolution} resolution')

    def make_call(self, number): #overriding the parent 'make_call' function
        print(f'Making a video call to {number} with {self.camera_resolution} resolution')

basic_phone = Smartphone('iPhone')
basic_phone.make_call('615-651-4354')
basic_phone.send_message('615-651-4354', 'Wassup brotha')

camera_phone = SmartCamera('iPhone X', '1080p')
camera_phone.make_call('615-651-4354')
camera_phone.take_photo()


#Polymorphism
    #ability of objects of different classes can respond to the same method call in a unique way


    #method overloading - when multiple methods have the same name but different parameters
class Smartphone:
    def download_app(self, app_name):
        print(f"Downloading {app_name} in a generic way")

class Android(Smartphone):
    def download_app(self, app_name):
        print(f'Downloading {app_name} from Play Store')

class iPhone(Smartphone):
    def download_app(self, app_name):
        print(f"Downloading {app_name} from App Store")


def download_app(phone, app_name):
    phone.download_app(app_name)


generic_phone = Smartphone()
android_phone = Android()
iphone = iPhone()

download_app(generic_phone, 'Instagram')
download_app(android_phone, 'Insta')
download_app(iphone, 'Insta')

