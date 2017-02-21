# Biaoge
## Introduction
Biaoge is a python tool to help researchers to record their data during their experiment. It is based on pandas but it's quite simplified. It can export data to markdown format which can be easily converted into other format.

## Usage
``` python
import Biaoge
bg = Biaoge.Biaoge()
bg.set("Table 1", "row1", "col1", 0.2)
result = self.bg.getMarkdown()
print result
```
