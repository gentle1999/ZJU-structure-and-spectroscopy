import numpy as np
import plotly.express as px
import pandas as pd
import sympy as sy
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st


def hybridization_and_HMO():
    """
            @author: Tang Miaojiong

            如有引用请注明原作者
    """

    pages = st.sidebar.radio('choose a page',
                             ('5.1 杂化轨道理论',
                              '5.2 休克尔分子轨道法（HMO）',
                              '自定义共轭体系的HMO法计算器'
                              ))
    if pages == '5.1 杂化轨道理论':
        st.markdown("""
            ## 5.1 杂化轨道理论
    """)
        st.markdown("""
        所谓“杂化”就是单中心原子轨道的线性组合，即在形成分子过程中，原子中能级相近的几个原子轨道可以相互混合，从而产生新的原子轨道。

$$\\phi_k=\\displaystyle\\sum_{i=1}^n\\left(K_i\\phi_i\\right)$$

新的原子轨道称为杂化轨道，这种过程称为“杂化”。在杂化过程中轨道数目不变。即有n个参加杂化的原子轨道，可以组合成n个新的杂化轨道。

按照量子力学中态的迭加原理，简并状态的任何线性组合，也一定是允许的状态。因此三个p轨道的线性组合，

$$\\displaystyle\\phi_p=C_1\\phi_{p_x}+C_2\\phi_{p_y}+C_3\\phi_{p_z}$$

得到的新的原子轨道仍然是p轨道，只是方向发生变化。对于能量不同的轨道，只要这些轨道的能量相差不大，它们之间可以杂化。
""")
        st.markdown("""
        杂化轨道必须是**正交归一性**的。

- 归一性

杂化轨道必须满足归一化条件，$\\displaystyle \\int\\phi_k^*\\phi_k\\,{\\rm d}\\tau=1$

- 正交性

杂化轨道也具有正交性，杂化轨道理论认为，一个杂化轨道的方向确定以后，其它杂化轨道的方向不是任意的，杂化轨道之间必须尽可能满足最小排斥原理，即杂化轨道应尽可能远离，这要求杂化轨道相互正交, $\\displaystyle\\int\\phi_k^*\\phi_l\\,{\\rm d}\\tau=0$

所以正交归一性可归纳为：$
        \\displaystyle \\int\\phi_k^*\\phi_l\\,{\\rm d}\\tau =
        \\begin{cases}
        1,  & K=l \\\\
        0, & K\\neq l
        \\end{cases}
$
""")
        st.markdown("""
        对应于每一个参加杂化的原子轨道，在所有新的杂化轨道中该轨道的成份之和必须为一个单位，即：

$$\\displaystyle\\sum_{k=1}^n C_{ki}^2=C_{1i}^2+C_{2i}^2+...+C_{ni}^2=1$$

若杂化中，$C_{1i}^2=C_{2i}^2=...=C_{ni}^2=\\frac{1}{n}$，称为等性杂化；$C_{ki}^2\\neq\\frac{1}{n}$，称为不等性杂化。
""")
        st.markdown("""
        原子轨道杂化以后可使成键能力增加因而使生成的分子更加稳定。Pauling将原子轨道$\\phi_i$在球极坐标中的最大值定义为原子轨道$\\phi_i$的成键能力$f$。

$$f_s=1,\\,f_p=\\sqrt{3}$$

s-p杂化轨道可以写成：$\\phi=a\\phi_s+b\\phi_p$

按归一化条件，$\\int|\\phi|^2\\,{\\rm d}\\tau=1$

$$
\\int{|a\\phi_s+b\\phi_p|}^2\\,{\\rm d}\\tau = \\int(a^2\\phi_s^2+b^2\\phi_p^2+2ab\\phi_s\\phi_p)\\,{\\rm d}\\tau=a^2\\int\\phi_s^2\\,{\\rm d}\\tau+b^2\\int\\phi_p^2\\,{\\rm d}\\tau=a^2+b^2=1
$$

令$\\alpha=a^2,\\,\\beta=b^2$

$$\\phi=\\sqrt{\\alpha}\\phi_s+\\sqrt{1-\\alpha}\\phi_p$$
""")
        with st.echo():
            alpha = np.linspace(0, 1, 200)
            phi = np.sqrt(alpha) + np.sqrt(1 - alpha) * np.sqrt(3)
            df = pd.DataFrame((alpha, phi)).T
            df.columns = ('α', 'φ')
            fig = px.line(df, x='α', y='φ')
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        可以看出，杂化后的成键能力比单纯的s或p轨道更强。
""")
        st.markdown("""
        ### 讨论杂化轨道之间的夹角

    设有两个杂化轨道，一个的s成份为$\\alpha_i$，另一个为$\\alpha_j$，则：

    $$\\phi_i=\\sqrt{\\alpha_i}\\phi_s+\\sqrt{1-\\alpha_i}\\phi_{pi};\\,\\,\\phi_{pi}=C_{1i}\\phi_{p_x}+C_{2i}\\phi_{p_y}+C_{3i}\\phi_{p_z}\\\\
    \\phi_j=\\sqrt{\\alpha_j}\\phi_s+\\sqrt{1-\\alpha_j}\\phi_{pj};\\,\\,\\phi_{pj}=C_{1j}\\phi_{p_x}+C_{2j}\\phi_{p_y}+C_{3j}\\phi_{p_z}$$

    由于两轨道正交：$\\int\\phi_i\\phi_j\\,{\\rm d}\\tau=0$

    $$\\int\\phi_i\\phi_j\\,{\\rm d}\\tau=\\int(\\sqrt{\\alpha_i}\\phi_s+\\sqrt{1-\\alpha_i}\\phi_{pi})(\\sqrt{\\alpha_j}\\phi_s+\\sqrt{1-\\alpha_j}\\phi_{pj})\\,{\\rm d}\\tau\\\\
    =\\int\\sqrt{\\alpha_i}\\sqrt{\\alpha_j}\\phi_s^2\\,{\\rm d}\\tau+\\int\\sqrt{\\alpha_i}\\sqrt{1-\\alpha_j}\\phi_s\\phi_{pj}\\,{\\rm d}\\tau+\\int\\sqrt{1-\\alpha_i}\\sqrt{\\alpha_j}\\phi_{pi}\\phi_s\\,{\\rm d}\\tau+\\int\\sqrt{1-\\alpha_i}\\sqrt{1-\\alpha_j}\\phi_{pi}\\phi_{pj}\\,{\\rm d}\\tau\\\\
    =\\sqrt{\\alpha_i\\alpha_j}+\\sqrt{(1-\\alpha_i)(1-\\alpha_j)}\\int\\phi_{pi}\\phi_{pj}\\,{\\rm d}\\tau$$

    由于是s-p杂化轨道，因而轨道间的夹角只与p轨道角度有关，假设$\\phi_{pi}$与$\\phi_{pj}$之间的夹角为$\\theta_{ij}$，则$\\phi_{pj}$沿$P_i$轴的分量将是$\\phi_{pj}cos\\theta_{ij}$。

    $$\\therefore \\int\\phi_{pi}\\phi_{pj}\\,{\\rm d}\\tau=\\cos\\theta_{ij}\\int\\phi_{pi}^2\\,{\\rm d}\\tau=\\cos\\theta_{ij}\\\\
    \\int\\phi_i\\phi_j\\,{\\rm d}\\tau=\\sqrt{\\alpha_i\\alpha_j}+\\sqrt{(1-\\alpha_i)(1-\\alpha_j)}\\cos\\theta_{ij}=0\\\\
    \\therefore \\cos\\theta_{ij}=-\\sqrt{\\cfrac{\\alpha_i\\alpha_j}{(1-\\alpha_i)(1-\\alpha_j)}}$$

    对于等性杂化，$\\alpha_i=\\alpha_j=\\alpha$：

    $$\\cos\\theta_{ij}=-\\cfrac{\\alpha}{1-\\alpha}$$
