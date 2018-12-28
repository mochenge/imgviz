<!-- DO NOT EDIT THIS FILE MANUALLY. This file is generated by generate_readme.py. -->

# imgviz: Image Visualization Tools

[![PyPI Version](https://img.shields.io/pypi/v/imgviz.svg)](https://pypi.python.org/pypi/imgviz)
[![Python Versions](https://img.shields.io/pypi/pyversions/imgviz.svg)](https://pypi.org/project/imgviz)
[![Build Status](https://travis-ci.com/wkentaro/imgviz.svg?token=zM5rExyvuRoJThsnqHAF&branch=master)](https://travis-ci.com/wkentaro/imgviz)

## Installation

```bash
pip install imgviz
```


## Dependencies

- [matplotlib](https://pypi.org/project/matplotlib)
- [numpy](https://pypi.org/project/numpy)
- [Pillow](https://pypi.org/project/Pillow)

## Getting Started

```python
# getting_started.py

import imgviz


# sample data of rgb, depth, class label and instance masks
data = imgviz.data.arc2017()
# colorize depth image with JET colormap
depthviz = imgviz.depth2rgb(data['depth'], min_value=0.3, max_value=1)
# colorize label image
labelviz = imgviz.label2rgb(data['class_label'], label_names=data['class_names'])
# tile visualization
tiled = imgviz.tile([data['rgb'], depthviz, labelviz], border=(255, 255, 255))
```

<img src=".readme/getting_started.jpg" width="50%" />

## [Examples](examples)

<table>
	<tr>
		<td align="center"><pre><a href="examples/centerize.py">examples/centerize.py</a></pre></td>
		<td align="center"><img src="examples/.readme/centerize.jpg" width="70%" /></td>
	</tr>
	<tr>
		<td align="center"><pre><a href="examples/depth2rgb.py">examples/depth2rgb.py</a></pre></td>
		<td align="center"><img src="examples/.readme/depth2rgb.jpg" width="70%" /></td>
	</tr>
	<tr>
		<td align="center"><pre><a href="examples/draw.py">examples/draw.py</a></pre></td>
		<td align="center"><img src="examples/.readme/draw.jpg" width="70%" /></td>
	</tr>
	<tr>
		<td align="center"><pre><a href="examples/label2rgb.py">examples/label2rgb.py</a></pre></td>
		<td align="center"><img src="examples/.readme/label2rgb.jpg" width="70%" /></td>
	</tr>
	<tr>
		<td align="center"><pre><a href="examples/resize.py">examples/resize.py</a></pre></td>
		<td align="center"><img src="examples/.readme/resize.jpg" width="70%" /></td>
	</tr>
	<tr>
		<td align="center"><pre><a href="examples/tile.py">examples/tile.py</a></pre></td>
		<td align="center"><img src="examples/.readme/tile.jpg" width="70%" /></td>
	</tr>
</table>
