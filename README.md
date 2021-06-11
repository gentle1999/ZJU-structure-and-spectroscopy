# ZJU-structure-and-spectroscopy
一个基于Streamlit的交互式笔记网站

* version 0.0.1
* author gentle

## 框架

```
framework
├── base.py
├── demos
│   ├── complexes.py
│   ├── fundamentals_of_quantum_mechanics.py
│   ├── hybridization_and_HMO.py
│   ├── __init__.py
│   ├── intro.py
│   ├── ion.py
│   ├── __pycache__
│   ├── structural_chemistry_of_covalent_bonds_and_diatomic_molecules.py
│   ├── symmetry_of_molecules.py
│   ├── the_structure_and_properties_of_atoms.py
│   └── wave_function_display.py
└── img
```

框架非常简单，分为三个部分，base.py，demos，img

其中base.py是程序的主体，用于承载其余脚本；demos模块中用于存放各个小章节的脚本程序；img目录中存放图片，后续可能改为media用于存放多媒体文件。

### base.py

```python
import inspect
import textwrap
from collections import OrderedDict

import streamlit as st
from streamlit.logger import get_logger
from demos import intro, fundamentals_of_quantum_mechanics, the_structure_and_properties_of_atoms, \
    wave_function_display, structural_chemistry_of_covalent_bonds_and_diatomic_molecules, symmetry_of_molecules, \
    hybridization_and_HMO, complexes, ion  
'''
	这里是demos模块中的具体脚本，每当添加一个新的脚本，都需要在这里导入，名字即为脚本的文件名
'''

LOGGER = get_logger(__name__)

# Dictionary of
# demo_name -> (demo_function, demo_description)
DEMOS = OrderedDict(
    [
        (
            "首页",
            (
                intro.intro,
                """
                """
            )
        ),
        (
            "第一章·量子力学基础知识",
            (
                fundamentals_of_quantum_mechanics.fundamentals_of_quantum_mechanics,
                """
                本节整理了第一章中的内容
                """
            )
        ),
        (
            "第二章·原子的结构与性质",
            (
                the_structure_and_properties_of_atoms.the_structure_and_properties_of_atoms,
                """
                本节整理了第二章中的内容
                """
            )
        ),
        (
            "氢原子三维波函数演示程序",
            (
                wave_function_display.wave_function_display,
                """
                """
            )
        ),
        (
            "第三章·共价键和双原子分子的结构化学",
            (
                structural_chemistry_of_covalent_bonds_and_diatomic_molecules.structural_chemistry_of_covalent_bonds_and_diatomic_molecules,
                """
                本节整理了第三章中的内容
                """
            )
        ),
        (
            "第四章·分子的对称性",
            (
                symmetry_of_molecules.symmetry_of_molecules,
                """
                本节整理了第四章中的内容
                """
            )
        ),
        (
            "第五章·杂化轨道理论和HMO法",
            (
                hybridization_and_HMO.hybridization_and_HMO,
                """
                本节整理了第五章中的杂化轨道和HMO相关的内容
                """
            )
        ),
        (
            "第六章·配位化合物的结构和性质",
            (
                complexes.complexes,
                """
                本节整理了第六章中的内容
                """
            )
        ),
        (
            "离子化合物 ",
            (
                ion.ion,
                """
                本节整理了离子化合物相关的内容
                """
            )
        )
    ]
)
'''
	这个对象中存放了脚本中的具体函数，引用时以<脚本名>.<函数名>的形式引用，其余格式可参照上例
'''


def run():
    demo_name = st.sidebar.selectbox("Choose a chapter", list(DEMOS.keys()), 0)
    demo = DEMOS[demo_name][0]

    if demo_name == "首页":
        show_code = False
        st.write("# 结构与谱学交互式笔记"
                 " 👋")
    else:
        show_code = st.sidebar.checkbox("Show code", False)
        st.markdown("# %s" % demo_name)
        description = DEMOS[demo_name][1]
        if description:
            st.write(description)
        # Clear everything from the intro page.
        # We only have 4 elements in the page so this is intentional overkill.
        for i in range(10):
            st.empty()

    demo()

    if show_code:
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))


if __name__ == "__main__":
    run()
```

每一次添加新的脚本，都需要修改这一base.py文件

### demos

```python
import numpy as np
import sympy as sp
import pandas as pd
import streamlit as st
'''
	导入的模块在此定义
'''

def fundamentals_of_quantum_mechanics():
    """
        @author: Tang Miaojiong

        如有引用请注明原作者
    """
    # const numbers
    h = 6.626070e-34
    c_0 = 299792458
    e = 2.718282
    k = 1.3806488e-23

    temperatures = [1000, 1500]

    pages = st.sidebar.radio('choose a page', ('1.1 微观粒子运动特征', '1.2 量子力学基本假设', '1.3 箱中粒子的Schrödinger方程及其解'))
    '''
    	这里定义了子目录，凡是拥有子目录的脚本都需要创建这个
    '''
    if pages == '1.1 微观粒子运动特征':
        pass

    if pages == '1.2 量子力学基本假设':
        pass

    if pages == '1.3 箱中粒子的Schrödinger方程及其解':
        pass
    '''
    	如上的语句表示选中子目录中的某一页时显示对应的内容
    '''
```

* 注意：**凡是在脚本中使用图片的，都要求统一使用**

```python
st.image('img/<name>')
```

使用markdown原生的img虽然也可以显示图片，但性能很差，且无法使用css控制格式，因为streamlit默认是禁用html的，自然，使用\<img>标签定义的图片完全无法显示。

希望在脚本中引入各种互动功能的，可以参照我之前的代码，并结合官方文档https://docs.streamlit.io/en/0.81.1/api.html进行开发

### img

这里用于存放图片资源，因为随着时间推移文件数量可能大大增长，建议在一开始就将图片命名为

作者-日期-序号

### 开发平台

基于code-server搭建，可以简单的理解为一个运行在浏览器里的vscode，也支持一个ipad上的app：*Servediter*进行连接。

因为streamlit支持脚本热更新，所以修改代码不需要先关闭服务再启动的过程，我们只需要直接修改代码即可。

如果脚本涉及一些第三方库，可以在下方的终端中安装（终端可能会被关闭，如果没找到点击左上角三条杠-terminal-new terminal即可打开），按照下方步骤进行

```shell
conda activate ss # 激活虚拟环境, ss为环境名
pip install <module>
# or
conda install <module>
```

#### 管理员

正式部署时有一位管理员进行控制，因为服务器的密码暴露很危险，建议选择班级内一位比较了解Linux操作系统的同学担任。管理员主要负责掌握root权限，用于安装第三方软件，以及平时的维护，必须保护密码不被传播。每一届班级更新一次管理员和密码。
