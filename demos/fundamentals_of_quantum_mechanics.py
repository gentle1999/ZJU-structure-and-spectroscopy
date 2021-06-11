import numpy as np
import sympy as sp
import pandas as pd
import streamlit as st


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
    if pages == '1.1 微观粒子运动特征':
        st.markdown("""## 1.1 微观粒子运动特征""")
        st.markdown("""
            ### 1.1.1 黑体辐射和能量量子化

        频率为$\\nu$的振动的平均能量为$$\\cfrac{h\\nu}{e^{\\cfrac{h\\nu}{kT}}-1}$$

        由此可得到单位时间、单位表面积上辐射的能量：$E_\\nu = \\cfrac{2\\pi h\\nu^3}{c^2}(e^{\\cfrac{h\\nu}{kT}}-1)^{-1}$
            """)

        with st.echo():
            temperature = st.number_input("输入一个自定义温度，单位为K", min_value=1, value=500)
            temperatures.append(temperature)

            def planck_function(v, T):
                return 10 ** 9 * 2 * np.pi * h * v ** 3 / (c_0 ** 2) * (pow(e, (h * v / (k * T))) - 1) ** -1

            e_ranges = []
            v_range = np.linspace(2e13, 4e14, 20)
            for t in temperatures:
                e_ranges.append(planck_function(v_range, t))
            E = pd.DataFrame(e_ranges)
            E.columns = v_range
            E.index = temperatures
            E = E.T
            st.line_chart(E, use_container_width=True)

        st.markdown("""
    ### 1.1.2 光电效应和光子学说

    >1. 光是一束光子流，每一种频率的光的能量都有一个最小单位，称为光子，光子的能量与光子的频率成正比，即：
    >$$E=h\\nu$$
    >2. 光子不但有能量，而且有质量，但光子的静止质量为零。光子的质量为：
    >$$m=\\cfrac{h\\nu}{c^2}$$
    >3. 光子具有一定的动量：
    >$$p=mc=\\cfrac{h\\nu}{c}=\\cfrac{h}{\\lambda}$$
    >4. 光的强度取决于单位体积内光子的数量，即光子密度。

    将频率为$\\nu$的光照射到金属上，当金属中的电子受到光子撞击时，产生光电效应，光子消失，并将它的能量$h\\nu$转移给电子，电子吸收的能量，一部分用于克服金属对它的束缚力，其余部分则变为光电子的动能：
    $$h\\nu=W+E_k=h\\nu_0+\\cfrac{1}{2}mv^2$$
            """)
        st.markdown("""
    ### 1.1.3 实物微粒的波粒二象性

    光的波粒二象性表明：光的波动性指光是电磁波，光的粒子性指光具有量子性。光在介质中以光速c传播时，它的二象性通过下列公式联系着：

    $$\\left\\{\\begin{array}{lcl}E=h\\nu \\\\ m=h\\nu/c^2 \\\\ p=h\\nu/c \\end{array}\\right.$$

    光的波性和粒性通过普朗克常数联系了起来。

    所以静止质量为m的实物微粒也具有波粒二象性：

    $$E=h\\nu=h\\cfrac{c}{\\lambda}=\\cfrac{p^2}{2m}=\\cfrac{1}{2}mc^2$$

    $$\\lambda = h/p = h/m\\nu$$

    1927年的单晶体电子衍射实验证明了经加速后电子具有波动性，验证了de Broglie的假设。
    """)

        st.markdown(
            """
    ### 1.1.4 不确定度关系

    $$\\Delta x\\Delta p_x\\ge h$$

    $$\\Delta E\\Delta t\\ge h/4\\pi$$

    比较微观粒子和宏观粒子的特性，可见：
    > 
    >1. 宏观物体同时具有确定的坐标和动量，其运动规律可以用经典物理学来描述；而微观粒子没有同时确定的坐标和动量，其运动规律需要用量子力学来描述。
    >
    >2. 宏观物体有连续、可测的运动轨道，可追踪各个物体的运动轨迹来加以分辨；微观粒子具有概率分布的特性，不可能辨别出各个粒子的轨迹。
    >
    >3. 宏观物体可处于任意的能量状态，体系的能量可以是任意的、连续变化的数值；微观粒子只能处于某种确定的能量状态，能量的该变量不能是任意的、连续变化的数值，只能是分立的，即量子化的。
    >
    >4. 不确定原理对宏观物体无实际意义，在不确定关系式中，普朗克常数可当作0；微观粒子遵循不确定关系，普朗克常数不能被看作0。

    """
        )

    if pages == '1.2 量子力学基本假设':
        st.markdown("""## 1.2 量子力学基本假设""")
        st.markdown("""
    ### 1.2.1 波函数和微观粒子的状态  
    - __假设一__   对于一个微观体系，它的状态和由该状态所决定的各种物理性质可用波函数$\\Psi(x,y,z,t)$表示。

    将波粒二象性关系$E=h\\nu,p=h/\\lambda$带入平面单色光的波动方程$\\Psi = A\\exp\\left[i2\\pi(x/\\lambda-vt)\\right]$，得到单电子一维运动的波函数：
    $$\\Psi=A exp\\left[\\cfrac{i2\\pi}{h}(xp_x-Et)\\right]$$
    若去除波函数中的时间项，则被称为定态波函数，用$\\psi$表示，后面基本都讨论定态波函数。

    $\\psi^*\\,\\psi(\\psi^2)$称为概率密度，$\\psi^*\\,\\psi d\\tau$为空间某点附近体积元中电子出现的概率。

    由于波函数描述的是概率波，因而必须满足下列三个条件：
    > 1. 波函数必须是单值的，即在空间每一点波函数只能有一个值。
    > 2. 波函数必须是连续的，即波函数的值不出现突跃；$\\psi$对x,y,z的一阶微商也是连续函数。
    > 3. 波函数必须是平方可积的，最好可归一化，即波函数在整个空间的积分$\\int\\psi^*\\psi d\\tau=1$。
    """)

        st.markdown("""
    ### 1.2.2 物理量和算符

    - __假设二__ 对每一个微观体系的每一个可观测的物理量，都对应着一个线性共轭算符。

    设物理量为$A$，相应的算符为$\\hat{A}$，若满足下一条件：

    $$\\hat{A}(\\psi_1+\\psi_2) = \\hat{A}\\psi_1+\\hat{A}\\psi_2$$

    则称$\\hat{A}$为线性算符，若$\\hat{A}$能满足：

    $$\\int \\psi_1^*\\hat{A}\\psi_1\\,d\\tau = \\int \\psi_1(\\hat{A}\\psi_1)^*\\,d\\tau$$

    或者

    $$\\int \\psi_1^*\\hat{A}\\psi_2\\,d\\tau = \\int \\psi_2(\\hat{A}\\psi_1)^*\\,d\\tau$$

    则称$\\hat{A}$为自轭算符，又称厄米算符。

    |                物理量                |                             算符                             |
    | :----------------------------------: | :----------------------------------------------------------: |
    |位置$$x$$               |                       $$\\hat{x} = x$$                        |
    |动量的x分量$$p_x$$       | $$\\hat{p_x}=-\\cfrac{ih}{2\\pi}\\cfrac{\\partial}{\\partial x}$$  |
    |角动量的z分量$$M_z=xp_y-yp_z$$ | $$\\hat{M_z}=-\\cfrac{ih}{2\\pi}\\left(x\\cfrac{\\partial}{\\partial y}-y\\cfrac{\\partial}{\\partial x}\\right)$$ |
    |动能$$T=p^2/2m$$        | $$\\hat{T}=-\\cfrac{h^2}{8\\pi^2 m}(\\cfrac{\\partial^2}{\\partial x^2}+\\cfrac{\\partial^2}{\\partial y^2}+\\cfrac{\\partial^2}{\\partial z^2}) = -\\cfrac{h^2}{8\\pi^2 m}\\triangledown^2$$ |
    |势能$$V$$            |                       $$\\hat{V} = V$$                        |
    |总能$$E=T+V$$          |  $$\\hat{H}=-\\cfrac{h^2}{8\\pi^2 m}\\triangledown^2+\\hat{V}$$   |

    最为关键的是$\\hat{p_x}$的推导：

    $$\\Psi=A exp\\left[\\cfrac{i2\\pi}{h}(xp_x-Et)\\right]$$

    对波函数以x求偏导：
    """)
        with st.echo():
            sp.init_printing(use_latex=True)
            A, h, x, p_x, E, t, pi, e = sp.symbols('A, h, x, p_x, E, t, pi, e')
            psi = A * e ** ((2 * pi * (0 + 1j) / h) * (x * p_x - E * t))
            st.write(sp.simplify(sp.diff(psi, x)))

        st.markdown("""
    $$\\therefore\\,\\cfrac{\\partial\\Psi}{\\partial x}=\\cfrac{i2\\pi}{h}p_x\\Psi$$

    $$p_x\\Psi=-\\cfrac{ih}{2\\pi}\\cfrac{\\partial\\Psi}{\\partial x}$$

    其余算符均可根据位置和动量算符推导
    """)

        st.markdown("""
    ### 1.2.3 本征态、本征值和$Schr\\ddot{o}dinger$方程

    - __假设三__ 若某一物理量$A$的算符$\\hat{A}$作用于某一状态函数$\\psi$等于某一常数$a$乘以$\\psi$，即：
    $$\\hat{A}\\psi=a\\psi$$
    那么对$\\psi$所描述的微观状态，物理量$A$具有确定的数值$a$。$a$称为物理量算符$\\hat{A}$的本征值，$\\psi$称为$\\hat{A}$的本征态或本征波函数。


    1. 自轭算符第一项重要性质：本征值一定为实数。

        一个保守体系的总能量E在经典物理学中用Hamilton函数$H$表示，即：

        $$H=T+V=\\cfrac{1}{2m}(p_x^2+p_y^2+p_z^2)+V$$

        把算符形式带入，就得到Hamilton算符$\\hat{H}$

        $$\\hat{H}=-\\cfrac{h^2}{8\\pi^2 m}(\\cfrac{\\partial^2}{\\partial x^2}+\\cfrac{\\partial^2}{\\partial y^2}+\\cfrac{\\partial^2}{\\partial z^2})+\\hat{V}=-\\cfrac{h^2}{8\\pi^2 m}\\triangledown^2+\\hat{V}$$

        对波函数使用$\\hat{H}$，得到：

        $$\\hat{H}\\psi=E\\psi$$

        $$\\left(-\\cfrac{h^2}{8\\pi^2 m}\\triangledown^2+\\hat{V}\\right)\\psi=E\\psi$$

        即$Schr\\ddot{o}dinger$方程。式中不含时间，因而本征态给出的概率密度不随时间改变，称为定态，这个本征态对应的本征值，就是这一状态的能量。

        含时$Schr\\ddot{o}dinger$方程为：

        $$\\hat{H}\\psi=\\cfrac{ih}{2\\pi}\\cfrac{\\partial}{\\partial t}\\psi$$

        $$or\\,\\,(-\\cfrac{h^2}{8\\pi^2 m}\\triangledown^2+\\hat{V})\\psi =\\cfrac{ih}{2\\pi}\\cfrac{\\partial}{\\partial t}\\psi$$

    2. 自轭算符第二项重要性质：

        - 归一性 即粒子在整个空间内出现的总概率为1：

        $$\\int \\psi_i^*\\psi_i\\,d\\tau=1$$

        - 正交性 即任意两状态的波函数相互正交，可作为正交基线性组合出其他波函数：

        $$\\int \\psi_i^*\\psi_jd\\tau=0$$

        这组关系可以归纳如下：

        $$\\int \\psi_i^*\\psi_j d\\tau=\\int \\psi_j^*\\psi_i d\\tau=\\delta_{ij}$$

        $$\\delta_{ij}=\\left\\{ \\begin{array}{rc} 0, & when & i\\neq j \\\\ 1, & when & i=j\\end{array}\\right.$$

    """)

        st.markdown("""
    ### 1.2.4 态叠加原理

    - __假设四__ 若$\\psi_1,\\psi_2,...,\\psi_n$为某一微观体系的可能状态，则由它们线性组合所得的$\\psi$也是该体系可能存在的状态。

        $$\\psi=c_1\\psi_1+c_2\\psi_2+\\cdots+c_n\\psi_n=\\sum_{i=1}^n\\ c_i\\psi_i$$

        - 本征态的物理量的平均值

        设与$\\psi_1,\\psi_2,...,\\psi_n$对应的本征值分别为$a_1,a_2,...,a_n$，当体系处于状态$\\psi$并且$\\psi$已归一化时，物理量$A$的平均值

        $$\\langle a\\rangle=\\int \\psi^*\\hat{A}\\psi d\\tau=\\int(\\sum_{i=1}^nc_i^*\\psi_i^*)\\hat{A}(\\sum_{i=1}^nc_i\\psi_i)d\\tau=\\sum_{i=1}^n\\left|c_i\\right|^2a_i$$

        而平均值体现的是宏观可测量的性质

        - 非本征态的物理量的平均值

        若状态函数$\\psi$不是物理量$A$的算符$\\hat{A}$的本征态，当体系处于这个状态时，$\\hat{A}\\psi\\neq a\\psi$，这时可用积分计算其平均值

        $$\\langle a\\rangle = \\int\\psi^*\\hat{A}\\psi\\,d\\tau$$

        由于对波函数而言，本征值为总能量，因而半径、势能等均可以像这样求得平均值。
    """)

        st.markdown("""
    ### 1.2.5 泡利原理

    - __假设五__ 在同一原子轨道或分子轨道上，最多只能容纳两个电子，这两个电子的自旋状态必须相反。或者说，两个自旋相同的电子不能占据同一轨道。

    对于微观粒子来说，相同的微粒是不可分辨的：

    > - 宏观粒子 一组粒子具有相同的质量和电量，但坐标和动量可以同时测定，因而可以区分开来。

    > - 微观粒子 一组电子或光子，由于不确定度关系，如果它们的质量、电量、自旋都相同，当任意两个坐标$q_1$和$q_2$相互交换，也无法观察到任何物理现象的变化。

    > $$\\psi^2(q_1,q_2)=\\psi^2(q_2,q_1)$$

    > $$\\therefore \\psi(q_1,q_2)=\\pm\\psi(q_2,q_1)$$

    对称的全同粒子波函数：

    $$\\psi(q_1,q_2)=+\\psi(q_2,q_1)$$

    适用于玻色子，自旋量子数为整数，运动遵循玻色-爱因斯坦统计规则。

    反对称的全同粒子波函数：

    $$\\psi(q_1,q_2)=-\\psi(q_2,q_1)$$

    适用于费米子，自旋量子数为半整数，运动遵循费米-狄拉克统计规则。

    处于三维空间同一坐标上，两个自旋相同的电子，其存在的概率密度为零：

    > - __泡利不相容原理__ 在一个多电子体系中，两个自旋相同的电子不能占据同一个轨道。也就是说，在同一原子中，两个电子的量子数不能完全相同。 

    > - __泡利排斥原理__ 在一个多电子体系中，自旋相同的电子尽可能分开、远离。
    """)

    if pages == '1.3 箱中粒子的Schrödinger方程及其解':
        st.markdown("""
    ## 1.3 箱中粒子的$Schr\\ddot{o}dinger$方程及其解

    ### 1.3.1 箱中粒子

    一维势箱的势能符合以下定义：

    $$V=\\left\\{\\begin{array}{lcl} 0, & {0<x<l} \\\\ \\infty , & x\\le0 \\cup x\\ge l\\end{array}\\right.$$

    所以粒子可以在$0<x<l$的范围内自由运动，在势箱内部，$Schr\\ddot{o}dinger$方程为：

    $$-\\cfrac{h^2}{8\\pi^2m}\\cfrac{d^2\\psi}{dx^2}=E\\psi$$

    如下求解得到：
    """)

        with st.echo():
            sp.init_printing(use_latex=True)
            h, x, m, E, pi = sp.symbols('h, x, m, E, pi')
            psi = sp.symbols('psi', cls=sp.Function)
            expr1 = sp.Eq(-h ** 2 / (8 * pi ** 2 * m) * psi(x).diff(x, x), E * psi(x))
            st.latex(sp.latex(sp.dsolve(expr1, psi(x))))

        st.markdown("""
    利用sympy解得的为复数形式，也可以根据常微分知识利用二阶齐次线性方程的公式得到如下：

    $$\\psi=c_1\\cos(\\cfrac{8\\pi^2mE}{h^2})^{\\cfrac{1}{2}}x+c_2\\sin(\\cfrac{8\\pi^2mE}{h^2})^{\\cfrac{1}{2}}x$$

    由一维势箱的定义，$x=0$或者$x=l$时，势能为无穷大，也就是说粒子不可能运动到这两个点，即$\\psi=0$。

    $$
    \\begin{cases}
    \\psi(0)=c_1\\cos(0)+c_2\\sin(0)=0 & \\therefore\\, c_1 = 0 \\\\
    \\psi(l)=c_1\\cos\\left[\\left(\\cfrac{8\\pi^2mE}{h^2}\\right)^{\\cfrac{1}{2}}l\\right]+c_2\\sin\\left[\\left(\\cfrac{8\\pi^2mE}{h^2}\\right)^{\\cfrac{1}{2}}l\\right]=0 & \\therefore\\, \\left(\\cfrac{8\\pi^2mE}{h^2}\\right)^{\\cfrac{1}{2}}l = n\\pi
    \\end{cases}
    $$

    显然，$n$的取值为正整数。

    所以得到波函数的能量为$E=\\cfrac{n^2h^2}{8ml^2}$

    将以上结论代回原波函数：

    $$\\psi(x)=c_2sin(\\cfrac{n\\pi x}{l})$$

    由于在$0<x<l$的范围中粒子出现的概率总和为1，因而有：

    $$\\int^l_0 \\left|\\psi\\right|^2\\,dx = 1$$
    """)
        with st.echo():
            sp.init_printing(use_latex=True)
            n, x, c_2, l, pi = sp.symbols('n, x, c_2, l, pi')
            psi = c_2 * sp.sin(n * pi * x / l)
            st.latex(sp.latex(sp.integrate(psi ** 2, (x, 0, l))))

        st.markdown("""
    因为$n$是正整数，所以积分结果即为$c_2^2\\cfrac{l}{2}=1,c_2=\\sqrt{\\cfrac{2}{l}}$

    综上，箱中粒子的波函数即为：

    $$\\psi_n(x)=\\sqrt{\\cfrac{2}{l}}\\sin(\\cfrac{n\\pi x}{l})$$

    能级为：

    $$E_n=\\cfrac{n^2h^2}{8ml^2}$$

    从一维势箱的计算中可以得到以下的一些结论：

    > - 粒子可以有多种运动状态，可以用$\\psi_1,\\psi_2,...,\\psi_n$来描述；
    > - 能量量子化；
    > - 存在零点能；
    > - 没有经典运动轨道，只有概率分布；
    > - 存在节点，节点越多，能量越高。

    以上都是微观粒子的量子效应，当$m,l,n$增大到宏观量时，量子效应消失，体系就变成了宏观体系，可用经典力学描述。

    下面是一维势箱中波函数及其概率密度分布的示意图

    """)
        with st.echo():
            n = st.number_input("输入能级", min_value=1, value=1, format="%d")

            def wave_function_of_one_dimension(n, x):
                return np.sqrt(2) * np.sin(n * np.pi * x)

            x_range = np.linspace(0, 1, 501)
            psi_range = wave_function_of_one_dimension(n, x_range)
            psi_2_range = wave_function_of_one_dimension(n, x_range) ** 2

            p1 = pd.DataFrame(psi_range)
            p2 = pd.DataFrame(psi_2_range)

            p1.index = x_range
            p2.index = x_range

            p1.columns = [n]
            p2.columns = [n]

            st.line_chart(p1, use_container_width=True)
            st.line_chart(p2, use_container_width=True)