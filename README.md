# nnview
**Visualization utilities for [PyTorch](https://pytorch.org).**
<img align='right' height='100' src='https://github.com/prasunroy/nnview/blob/master/assets/logo.jpg' />

![badge](https://github.com/prasunroy/nnview/blob/master/assets/badge_1.svg)
![badge](https://github.com/prasunroy/nnview/blob/master/assets/badge_2.svg)

## Installation
#### Option 1: Install using pip
```
pip install git+https://github.com/prasunroy/nnview.git
```
#### Option 2: Install from source
```
git clone https://github.com/prasunroy/nnview.git
cd nnview
python setup.py install
```

## LayerVisualizer
```python
CLASS nnview.visualization.LayerVisualizer
```
#### Example
```python
import torchvision
from PIL import Image

model = torchvision.models.vgg16(pretrained=True)
image = Image.open('assets/test.jpg').convert('RGB')

transforms = torchvision.transforms.Compose([
    torchvision.transforms.Resize((224, 224)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

x = transforms(image)
x = x.reshape((1,) + x.shape)
```
```python
from nnview.visualization import LayerVisualizer

visualizer = LayerVisualizer(model)
visualizer.parse_input(x)
visualizer.show()
visualizer.save(out_dir='output/')
```

<p align='center'>
  <b>Feature Maps of First Convolution Layer of VGG16</b>
  <br />
  <img src='https://github.com/prasunroy/nnview/raw/master/assets/layer_visualizer.jpg' />
  <br />
</p>

## Acknowledgements
Images from [Pixabay](https://pixabay.com) are used under [Creative Commons CC0 License](https://creativecommons.org/publicdomain/zero/1.0/deed.en).

## License
MIT License

Copyright (c) 2019 Prasun Roy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


<br />

**Made with** :heart: **and GitHub**