""")
        with st.echo():
            alpha = np.linspace(0, 0.5, 200)
            phi = np.arccos(-alpha / (1 - alpha)) / np.pi * 180
            df = pd.DataFrame((alpha, phi)).T
            df.columns = ('α', 'φ')
            fig = px.line(df, x='α', y='φ')
            st.plotly_chart(fig, use_container_width=True)
        st.markdown("""
        $\\alpha$成分为0时，即全部为p轨道，形状为墙角形，轨道间夹角为90°；$\\alpha$成分为0.5时，即sp杂化，轨道间夹角为180°。

""")
        st.markdown("""
        ### 杂化轨道及有关分子结构

#### $sp^3$等性杂化

一个s轨道与3个p轨道杂化，其杂化轨道数目应有4个，其形式可写为：

$$ \\phi_1=C_{11}\\phi_s+C_{12}\\phi_{p_x}+C_{13}\\phi_{p_y}+C_{14}\\phi_{p_z}\\\\
\\phi_2=C_{21}\\phi_s+C_{22}\\phi_{p_x}+C_{23}\\phi_{p_y}+C_{24}\\phi_{p_z}\\\\
\\phi_3=C_{31}\\phi_s+C_{32}\\phi_{p_x}+C_{33}\\phi_{p_y}+C_{34}\\phi_{p_z}\\\\
\\phi_4=C_{41}\\phi_s+C_{42}\\phi_{p_x}+C_{43}\\phi_{p_y}+C_{44}\\phi_{p_z}$$

由于单位轨道贡献：

