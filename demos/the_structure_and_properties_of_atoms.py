import streamlit as st


def the_structure_and_properties_of_atoms():
    """
            @author: Tang Miaojiong & Xiao Hanqi

            如有引用请注明原作者
        """
    pages = st.sidebar.radio('choose a page',
                             ('2.1 玻尔的氢原子理论',
                              '2.2 单电子原子的Schrödinger方程',
                              '2.3 波函数和电子云的图形',
                              '2.4 多电子原子的结构'))
    if pages == '2.1 玻尔的氢原子理论':
        st.markdown("""
## 2.1 玻尔的氢原子理论

### **Bohr的两个假设：**

- **定态规则**

原子有一系列定态，每一个定态有一个相应的能量E，电子在这些定态上绕核做圆周运动，既不吸收能量也不放出能量，而是处于稳定的状态。

即***角动量量子化***

$$M=\\cfrac{nh}{2\\pi}$$

- **频率规则**

电子由一个定态跃迁到另一个定态时，会吸收或发射$\\Delta E$的能量，其中$\\Delta E$为两个定态之间的能量差。

即***能量量子化***

$$\\Delta E=h\\nu$$


### **几个基本物理量的推算：**

- **氢原子半径r**

由 角动量量子化条件 和 电子圆周运动向心力等于电子和核间的库伦引力 联立：

$$\\begin{cases}M=mvr=\\cfrac{nh}{2\\pi}&1 \\\\ \\cfrac{mv^2}{r}=\\cfrac{e^2}{4\\pi\\epsilon_0r^2}&2\\end{cases}$$

得：$$r=\\cfrac{n^2h^2\\epsilon_0}{\\pi me^2}$$

当n=1时，$$r=a_0=\\cfrac{\\epsilon_0h^2}{\\pi me^2}=52.92pm$$

- **单电子能量E**

电子能量等于电子动能和静电吸引的势能之和：$E=\\cfrac{1}{2}mv^2-\\cfrac{e^2}{4\\pi\\epsilon_0r}$

将②式代入得：$E=-\\cfrac{e^2}{8\\pi\\epsilon_0r}$

将$r=\\cfrac{n^2h^2\\epsilon_0}{\\pi me^2}$代入E得：$$E_n=-\\cfrac{me^4}{8\\epsilon_0^2n^2h^2}$$

- **Rydberg常量$R_H$**

由频率规则，电子跃迁时，吸收或发射的光谱满足：$E_2-E_1=h\\nu=h\\cfrac{c}{\\lambda}$

将$E_n$代入得：$$\\cfrac{1}{\\lambda}=\\cfrac{me^4}{8ch^3\\epsilon_0^2}(\\cfrac{1}{n_1}-\\cfrac{1}{n_2})$$

令$\\cfrac{me^4}{8ch^3\\epsilon_0^2}=R$得经验公式：

$$\\cfrac{1}{\\lambda}=R(\\cfrac{1}{n_1}-\\cfrac{1}{n_2})$$

其中R即为Rydberg常量，若$m$代入电子质量$m_e=9.10953*10^{-31}kg$,得$R_∞=109737cm^{-1}$

若代入氢原子的折合质量：$\\mu_H=\\cfrac{m_em_N}{m_e+m_N}=9.10458*10^{-31}kg$,

得:$$R_H=109678cm^{-1}$$

Bohr理论计算所得的$R_H$和归纳所得的实验值符合的很好，也因此Bohr原子结构模型风行一时。

- **Bohr理论的局限性：**

> ①既要求满足角动量量子化和能量量子化，又服从Newton力学，相互矛盾；

> ②从电磁学理论，带电粒子做圆周运动会辐射能量，发出电磁波，原子不能稳定存在；

> ③只涉及了粒子的粒子性，没有涉及电子的波性。
""")
    if pages == '2.2 单电子原子的Schrödinger方程':
        st.markdown("""
## 2.2 单电子原子的薛定谔方程

对于一维势箱，我们知道：

$$\\begin{cases}V=0&0<x<l \\\\V=\\infty &x<=0\\cup x>=l \\end{cases}$$

在势箱内部V=0，其薛定谔方程的解为： $-\\cfrac{h^2}{8\\pi^2m}\\cfrac{d^2}{dx^2}=E\\psi$

而对于单电子原子，例如核电荷为Z，核外只有一个电子的原子

示例：$H, He^+, Li^{2+}$这种原子的势能

$$V=-\\cfrac{Ze^2}{4\\pi\\epsilon_0r}$$

将这个势能代入哈密顿算符：$H=-\\cfrac{h^2}{8\\pi^2m}\\nabla^2+V$

得：

$$\\left[-\\cfrac{h^2}{8\\pi^2\\mu}\\nabla^2-\\cfrac{Ze^2}{4\\pi\\epsilon_0r}\\right]\\psi=E\\psi$$

（$\\nabla=\\cfrac{\\partial^2}{\\partial x^2}+\\cfrac{\\partial^2}{\\partial y^2}+\\cfrac{\\partial^2}{\\partial z^2}$为拉普拉斯算符，$\\mu_H$则是约化质量$\\mu_H=\\cfrac{m_em_N}{m_e+m_N}$）

解的时候，把笛卡尔坐标变换成球极坐标，采用变数分离法求解。
""")
    if pages == '2.3 波函数和电子云的图形':
        st.markdown("""
        ## 2.3 波函数和电子云的图形
""")
        st.markdown("""
        为了更直观地理解波函数在空间中的分布，我们可以绘制波函数的一维、二维和三维图像，从而了解波函数的几何性质。

        在这里我为了程序的独立性和完整性，将波函数和电子云的图形单列在了“氢原子三维波函数演示程序”一节中，读者可以直接利用程序进行计算。

        小节中引用的参考资料相比《结构化学基础》《量子力学》中的相关描述更为准确，这不由得让人吐槽教材的一定过时性，不过也可能是因为这部分内容不考所以多年未有人发现错误并使得编者纠正。

        [氢原子勒让德方程](https://zhuanlan.zhihu.com/p/131295215)、[氢原子拉盖尔方程](https://zhuanlan.zhihu.com/p/131296509)
""")
    if pages == '2.4 多电子原子的结构':
        st.markdown("""
        ## 2.4 多电子原子的结构
""")
        st.markdown("""
        难点：不同于单电子原子的是，多电子原子的电子之间也存在着相互作用，使得薛定谔方程求解更加困难，一般用近似方法求数值解。

以He原子为例的多电子原子的薛定谔方程：

$\\left[-\\cfrac{h^2}{8\\pi^2m}(\\nabla^2_1+\\nabla^2_2)-\\cfrac{Ze^2}{4\\pi\\epsilon_0}(\\cfrac{1}{r_1}+\\cfrac{1}{r_2})+\\cfrac{e^2}{4\\pi\\epsilon_0r_{12}}\\right]\\phi=E\\phi$

其中$r_{12}$是两个电子的距离。由于此项存在，无法像之前那样分离变量。

### 方法1：忽略电子间作用项

也就是让$\\cfrac{e^2}{4\\pi\\epsilon_0r_{12}}=0$

这样就能正常分离变量，得到每个轨道的波函数。此时解出来的每个波函数叫“单电子波函数”。

体系的近似波函数$\\phi=\\phi_1\\phi_2\\phi_3...\\phi_m$

体系总能量$E=E_1+E_2+...+E_n$

**单电子近似**：在不忽略电子间作用的前提下，用单电子波函数描述多电子原子中单个电子的运动状态。此时电子都分别在某个势场里独立运动，如同单电子体系一样。

### 方法2：自洽场法（又名Hartree-Fock法）

假定电子i处在原子核与其他(n-1)个电子组成的平均势场里运动。平均势场的处理里面，电子作用项可以近似。总之它可以只和$r_i$有关

那么$H_i=-\\cfrac{1}{2}\\nabla_i^2-\\cfrac{Z}{r_i}+V(r_i)$。

其中$V(r_i)$是别的电子的波函数决定的。算出来以后，得到的哈密顿算符还要迭代，直到达到所求的精度。
### 方法3：中心力场法

将其他电子的作用视作一个球对称的、只和径向有关的力场，如同原子核的力场一样。

那么第i个电子的势能函数就是

$V_i=-\\cfrac{Z}{r_i}+\\cfrac{\\sigma_i}{\\sigma_i}=-\\cfrac{Z-\\sigma_i}{r_i}=-\\cfrac{Z_i^*}{r_i}$

这里的$Z^*_i$就是有效核电荷，然后得出多电子原子中第i个电子的单电子薛定谔方程：

$[-\\cfrac{1}{2}\\nabla_i^2-\\cfrac{Z-\\sigma_i}{r_i}]\\phi_i=E_i\\phi_i$

于是乎，$E_i=-13.6(Z_i^*)^2/n^2$

还可以引申到屏蔽效应上。
""")
        st.markdown("""
        ### Slater经验规则：
> 电子层分组：1s|2s,2p|3s,3p|3d|4s,4p|4d|4f|5s,5p|...
>
> 外层电子$\\sigma=0$
>
> 同一组$\\sigma=0.35$，但是1s的话$\\sigma=0.30$
>
> s和p的话，相邻组的$\\sigma=0.85$；d和f的话，相邻组的电子对它屏蔽常数是1.00
>
> 更内的都是1.00
""")
        st.markdown("""
        ### 基态原子的电子排布
>泡利原理：交换两个全同的费米子的坐标，整个体系的波函数应反对称。反映在原子里，没有两个电子拥有完全相同的4个量子数。
>
>能量最低原理：满足泡利原理的前提下，电子优先使整个原子能量最低。
>
>Hund规则：能量高低相等的轨道上，电子尽量分占不同轨道，自旋相同。
""")
        st.markdown("""
        多电子原子的组态及自旋都已知时，可以用一个总的波函数$\\phi(1,2,...,n)$表示n个电子的状态

以He为例，

两个电子都在1s，自旋分别是$\\alpha$和$\\beta$

若波函数表示为$\\phi_{1s}(1)\\alpha(1)\\phi_{1s}(2)\\beta(2)$

坐标交换后的结果并不能满足泡利原理，并不是反对称

所以，线性组合，

$$\\phi(1,2)=\\cfrac{1}{\\sqrt{2}}(\\phi_{1s}(1)\\alpha(1)\\phi_{1s}(2)\\beta(2)-\\phi_{1s}(2)\\alpha(2)\\phi_{1s}(1)\\beta(1))= \\cfrac{1}{\\sqrt{2}}
\\left|\\begin{array}{cccc} 
    \\phi_{1s}(1)\\alpha(1) &  \\phi_{1s}(2)\\alpha(2)    \\\\ 
 \\phi_{1s}(2)\\beta(2)&\\phi_{1s}(1)\\beta(1)
\\end{array}\\right| 
$$

是为Slater行列式

n电子原子的Slater行列式：
$$\\phi(1,2,...,n)=\\cfrac{1}{\\sqrt{n!}}\\left|\\begin{array}{cccc} 
    \\psi_1(1) &  \\psi_1(2)  & ... & \\psi_1(n)  \\\\ 
 \\psi_2(1) &  \\psi_2(2)  & ... & \\psi_2(n) \\\\
 ... & ... & ... & ... \\\\
 \\psi_n(1) &  \\psi_n(2)  & ... & \\psi_n(n)
\\end{array}\\right| $$
""")