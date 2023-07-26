class ModelStore(object):
    def __init__(self, models, scenes, flashes, cameras, chnage_observers):
        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras
        self.chnage_observers = chnage_observers

    def get_scena(self):
        return

    def get_notify_change(self):
        return


class Poligon(ModelStore):
    def __init__(self, points):
        self.points = points


class PoligonalModel(Poligon):
    def __init__(self, poligons, textures):
        self.poligons = poligons
        self.textures = textures


class Flash(ModelStore):
    def __init__(self, location, angle, color, power):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self):
        return

    def move(self):
        return


class Camera(ModelStore):
    def __init__(self, location, angel):
        self.location = location
        self.angel = angel

    def rotate(self):
        return

    def move(self):
        return


class Scene(ModelStore):
    def __init__(self, id, models, flashes):
        self.id = id
        self.models = models
        self.flashes = flashes

    def method1(type):
        return type

    def method2(type):
        return type