$$C_{1i}^2+C_{2i}^2+C_{3i}^2+C_{4i}^2=1,\\,i=1,2,3,4$$

又因为等性杂化：

$$C_{1i}^2=C_{2i}^2=C_{3i}^2=C_{4i}^2=\\frac{1}{4},\\,i=1,2,3,4$$

$$C_{11}=C_{21}=C_{31}=C_{41}=\\frac{1}{2}$$

于是也满足轨道归一化条件。

再根据$sp^3$杂化的具体空间构型得到：

$$ 
\\phi_1=\\frac{1}{2}(\\phi_s+\\phi_{p_x}+\\phi_{p_y}+\\phi_{p_z})\\\\
\\phi_2=\\frac{1}{2}(\\phi_s-\\phi_{p_x}+\\phi_{p_y}-\\phi_{p_z})\\\\
\\phi_3=\\frac{1}{2}(\\phi_s+\\phi_{p_x}-\\phi_{p_y}-\\phi_{p_z})\\\\
\\phi_4=\\frac{1}{2}(\\phi_s-\\phi_{p_x}-\\phi_{p_y}+\\phi_{p_z})
$$

#### $dsp^2$等性杂化

$$ \\phi_1=C_{11}\\phi_s+C_{12}\\phi_{p_x}+C_{13}\\phi_{p_y}+C_{14}\\phi_{d_{x^2-y^2}}\\\\
\\phi_2=C_{21}\\phi_s+C_{22}\\phi_{p_x}+C_{23}\\phi_{p_y}+C_{24}\\phi_{d_{x^2-y^2}}\\\\
\\phi_3=C_{31}\\phi_s+C_{32}\\phi_{p_x}+C_{33}\\phi_{p_y}+C_{34}\\phi_{d_{x^2-y^2}}\\\\
\\phi_4=C_{41}\\phi_s+C_{42}\\phi_{p_x}+C_{43}\\phi_{p_y}+C_{44}\\phi_{d_{x^2-y^2}}$$

由于s轨道贡献相等：

$$C_{11}^2=C_{21}^2=C_{31}^2=C_{41}^2=\\frac{1}{4}\\\\
C_{11}=C_{21}=C_{31}=C_{41}=\\frac{1}{2}$$

$p_x$轨道只对$\\phi_1$和$\\phi_3$做贡献：

$$C_{12}^2=C_{32}^2=\\frac{1}{2}\\\\
C_{12}=\\frac{1}{\\sqrt{2}},\\,C_{32}=-\\frac{1}{\\sqrt{2}}$$

同理，

$$C_{23}=\\frac{1}{\\sqrt{2}},\\,C_{42}=-\\frac{1}{\\sqrt{2}}$$

$d_{x^2-y^2}$对4个杂化轨道贡献相同，

$$C_{14}=\\frac{1}{2},\\,C_{24}=-\\frac{1}{2},\\,C_{34}=\\frac{1}{2},\\,C_{44}=-\\frac{1}{2}$$

于是：

$$ \\phi_1=\\cfrac{1}{2}\\phi_s+\\frac{1}{\\sqrt{2}}\\phi_{p_x}+\\frac{1}{2}\\phi_{d_{x^2-y^2}}\\\\
\\phi_2=\\cfrac{1}{2}\\phi_s+\\frac{1}{\\sqrt{2}}\\phi_{p_y}-\\frac{1}{2}\\phi_{d_{x^2-y^2}}\\\\
\\phi_3=\\cfrac{1}{2}\\phi_s-\\frac{1}{\\sqrt{2}}\\phi_{p_x}+\\frac{1}{2}\\phi_{d_{x^2-y^2}}\\\\
\\phi_4=\\cfrac{1}{2}\\phi_s-\\frac{1}{\\sqrt{2}}\\phi_{p_y}-\\frac{1}{2}\\phi_{d_{x^2-y^2}}$$

""")
        st.markdown("""
#### 不等性杂化——以$H_2O$为例

实测H-O-H键角为104.5°。成键的杂化轨道可以表示为：

$$\\phi_{bond_1}=C_{11}\\phi_s+C_{12}\\phi_p\\\\
\\phi_{bond_2}=C_{21}\\phi_s+C_{22}\\phi_p$$

而$\\phi_p=m\\phi_{p_x}\\pm n\\phi_{p_y}=\\cos52.25^\\circ\\phi_{p_x}\\pm \\sin52.25^\\circ\\phi_{p_y}$

$$\\therefore \\phi_{bond_1}=C_{11}\\phi_s+C_{12}(0.6122\\phi_{p_x}+0.7909\\phi_{p_y})\\\\
\\phi_{bond_2}=C_{21}\\phi_s+C_{22}(0.6122\\phi_{p_x}-0.7909\\phi_{p_y})$$

