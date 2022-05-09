from re import S
import torch
from abc import ABC, abstractmethod
from typing import Protocol

# class MyDataset(ABC, torch.utils.data.Dataset):
#     """ABC of custom Dataset
#     """
#     @abstractmethod
#     def __init__(
#         self,
#         root: str,
#         train: bool = True, 
#         download: bool = False,
#     ):
#         pass
    
#     @abstractmethod
#     def __len__(self):
#         ...
        
#     @abstractmethod
#     def __getitem__(self, index):
#         ...

class MyMappingDataset(Protocol):
    def __init__(
        self,
        root: str,
        train: bool = True,
        download: bool = False,
    ):
        ...
        
    def __len__(self):
        ...
        
    def __getitem__(self, index):
        ...