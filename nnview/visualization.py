# -*- coding: utf-8 -*-
"""
Visualization utilities for PyTorch.
Created on Fri May 10 14:00:00 2019
Author: Prasun Roy | CVPRU-ISICAL (http://www.isical.ac.in/~cvpr)
GitHub: https://github.com/prasunroy/nnview

"""


import torch
import torchvision
import matplotlib.pyplot as plt
import os


class LayerVisualizer(object):
    
    def __init__(self, network):
        self._network = network
        self._modules = []
        self._fwhooks = []
        self._outputs = {}
        self._hookidx = 0
        self._find_modules(self._network)
        self._attach_hooks()
        self._transform = torchvision.transforms.ToPILImage()
    
    def _find_modules(self, module):
        if len(list(module.children())) > 0:
            for child in list(module.children()):
                self._find_modules(child)
        else:
            self._modules.append(module)
    
    def _attach_hooks(self):
        for module in self._modules:
            self._fwhooks.append(module.register_forward_hook(self._hook))
    
    def _hook(self, module, x, y):
        self._outputs[str(self._hookidx) + '_' + module.__class__.__name__] = y
        self._hookidx += 1
    
    def _unhook(self):
        for hook in self._fwhooks:
            hook.remove()
    
    def _make_grid(self, tensor):
        rank = len(tensor.shape)
        tensor = tensor[:1] if rank > 1 else tensor
        tensor = tensor.reshape((1,) * (4 - rank) + tensor.shape)
        tensor = tensor.permute(1, 0, 2, 3)
        grid = torchvision.utils.make_grid(tensor)
        rank = len(grid.shape)
        grid = grid.reshape(grid.shape + (1,) * (3 - rank))
        grid = grid.permute(0, 2, 1) if rank < 3 else grid
        return self._transform(grid)
    
    def parse_input(self, *args, **kwargs):
        self._outputs = {}
        self._hookidx = 0
        with torch.no_grad():
            self._network(*args, **kwargs)
    
    def show(self):
        for name, output in self._outputs.items():
            plt.figure()
            plt.axis('off')
            plt.title(name)
            plt.imshow(self._make_grid(output))
            plt.show()
    
    def save(self, out_dir):
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)
        for name, output in self._outputs.items():
            self._make_grid(output).save(f'{out_dir}/{name}.png')