又因为s和p轨道对这两个杂化轨道的贡献相同，

$$C_{11}=C_{21}=C_a;C_{12}=C_{22}=C_b$$

正交条件：

$$\\displaystyle\\int\\phi_{bond_1}\\phi_{bond_2}\\,{\\rm d}\\tau=C_a^2+C_b^2(0.6122^2-0.7909^2)=C_a^2-0.25C_b^2=0$$

归一条件：

$$\\displaystyle\\int|\\phi_{bond_1}|^2\\,{\\rm d}\\tau=C_a^2+C_b^2(0.6122^2+0.7909^2)=C_a^2+C_b^2=1$$

联立解方程得到：

$$
\\left\\{ 
\\begin{array}{c}
C_a^2=0.2 & C_a=0.4472\\\\ 
C_b^2=0.2 & C_b=0.8944
\\end{array}
\\right. 
$$

对于孤对电子的杂化轨道，也可以如下表示：

$$\\phi_{e_1}=C'_a\\phi_s+C'_b\\phi_p\\\\
\\phi_{e_2}=C'_a\\phi_s+C'_b\\phi_p$$

由于s轨道的单位贡献：

$$2C_a^2+2C'^2_a=1\\Rightarrow C'^2_a=0.3\\Rightarrow C_a^2=0.5477$$

$$\\cos\\theta=-\\cfrac{\\alpha}{1-\\alpha}=-\\cfrac{3}{7}\\rightarrow\\theta=115.4^\\circ$$

孤对电子与成键电子之间的夹角满足：

$$\\cos\\theta_{kp}=-\\cfrac{\\sqrt{\\alpha_k\\alpha_p}}{\\sqrt{(1-\\alpha_k)(1-\\alpha_p)}}$$

于是：

$$\\cos\\theta=-\\cfrac{\\sqrt{0.2\\times0.3}}{\\sqrt{(1-0.2)(1-0.3)}}\\rightarrow \\theta=109.1^\\circ$$

""")
        st.markdown("""
        #### 练习——以$NH_3$为例

事实上，如果已知一组广义上的等性轨道夹角，可以直接算出$\\alpha$，例如：

已知H-N-H的键角为107.3°。

$$\\cos\\theta=-\\cfrac{\\alpha}{1-\\alpha}\\rightarrow\\alpha=0.23$$

$$\\phi_{bond}=\\sqrt{0.23}\\phi_s+\\sqrt{0.77}\\phi_p$$

所以孤对电子的$\\alpha=1-0.23\\times3=0.31$

$$\\phi_{e}=\\sqrt{0.31}\\phi_s+\\sqrt{0.69}\\phi_p$$

孤对电子与成键电子之间的夹角为$\\arccos\\left(-\\cfrac{\\sqrt{0.23\\times0.31}}{\\sqrt{(1-0.23)(1-0.31)}}\\right)=111.5^\\circ$

""")
    if pages == '5.2 休克尔分子轨道法（HMO）':
        st.markdown("""
            ## 5.2 休克尔分子轨道法（HMO）
""")
        st.markdown("""
        ### 问题的提出与休克尔近似

丁二烯分子中不存在正常的单双键，键长有趋于平均化的迹象。
""")
        st.image("img/buta-1,3-diene.jpg")
        st.markdown("""
        丁二烯主要是1、4位的加成反应，这又说明丁二烯分子在旧键的破坏和新键的形成不是局限于两个原子之间进行，而和整个分子有关。

1930年休克尔(Hückel)用分子轨道理论（LCAO—MO）提出了一些近似处理方法，求解了大量有机共轭分子的结构，这些条件下处理分子的结构，称为休克尔分子轨道法，简称为HMO法。

HMO法的近似主要有以下几点：

 - **σ—π分离和分子骨架近似**

 由于在平面上的所有σ键与离域π键的对称性不同，考虑将分子中组成σ键的电子和组成离域π键的电子分开来考虑，σ—π分离近似，这样就把在分子平面上的所有σ键归为一类，称为σ分子骨架。

 - **库仑积分近似**

$$H_{ii}=\\displaystyle \\int\\psi_i^*\\hat{H}\\psi_i\\,{\\rm d}\\tau=\\alpha$$

 在分子势场中，第i个碳原子的$2P_z$电子的平均能量，不考虑C原子位置不同所产生的影响。

 - **交换积分近似**

$$H_{ij}=\\int\\psi_i^*\\hat{H}\\psi_j\\,{\\rm d}\\tau=
        H_{ij} =
        \\begin{cases}
        0,  & \\text{$(i\\neq j\\pm 1)$} \\\\
        \\beta, & \\text{$(i=j\\pm 1)$}
        \\end{cases}
$$
""")
        st.markdown("""
 属于相邻原子间的$2P_z$轨道的交换积分为β，不相邻原子间的$2P_z$轨道的交换积分为零。
 - **重迭积分近似**
 $$S_{ii}=\\int\\psi_i^*\\psi_i\\,{\\rm d}\\tau =
\\begin{cases}
        0,  & \\text{$(i\\neq j)$} \\\\
        1, & \\text{$(i=j)$}
        \\end{cases}
$$
""")
        st.markdown("""
忽略了原子间的重叠积分。

简单来说，HMO法忽略了所有不相邻原子之间的相互作用，仅考虑原子自身和相邻原子之间的相互作用，所以在久期方程中可以出现大量的0，使得矩阵变得稀疏，便于求解。

""")
        st.markdown("""
        优点：
>这种方法对共轭分子的离域π键能给出本质的描述;
>
>能较好地反映对成键起主要作用的β积分的贡献;
>
>求解方法简单;
>
>对于定性或半定量地讨论问题有一定的帮助。

缺点：
>用HMO法处理分子的结构是非常粗略的。
""")
        st.markdown("""
        ### 用HMO法处理丁二烯分子

#### 求分子轨道能级

用HMO法处理由4个垂直分子平面的$2P_z$轨道组成离域π键。分子轨道是原子轨道的线性组合，因此离域π键的分子轨道可以由4个$2P_z$轨道线性组合：

$$\\psi=C_1\\phi_1+C_1\\phi_2+C_3\\phi_3+C_4\\phi_4$$

应用线性变分法处理来确定组合系数，久期方程如下：

$$\\sum_{j=1}^4C_j(H_{ij}-ES_{ij})=0,\\,i=1,2,3,4$$

于是有：

$$C_1(H_{11}-ES_{11})+C_2(H_{12}-ES_{12})+C_3(H_{13}-ES_{13})+C_4(H_{14}-ES_{14})=0\\\\
C_1(H_{21}-ES_{21})+C_2(H_{22}-ES_{22})+C_3(H_{23}-ES_{23})+C_4(H_{24}-ES_{24})=0\\\\
C_1(H_{31}-ES_{31})+C_2(H_{32}-ES_{32})+C_3(H_{33}-ES_{33})+C_4(H_{34}-ES_{34})=0\\\\
C_1(H_{41}-ES_{41})+C_2(H_{42}-ES_{42})+C_3(H_{43}-ES_{43})+C_4(H_{44}-ES_{44})=0$$

应用HMO法的近似，可以得到线性方程组的系数矩阵，而若要得到$C_i$的非零解，其行列式应当等于0：

$$\\begin{vmatrix} \\alpha-E & \\beta & 0 & 0\\\\
            \\beta & \\alpha-E & \\beta & 0\\\\
            0 & \\beta & \\alpha-E & \\beta\\\\
            0 & 0 & \\beta & \\alpha-E\\\\ \\end{vmatrix}=0$$

为了简化计算，令$x=\\cfrac{\\alpha-E}{\\beta}$，则：

$$\\begin{vmatrix} 
x & 1 & 0 & 0\\\\
1 & x & 1 & 0\\\\
0 & 1 & x & 1\\\\
0 & 0 & 1 & x\\\\ \\end{vmatrix}=0$$
""")
        with st.echo():
            sy.init_printing(use_latex=True)
            x = sy.Symbol('x')
            M = sy.Matrix([
                [x, 1, 0, 0],
                [1, x, 1, 0],
                [0, 1, x, 1],
                [0, 0, 1, x]
            ])
            M.det()
            e = ["x = {:.3f}".format(i.evalf()) for i in sorted(sy.solve(M.det(), x))]
            st.latex(sy.latex(sy.solve(M.det(), x)))
            st.markdown("""
        解得x如上所示，由于$E=\\alpha-x\\beta$，得到：

$$E_1=\\alpha+1.618\\beta;\\\\
E_2=\\alpha+0.618\\beta;\\\\
E_3=\\alpha-0.618\\beta;\\\\
E_4=\\alpha-1.618\\beta;$$

因为$\\beta$是负值，能级排列次序如下：
""")
            st.image("img/丁二烯能级.png")
            st.markdown("""

所以丁二烯分子的离域π键总能量为：$E_\\pi=2E_1+2E_2=4\\alpha+4.472\\beta$。

对于丁二烯分子，按定域观点看，可有2个小π键。

$$\\begin{vmatrix} 
x & 1\\\\
1 & x\\\\
 \\end{vmatrix}=0$$

显然$x_1=-1,x_2=1\\rightarrow E_1=\\alpha+\\beta,E_2=\\alpha-\\beta$

所以离域能（Delocalization Energy）：

$$DE=4\\alpha+4.472\\beta-(4\\alpha+4\\beta)=0.472\\beta<0$$

能量相比孤立双键下降了。
""")
            st.markdown("""
        #### 求分子轨道表达式

将不同能级的能量代入已化简的久期方程：

$$C_1(\\alpha-E)+C_2(\\beta)+C_3(0)+C_4(0)=0\\\\
C_1(\\beta)+C_2(\\alpha-E)+C_3(\\beta)+C_4(0)=0\\\\
C_1(0)+C_2(\\beta)+C_3(\\alpha-E)+C_4(\\beta)=0\\\\
C_1(0)+C_2(0)+C_3(\\beta)+C_4(\\alpha-E)=0$$
""")
            with st.echo():
                def secular_diene(x):
                    return np.array([
                        [-x, 1, 0, 0],
                        [1, -x, 1, 0],
                        [0, 1, -x, 1],
                        [0, 0, 1, -x]
                    ])

                def Combination_coefficient(s):
                    return np.linalg.svd(s)[0].T[-1]

                Combination_coefficients = np.array([Combination_coefficient(secular_diene(float(e)))
                                                     for e in sorted([i.evalf()
                                                                      for i in sy.solve(M.det(), x)])])
                st.write(pd.DataFrame(Combination_coefficients))
        st.markdown("""
        计算结果表明，能量从高到低的分子轨道依次为：

$$\\psi_4=-0.372\\phi_1+0.602\\phi_2-0.602\\phi_3+0.372\\phi_4\\\\
\\psi_3=0.602\\phi_1-0.372\\phi_2-0.372\\phi_3+0.602\\phi_4\\\\
\\psi_2=-0.602\\phi_1-0.372\\phi_2+0.372\\phi_3+0.602\\phi_4\\\\
\\psi_1=0.372\\phi_1+0.602\\phi_2+0.602\\phi_3+0.372\\phi_4$$

其分子轨道可以用如下的图形来描述。
""")
        with st.echo():
            def draw_orbital(cs, e):
                fig = make_subplots(
                    rows=len(cs),
                    cols=1,
                    subplot_titles=e
                    # row_heights=1 / len(cs)
                )
                i = 1
                df = []
                for c in cs:
                    df.append([])
                    d = 0
                    for coeff in c:
                        df[i - 1].append([d, abs(coeff), abs(coeff), coeff / abs(coeff)])
                        df[i - 1].append([d, -abs(coeff), abs(coeff), -coeff / abs(coeff)])
                        d = 0.1 + d
                    df[i - 1] = pd.DataFrame(df[i - 1], columns=['x', 'y', 'radius', 'color'])
                    fig.add_trace(go.Scatter(x=list(df[i - 1]['x']), y=list(df[i - 1]['y']), mode='markers',
                                             marker=dict(
                                                 size=list(df[i - 1]['radius'] * 30),
                                                 color=list(df[i - 1]['color'])
                                             )), row=i, col=1)
                    i += 1
                return fig

            st.plotly_chart(draw_orbital(Combination_coefficients, e))
        st.markdown("""
        #### 分子图

- 电子密度

一个离域π轨道，$\\psi_i=C_1\\phi_1+C_2\\phi_2+...+C_m\\phi_m$。

$$\\int|\\psi_j|^2\\,{\\rm d}\\tau=\\int(C_1\\phi_1+C_2\\phi_2+...+C_m\\phi_m)^2\\,{\\rm d}\\tau=C_1^2+C_2^2+...+C_m^2=1$$

$C_i^2$是第i个碳原子上的几率，如果在这个分子轨道上有n个电子，那么n个电子在第i个碳原子上的几率为$n_1C_i^2(1)$。

同样在第二个分子轨道中，这第i个原子也参加组合，因此在第二个分子轨道中这个第i原子上的几率应为$n_2C_i^2(2)$。

在第i个原子上出现的总几率应是：

$$P_i=n_1C_i^2(1)+n_2C_i^2(2)+...+n_jC_i^2(j)=\\sum_k n_kC_i^2(K)$$

电子在第i个原子上出现的总几率也称为电荷密度。
""")
        st.markdown("""
        例如丁二烯的第一个碳原子上电荷密度为：
$$P_1 = 2\\times 0.372^2+2\\times 0.602^2=1$$

简单来说，可以理解为每个填充了电子的分子轨道对指定碳原子的电荷贡献。
""")
        with st.echo():
            ps = []
            for i in range(4):
                ps.append(2 * Combination_coefficients[3][i] ** 2 + 2 * Combination_coefficients[2][i] ** 2)
            st.write(pd.DataFrame(ps).T)
        st.markdown("""
可见丁二烯的电子密度是均等的。

- 键级（Bond order）

每个电子对相邻两个原子的键级贡献是个比较复杂的问题，定义相邻两原子之间的π键键级为：

$$P_{ij}=\\sum_k n_kC_i(k)C_j(k)$$

其中，$C_i(k)$是第k个分子轨道中第i个原子的系数，$n_k$是第k个分子轨道中电子数。

例如丁二烯的1号和2号原子之间的$\\pi$键键级为：

$$P_{12}=2\\times 0.372\\times 0.602+2\\times 0.602\\times 0.372=0.896$$

而2号和3号原子之间的$\\pi$键键级为：

$$P_{23}=2\\times 0.602\\times 0.602+2\\times -0.372\\times 0.372=0.448$$

简单来说，类似于求电荷密度，也是将所有填了电子的轨道对应于电子对的系数相乘之和。

""")
        with st.echo():
            bs = []
            for i in range(3):
                bs.append(2 * Combination_coefficients[3][i] * Combination_coefficients[3][i + 1] + 2 *
                          Combination_coefficients[2][i] * Combination_coefficients[2][i + 1])
            st.write(pd.DataFrame(bs).T)
        st.markdown("""
可见键级并不均等。        

- 自由价

自由价是某个原子可能剩余的键级，它说明了i个原子在某化合物中特定位置上用以键合其它基团的剩余成键能力。

$$F_i=F_{max}-\\sum_iP_{ij}=4.732-\\sum_iP_{ij}$$

一般定义碳原子周围的一个σ单键键级为1，计算碳原子周围所有的σ键键级再加上离域π键键级即得到某个碳原子的总键级。4.732是二亚甲基乙烯双基$C(CH_2)_3$中心碳原子周围总键级，一般认为这是碳原子周围总键级最高的数值。计算如下：

$$P_{\\text{总}}=3\\times 2\\times -0.707\\times -0.408 = 1.732$$

加上三个单键即为4.732
""")
        st.markdown("""
- 分子图

将π键键级，电荷密度和自由价分别标明在分子结构式上即得分子图，丁二烯分子图：
""")
        st.image("img/molecule.jpg")
        st.markdown("""
        ### HMO法对共轭环多烯的处理（单环）

例如苯分子，其久期行列式为（简化）：

$$\\begin{vmatrix} 
x & 1 & 0 & 0 & 0 & 1\\\\
1 & x & 1 & 0 & 0 & 0\\\\
0 & 1 & x & 1 & 0 & 0\\\\
0 & 0 & 1 & x & 1 & 0\\\\
0 & 0 & 0 & 1 & x & 1\\\\
1 & 0 & 0 & 0 & 1 & x
\\end{vmatrix}=0$$
""")
        st.image("img/benzene.jpg")
        st.markdown("""

能级计算如下：
""")
        with st.echo():
            M = sy.Matrix([
                [x, 1, 0, 0, 0, 1],
                [1, x, 1, 0, 0, 0],
                [0, 1, x, 1, 0, 0],
                [0, 0, 1, x, 1, 0],
                [0, 0, 0, 1, x, 1],
                [1, 0, 0, 0, 1, x]
            ])
            st.latex(sy.latex(sy.solve(M.det(), x)))
        st.markdown("""
$$\\therefore \\begin{cases}
        E_0=\\alpha+2\\beta \\\\
        E_j=\\alpha+2\\beta cos\\left(\\cfrac{2j\\pi}{n}\\right) & j=1,2,...,n-1
        \\end{cases}
$$

从这能级分式可知，环状共轭体系有如下性质：

1.n为偶数
> $n=4m+2$，除最低能级$E_0=\\alpha+2\\beta$，和最高能级$E_0=\\alpha-2\\beta$外，其余均为二重简并轨道（芳香性）。
>
> $n=4m$，有非键轨道（反芳香性）。

2.n为奇数
> 除最低能级$E_0=\\alpha+2\\beta$,，其余均为二重简并轨道。

""")
        st.image("img/环状共轭.png")
        with st.echo():
            def secular_diene_1(x):
                return np.array([
                    [-x, 1, 0, 0, 0, 1],
                    [1, -x, 1, 0, 0, 0],
                    [0, 1, -x, 1, 0, 0],
                    [0, 0, 1, -x, 1, 0],
                    [0, 0, 0, 1, -x, 1],
                    [1, 0, 0, 0, 1, -x]
                ])

            e = ["x = {:.3f}".format(i.evalf()) for i in sorted(sy.solve(M.det(), x))]
            Combination_coefficients_1 = np.array([Combination_coefficient(secular_diene_1(float(e)))
                                                   for e in sorted([i.evalf()
                                                                    for i in sy.solve(M.det(), x)])])
            st.write(pd.DataFrame(Combination_coefficients_1))
            st.plotly_chart(draw_orbital(Combination_coefficients_1, e))
        st.markdown("""
        ### 共轭效应

#### 电性

离域π键的形成增加物质的电导性能。如石墨、四氰代二甲基苯醌、四硫代富瓦烯等。

#### 颜色

离域π键的形成，若增大电子的活动范围，使体系能量降低，能级间隔变小，光谱由紫外区向可见区移动。

#### 化学反应性

用HMO法了解分子的物理性质和化学性能很有说服力。

### 形成离域π键的条件与类型

#### 形成条件

从上面丁二烯分子的讨论，可以得出形成离域π键的条件为：

> - 共轭原子必须在同一平面上，每个原子可提供一个轨道（p, d）并且相互平行。
>
> - 电子数目小于轨道数目的二倍。

#### 类型

离域π键可用符号$\\Pi_n^m$表示，其中n表示相互平行的轨道数目，m表示离域π键中电子的数目，根据n和m的大小关系，离域π键可分为三种类型。

> - 正常离域π键，m=n，即参加共轭的轨道数目与电子数相等。
>
> - 多电子离域π键，m﹥n，电子数大于轨道数（但小于2倍轨道数）,双键邻接带有孤对电子的O，N，P，Cl，S等原子时，常形成多电子离域大π键。
>
> - 缺电子离域π键，m﹤n，电子数小于轨道数。

### 超共轭效应

超共轭效应是指C-H等σ键轨道和相邻原子的π键轨道或其他轨道互相叠加，扩大电子的活动范围所产生的离域效应。例如在$H_3C-CH=CH_2$分子中，σ键电子与π键电子间相互作用产生的离域效应。这一效应使得单键键长缩短，键能增加；使双键键长略为增长。超共轭效应使的C原子带有正电性，这是由于碳原子的电负性依赖于它的杂化状态。当两个不同杂化形式的碳原子连接在一起时，将会出现键矩。超共轭效应也会改变分子的性质。例如，由于超共轭效应，甲苯和二甲苯的紫外吸收峰分别比苯向长波方向移8nm和16nm。

""")
    if pages == '自定义共轭体系的HMO法计算器':
        def energy(m):
            return [sy.re(i) for i in sy.solve(m.det(), x)]

        def secular(m, e):
            dt = np.dtype(np.float_)
            return np.array(m.subs(x, -e), dtype=dt)

        def combination_coefficient(s):
            return np.linalg.svd(s)[0].T[-1]

        def draw_orbital(cs, e):
            fig = make_subplots(
                rows=len(cs),
                cols=1,
                subplot_titles=e
                # row_heights=1 / len(cs)
            )
            i = 1
            df = []
            for c in cs:
                df.append([])
                d = 0
                for coeff in c:
                    df[i - 1].append([d, abs(coeff), abs(coeff), coeff / abs(coeff)])
                    df[i - 1].append([d, -abs(coeff), abs(coeff), -coeff / abs(coeff)])
                    d = 0.1 + d
                df[i - 1] = pd.DataFrame(df[i - 1], columns=['x', 'y', 'radius', 'color'])
                fig.add_trace(go.Scatter(x=list(df[i - 1]['x']), y=list(df[i - 1]['y']), mode='markers',
                                         marker=dict(
                                             size=list(df[i - 1]['radius'] * 30),
                                             color=list(df[i - 1]['color'])
                                         )), row=i, col=1)
                i += 1
            return fig

        st.markdown("""
本程序用于计算任意给定的久期行列式所对应的能级、轨道系数以及可视化，由实际共轭分子到久期行列式的转化由于技术问题没有做，也就是说我不保证合理的久期行列式是否存在对应的真实分子。

合理的久期行列式输入范例如下面所示，仅包括数字0,1，小写字母x和英文逗号，输入完成后按下“ctrl+enter”进行计算。        
""")
        matrix = st.text_area('输入符合格式的久期行列式', 'x,1,0\n1,x,1\n0,1,x')
        x = sy.Symbol('x')

        try:
            mat = matrix.split('\n')
            ans = []
            for i in mat:
                ans.append(eval(i))
            mat = ans
            mat = sy.Matrix(mat)
            initial_matrix = mat
            energies = sorted([e.evalf() for e in energy(initial_matrix)])
            combination_coefficients = np.array(
                [combination_coefficient(secular(initial_matrix, float(e))) for e in energies])
            E = ["x = {:.3f}".format(float(i)) for i in energies]
            st.markdown("久期行列式")
            st.dataframe(pd.DataFrame(ans))
            st.markdown("能级 x = $\\frac{\\alpha-E}{\\beta}$")
            st.dataframe(pd.DataFrame(energies))
            st.markdown("轨道系数")
            st.dataframe(pd.DataFrame(combination_coefficients))
            st.markdown("轨道可视化")
            st.plotly_chart(draw_orbital(combination_coefficients, E))
        except:
            st.markdown("""请输入正确格式的久期行列式""")
