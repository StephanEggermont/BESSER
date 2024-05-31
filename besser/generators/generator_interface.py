from abc import ABC, abstractmethod
from besser.BUML.metamodel.structural import Model
import os

# Interface for code generators
class GeneratorInterface(ABC):
    
    @abstractmethod
    def __init__(self, model: Model, output_dir: str = None):
        self.model = model
        self.output_dir = output_dir

    @abstractmethod
    def generate(self, *args):
        pass
    
    @property
    def model(self) -> Model:
        return self.__model
    
    @model.setter
    def model(self, model: Model):
        self.__model = model

    @property
    def output_dir(self) -> str:
        return self.__output_dir
    
    @output_dir.setter
    def output_dir(self, output_dir: str):
        self.__output_dir = output_dir

    def build_generation_path(self, file_name:str) -> str:
        if self.output_dir != None:
            if os.path.isdir(self.output_dir):
                file_path = os.path.join(self.output_dir, file_name)
            else:
                raise ValueError("The output_dir provided does not exist or is inaccessible")
        else:
            working_path = os.path.abspath('')
            os.makedirs(os.path.join(working_path, "output"), exist_ok=True)
            file_path = os.path.join(working_path, "output", file_name)
        return file_path