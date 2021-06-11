import streamlit as st


def structural_chemistry_of_covalent_bonds_and_diatomic_molecules():
    """
            @author: Tang Miaojiong & Wei Yuxi & Wei Chenshuai

            如有引用请注明原作者
    """
    pages = st.sidebar.radio('choose a page',
                             ('3.1 化学键的定义和类型',
                              '3.2 单电子氢分子的结构和共价键的本质',
                              '3.3 分子轨道理论和双原子分子的结构',
                              '3.4 氢气分子的结构和价键理论'
                              ))
    if pages == '3.1 化学键的定义和类型':
        st.markdown("""
            ## 3.1 化学键的定义和类型
""")
        st.markdown("""
        ### 化学键的定义

广义的说**化学键是将原子结合成物质的作用**  

一般的定义是**化学键是在分子或晶体中两个或多个原子间的强烈相互作用**

### 化学键的类型。

化学键有**共价键**、**离子键**、**金属键**三种**极限键型**，而实际的化学键是在这三者之间通过键型变异而偏离极限键型，为多种多样的过渡型式的化学键。 三种极限键型的特征如下 

| 性质|      共价键 |  离子键 | 金属键|
|:----------:|:-------------:|:------:|:------:|
| A和B的电负性 |  A电负性   B电负性|  A电正性 B电负性|A电正性  B电正性 |
| 结合力性质 |    两原子成键电子轨道相互叠加形成   |   离子间的静电作用 |自由电子和金属正离子之间的相互吸引 |
| 结合的几何形式 | 轨道叠加和价电子数控制 |   A-B接近，A-A与B-B之间远离 | 金属原子密堆积 |
|键强度性质|由净的成键电子数决定|由离子的电价和配位数决定|6个价电子最高，大于6和小于6都逐渐减小|
|电学性质|固态和熔融态均为绝缘体或半导体|固态为绝缘体，熔融态为导体|导体|  

以上三种是极限键型。有一种说法认为像氢键之类的次级键也参与分子的结构，也算一种类型的化学键。如果将离子键、共价键、金属键、次级键看做四面体的四个顶点，实际分子就处在四面体的任意一点上。可能在顶点，棱上，或则面上，甚至四面体内部。例如石墨除了同层中C与C的共价键，还有层与层之间的次级键，以及可以看成二维的金属键的大$\\pi$键。

![RUNOOB 图标](https://pic1.zhimg.com/100/v2-44870feea5784c6c050bf49888c803ae_r.jpeg
) 
""")
        st.markdown("""
### 键型的多样性

世界上已知的元素有118种，每种元素的原子在不同的条件和成键环境下可以形成不同的化学键，而研究如此复杂多样的体系还是要从研究最简单的原子体系**H原子**所能所能够成的化学键开始。

氢的质子数为一核外只有一个电子，基态时电子处于1s轨道上。可以失去一个电子成$H^+$也可以失去一个电子形成$H^-$。氢只用一个1s轨道和一个电子参与成键却可以形成多种类型的化学键。

#### 1.共价单键

由H,C,O,N,S形成的氢化物和各种有机化合物中H都以共价单键与其他原子结合，其共价半径为32pm.

#### 2.离子键

H原子获得一个电子形成$H^-$离子，由于H原子电子亲和能小（0.75eV），所以只有与正电性高的金属才能形成**盐型氢化物**，如**NaH,$CaH_2$**等。  

当H原子丢失一个电子形成$H^+$,$H^+$是一个裸露的质子，半径约为 0.0015pm，当$H^+$接近其他原子时能使其他原子变形，形成共价键再和其他阴离子形成化合物。

#### 3.金属键

$H_2$能被某些金属或合金，如Pd,Ni,La,$LaNi_5$等大量吸附，以原子状态存在于金属或合金的空隙中，H原子贡献了电子汇入整个金属的电子海中，所以看做H形成了金属键.例如  

$$LaNi_5 + 3H_2\\stackrel{\\mathrm{0.4MPa}}{\\rightleftharpoons}{LaNi_5H_6}$$

而只由氢原子形成的金属键被认为在非常高的压力和很低的温度下如（250GPa和77K），$H_2$分子转变成线性氢原子链$H_n$,并表现出金属那样的导电性和不透明性。

#### 4.氢键

氢键通常的格式为X-H…Y，X和Y均为高电负性原子。Y有一対孤对电子作为质子的受体。X-H作为质子的给体

#### 5.非常规氢键

##### 1.缺电子多中心氢桥键

在硼烷中存在3c-2e的缺电子多中心键如![RUNOOB 图标](https://pic1.zhimg.com/100/v2-361e596ed0874bcea3f8db84a72aec50_r.jpeg
)  

##### 2.$H^-$配键

$H^-$能作为配体提供一堆电子给一个或多个过渡金属原子形成金属氢化物如$Mg_2NiH_4,Mg_2FeH_6,K_2ReH_9$等。

![RUNOOB 图标](https://pic1.zhimg.com/100/v2-6af86b8c7d229d9d56404e2ee363a41e_r.jpeg
)  

##### 3.分子氢配键

$H_2$能作为一个整体配位金属原子,$H_2$和过渡金属原子之间的键分为两部分：一是$H_2$分子提供成键$\\sigma$电子给空的金属原子的d轨道；另一部分是金属的d轨道电子反馈给$H_2$分子空的$\\sigma^*$反键轨道。**由于反键轨道被填入电子,H-H键被减弱，所以这些配合物可用于$H_2$的活化**  

在**$W(\\eta^2-H_2)(CO)_3[P(C_2H_3)]_2$**以及**$[Fe(\\eta^2-H_2)(H)(PPh_2CH_2CH_2PPh_2)_2]BPh_4$**中$H_2$与金属原子从侧面结合

![RUNOOB 图标](https://pic2.zhimg.com/100/v2-f8b0108ec5b84f928078ab3386e094c9_r.jpeg)

##### 4.抓氢键

抓氢键C-H$\\rightharpoonup$M，半箭头表示由C-H提供两个电子给金属原子M  
C-H$\\rightharpoonup$形成后会使C-H键减弱，可用于活化有机物中的C-H键。  
![RUNOOB 图标](https://pic1.zhimg.com/100/v2-51dc64cfb93157aa3abdd62ad8acead3_r.jpeg
)
""")
    if pages == '3.2 单电子氢分子的结构和共价键的本质':
        st.markdown("""
        ## 3.2 $H^+_2$的结构和共价键的本质
""")
        st.markdown("""
        $H^+_2$作为最简单的双原子分子，可以给讨论多电子的双原子分子提供许多有用的概念。  

### 3.2.1 $H^+_2$的Schrödinger方程  

![RUNOOB 图标](https://pic4.zhimg.com/100/v2-98266a4ca2e00a4ec60cdc3951538e65_r.jpeg)

$H^+_2$坐标关系如图，A、B表示原子核，$r_a$与$r_b$表示电子与两个核间距离，R表示两核间距。则$H^+_2$的Schrödinger方程以原子单位表示为

$$\\left[-\\displaystyle \\cfrac{1}{2}\\nabla^2-\\displaystyle \\cfrac{1}{r_a}-\\displaystyle \\cfrac{1}{r_b}+\\displaystyle \\cfrac{1}{R}\\right]\\psi = E\\psi$$

式中$\\psi$和E分别为$H^+_2$的波函数和能量。等号左边括号中，第一项为电子的动能算符，第二、三项为电子受核的吸引能，第四项为两原子核间的静电排斥能。

**Born-Oppenheimer近似**：

由于电子质量远小于原子核质量，且速度远快于核，故认为**核在电子运动时，近似看为不动**。因此式子中并没有包含核的动能算符项，电子认为在固定的核势场中运动，解得反映电子运动状态的波函数。这样固定核间距R，就可以解Schrödinger方程得到分子中电子的$\\psi$函数和能级。改变R值，则可以获得一系列波函数和相应能级，其中**与电子能量最低值相对应的R就是平衡核间距**$R_e$. 

(品优：单值、连续、有限的。有限即平方可积的，通常要求归一化。)

### 3.2.2 变分法解Schrödinger方程  

变分法（variation method）近似原理：对任一品优波函数$\\psi$,用体系的$\\hat{H}$算符求得能量平均值，将大于或接近于体系基态的能量（$E_0$）。

$$\\left\\langle E\\right\\rangle =\\displaystyle \\cfrac{\\displaystyle \\int{\\psi^*\\hat{H}\\psi d\\tau}}{\\displaystyle \\int{\\psi^*\\psi d\\tau}} \\geq E_0$$

根据此原理，利用求极值方法调节参数，找出能量最低时对应的波函数，即为和体系基态相近似的波函数。

**上式的证明**:

设$\\psi_0,\\psi_1,\\psi_2,...$组成正交，归一的函数组，其能量依次增加，$E_0\\leq E_1\\leq E_2...$，由此可得

$$\\hat{H}\\psi_i = E_i\\psi_i$$

将上式中$\\psi$按体系$\\hat{H}$的本征函数$\\psi_i$展开，即

$$\\psi = c_1\\psi_1 + c_2\\psi_2 + ... = \\sum c_i\\psi_i$$

利用$\\psi_i$的正交、归一性，可得平均能量

$$\\left\\langle E\\right\\rangle = \\displaystyle \\int{\\psi^*\\hat{H}\\psi d\\tau} = \\sum c_i^*c_iE_i$$

因$c_i^*c_i$恒为正值，$\\sum c_i^*c_i = 1$，$0<c_i^*c_i\\leq 1$，故得

$$\\left\\langle E\\right\\rangle-E_0 = \\sum c_i^*c_i(E_i-E_0)\\geq 0$$

所以$\\left\\langle E\\right\\rangle\\geq E_0$。

$c_1,c_2,...,c_n$数值的大小，反映$\\psi_i$对$\\psi$的贡献，$\\psi^2_i$表示$\\psi_i$在$\\psi$中所占的百分数。

常用的变分法是线性变分法，即选择一品优的线性变分函数

$$\\psi = c_1\\psi_1 + c_2\\psi_2 + ... + c_n\\psi_n$$

求出E值最低时对应的线性组合系数$c_i$值，进而求得波函数$\\psi$。
""")
        st.markdown("""
**解$H^+_2$的Schrödinger方程**

当电子运动到核A附近时，$\\psi$近似于原子轨道$\\psi_a$；同样，到核B附近时，近似于$\\psi_b$。根据电子的波动性，波可以叠加，$\\psi$将会在一定程度上继承和反映原子轨道的性质，因而可用原子轨道线性组合

$$\\psi = c_a\\psi_a + c_b\\psi_b$$

作为$H^+_2$的变分函数，式子中$c_a$和$c_b$为待定参数，而

$$\\psi_a = \\cfrac{1}{\\sqrt{\\pi}}e^{-r_a}, \\psi_b = \\cfrac{1}{\\sqrt{\\pi}}e^{-r_b}$$

将$\\psi$代入$\\left\\langle E\\right\\rangle =\\displaystyle \\cfrac{\\int{\\psi^*\\hat{H}\\psi d\\tau}}{\\int{\\psi^*\\psi d\\tau}}$中，得

$$E_{c_a,c_b} =\\displaystyle \\cfrac{\\int(c_a\\psi_a+c_b\\psi_b)\\hat{H}(c_a\\psi_a+c_b\\psi_b) d\\tau}{ \\int(c_a\\psi_a+c_b\\psi_b)^2 d\\tau}$$

由于$H^+_2$的两个核是等同的，而$\\psi_a$和$\\psi_b$又都是归一化函数，展开上式，并令

$$H_{aa} = \\displaystyle \\int{\\psi^*_a\\hat{H}\\psi_a d\\tau} = H_{bb} = \\displaystyle \\int{\\psi^*_b\\hat{H}\\psi_b d\\tau}$$

$$S_{aa} = \\displaystyle \\int{\\psi^*_a\\psi_a d\\tau} = S_{bb} = \\displaystyle \\int{\\psi^*_b\\psi_b d\\tau}$$

$$S_{ab} = \\displaystyle \\int{\\psi^*_a\\psi_b d\\tau} = \\displaystyle \\int{\\psi^*_b\\psi_a d\\tau} = S_{ba}$$

$$H_{ab} = \\displaystyle \\int{\\psi^*_a\\hat{H}\\psi_b d\\tau} = H_{ba} = \\displaystyle \\int{\\psi^*_b\\hat{H}\\psi_a d\\tau}$$

得

$$E_{c_a,c_b} = \\displaystyle \\cfrac{c_a^2H _{aa}+2c_ac_bH_{ab}+c_b^2H_{bb}}{c_a^2S _{aa}+2c_ac_bS_{ab}+c_b^2S_{bb}} = \\displaystyle \\cfrac{Y}{Z}$$

对$c_a,c_b$偏微商求极值，得

$$\\displaystyle \\cfrac{\\partial E}{\\partial c_a} = \\displaystyle \\cfrac{1}{Z}\\displaystyle \\cfrac{\\partial Y}{\\partial c_a}-\\displaystyle \\cfrac{Y}{Z^2}\\displaystyle \\cfrac{\\partial Z}{\\partial c_a} = 0$$

$$\\displaystyle \\cfrac{\\partial E}{\\partial c_b} = \\displaystyle \\cfrac{1}{Z}\\displaystyle \\cfrac{\\partial Y}{\\partial c_b}-\\displaystyle \\cfrac{Y}{Z^2}\\displaystyle \\cfrac{\\partial Z}{\\partial c_b} = 0$$

消去Z，因为$\\cfrac{Y}{Z} = E$，得

$$\\displaystyle \\cfrac{\\partial Y}{\\partial c_a}-E\\displaystyle \\cfrac{\\partial Z}{\\partial c_a} = 0, \\displaystyle \\cfrac{\\partial Y}{\\partial c_b}-E\\displaystyle \\cfrac{\\partial Z}{\\partial c_b} = 0$$

将Y,Z值代入，并利用上述式子化简，可得到**久期方程组**

$$
\\left\\{ 
\\begin{matrix}
c_a(H_{aa}-E)+c_b(H_{ab}-ES_{ab}) = 0 \\\\
c_a(H_{ab}-ES_{ab})+c_b(H_{ab}-E) = 0\\\\
\\end{matrix}
\\right.
$$

为了使$c_a,c_b$有不完全为零的解，可得久期行列式

$$\\left[ \\begin{matrix} H_{aa}-E &H_{ab}-ES_{ab} \\\\ H_{ab}-ES{ab} &H_{bb}-E\\end{matrix} \\right] = 0$$

解此行列式，得E的两个解

$$E_1 = \\cfrac{H_{aa}+H_{ab}}{1+S_{ab}}$$

$$E_2 = \\cfrac{H_{aa}-H_{ab}}{1-S_{ab}}$$

将$E_1$值代入久期方程组中的E，得$c_a = c_b$，相应的波函数

$$\\psi_1 = c_a(\\psi_a+\\psi_b)$$

将$E_2$值代入久期方程组中的E，得$c_a = -c_b$，相应的波函数

$$\\psi_2 = c_a^,(\\psi_a-\\psi_b)$$  

利用波函数归一化条件，可求得

$$c_a = (2+2S_{ab})^{-\\cfrac{1}{2}}$$

$$c_a^, = (2-2S_{ab})^{-\\cfrac{1}{2}}$$
""")
        st.markdown("""
### 3.2.3 积分$H_{aa},H_{ab},S_{ab}$的意义和$H_2^+$的结构  

#### 1.库仑积分  

通常把$H_{aa},H_{bb}$称为库仑积分，又称为$\\alpha$积分。根据$\\hat{H}$算符表达式，可得

$$H_{aa} = \\int \\psi^*_a \\hat{H} \\psi_a d\\tau = \\int \\psi^*_a [-\\cfrac{1}{2}\\nabla^2-\\cfrac{1}{r_a}-\\cfrac{1}{r_b}+\\cfrac{1}{R}]\\psi_a d\\tau$$

$$=\\int \\psi^*_a [-\\cfrac{1}{2}\\nabla^2-\\cfrac{1}{r_a}]\\psi_a d\\tau+\\cfrac{1}{R}\\int \\psi_a^*\\psi_a d\\tau - \\int \\psi^*_a\\cfrac{1}{r_b}\\psi_a d\\tau$$

$$=E_H+\\cfrac{1}{R}-\\int \\cfrac{\\psi^2_a}{r_b}d \\tau$$

$$=E_H+J$$

$E_H$是基态氢原子的能量。

$$J \\equiv \\cfrac{1}{R}-\\int{\\cfrac{1}{r_b}\\psi^2_b}d \\tau$$

此式中$-\\int{\\cfrac{1}{r_b}\\psi^2_b}d \\tau$表示电子处在$\\psi_a$轨道时受到核B作用的平均吸引能。由于$\\psi_a$为球形对称，它的平均值近似等于电子在A核处受到B核吸引能，其绝对值与两核间排斥能1/R相近，因符号相反，几乎可以抵消。据计算，$H^+_2$的R等于平衡核间距$R_e$时，J值只是$E_H$的5.5%，所以$H_{aa}\\approx E_H$。  

#### 2.交换积分  

$H_{ab}和H_{ba}$称为交换积分，或$\\beta$积分。$\\beta$积分与$\\psi_a和\\psi_b$的重叠程度有关，因而是与核间距R有关的函数。

$$H_{ab} = E_HS_{ab}+\\cfrac{1}{R}S_{ab}-\\int\\cfrac{1}{r_a}\\psi_a\\psi_bd \\tau = E_HS_{ab}+K$$

$$K\\equiv \\cfrac{1}{R}S_{ab}-\\int\\cfrac{1}{r_a}\\psi_a\\psi_bd\\tau$$

在分子的核间距条件下，K为负值，$S_{ab}$为正值，$E_H=-13.6eV$，这就使得$H_{ab}$为负值。所以当两个原子接近成键时，体系能量降低，$H_{ab}$项起重大作用。  

#### 3.重叠积分  

$S_{ab}$称为重叠积分，或称S积分。

$$S_{ab} = \\int\\psi_a\\psi_bd\\tau$$

它与核间距R有关：当R=0时，$S_{ab}=1$；当$R=\\infty$时，$S_{ab}\\rightarrow 0$；R为其他值时，$S_{ab}$的数值可通过具体计算得到。

将上述关系代入变分法求得的$E_1、E_2$中，可得

$$E_1 = E_H\\cfrac{J+K}{1+S}$$

$$E_2 = E_H\\cfrac{J-K}{1-S}$$

积分J,K,S可在以核A和核B为焦点的椭圆坐标中求得，其结果以原子单位表示为

$$J = (1+\\cfrac{1}{R})e^{-2R}$$

$$K = (\\cfrac{1}{R}-\\cfrac{2R}{3})e^{-R}$$

$$S = (1+R+\\cfrac{R^2}{3})e^-R$$

所以这些积分都与R有关，R给定后，可计算其具体数值。

例如，当$R=2a_0时，J=0.0275au,K=-0.1127au,S=0.5863au$，而

$$\\cfrac{J+K}{1+S}=-0.0537au$$

$$\\cfrac{J-K}{1-S}=0.3388au$$

可见，$E_1<E_H<E_2$

下图给出了$H^+_2$的能量随核间距R的变化曲线（E-R曲线）。

图中可见，$E_1$随R的变化出现一个最低点，它从能量的角度说明了$H^+_2$能稳定存在。但是，计算所得$E_1$曲线最低点为$(132pm,170.8kJ·mol^{-1})$，与实验测定的平衡解离能$D_e=269.0kJ·mol^{-1},R=106pm$相差较大。

![RUNOOB 图标](https://pic1.zhimg.com/100/v2-1312055b444e656f8aec9ede389f9940_r.jpeg)

$E_2$随R的增加而单调地下降，当$R\\rightarrow \\infty$时，$E_2$为0，即$H+H^+$的能量$(E_H+E_{H^+})$。

由上述结果可见，用变分法近似解$H^+_2$的Schrödinger方程，可得两个波函数$\\psi_1和\\psi_2$，以及相应的能量$E_1和E_2$

$$\\psi_1 = \\cfrac{1}{\\sqrt{2+2S}}(\\psi_1+\\psi_2), E_1 = \\cfrac{\\alpha+\\beta}{1+S}$$

$$\\psi_2 = \\cfrac{1}{\\sqrt{2-2S}}(\\psi_1-\\psi_2), E_1 = \\cfrac{\\alpha-\\beta}{1-S}$$

相应的概率密度函数（即电子云）分别为

$$\\psi_1^2 = \\cfrac{1}{2+2S}(\\psi_a^2+\\psi_b^2+2\\psi_a\\psi_b)$$

$$\\psi_2^2 = \\cfrac{1}{2-2S}(\\psi_a^2+\\psi_b^2-2\\psi_a\\psi_b)$$

$\\psi_1$的能量比1s轨道的能量低，当电子从氢原子的1s轨道进入$\\psi_1$时，体系的能量降低，$\\psi_1$成为成键轨道。相反，电子进入$\\psi_2$时，$H^+_2$的能量比原来的氢原子能量高，$\\psi_2$成为反键轨道。
""")
        st.markdown("""
### 3.2.4 共价键的本质  

当原子相互靠近时，其原子轨道互相同号叠加，组合成成键分子轨道。当电子进入成键轨道，体系能量降低，形成稳定的分子。此时，原子间形成共价键。

分子中电子的分布，和两个原子的电子分布的简单加和不同。电子云分布的差值图可以直观反映这一结果。

电子在分子中的分布，由分子中空间各点概率密度$(\\psi^2_1)$的大小表示。电子云分布的差值图，是将$(\\psi^2_1)$按空间各点逐点减去处在A核位置的$(\\psi^2_a)$和处在B核位置的$(\\psi^2_b)$后，绘制出的差值等值图。下图给出了$H_2^+$的电子云分布的差值图（$\\psi_1$用精确解的波函数，$\\psi^2_a和\\psi_b^2$的平均占有率各为1/2）。图中实线表示电子云增加的等值线，虚线表示电子云减少的等值线。

![RUNOOB 图标](https://pic4.zhimg.com/100/v2-990740fb003e166f38aa07046b65d42a_r.jpeg)

由图可见，$\\psi_1$轨道的成键作用，实质上是将分子两端原子外侧的电子抽调到2个原子核之间，增加了核间区域的电子云。核间电子云同时受两个核吸引，将它们结合在一起，就是$H^+_2$得以形成的原因。

因此说，共价键的形成，是原子轨道，而非电子云的叠加。原子轨道有正有负，按波的规律叠加，或增强，或削弱，形成成键或反键轨道；而电子云，$|\\psi|^2$的大小只反映电荷的分布，无所谓正负号，从物理意义考虑，同号电荷互相接近，只有静电排斥作用。由原子轨道叠加形成分子轨道时，在$|\\psi|^2$中会出现交叉项$2\\psi_a\\psi_b$,使得电子分布的差值图不为0；但若由电子云$|\\psi_a|^2$和$|\\psi_b|^2$叠加，差值图为零，就没有成键时电子云分布改变的效应。

""")

    if pages == '3.3 分子轨道理论和双原子分子的结构':
        st.markdown("""
        ## 3.3 分子轨道理论和双原子分子的结构
""")
        st.markdown("""
        ### 3.3.1 简单分子轨道理论

#### 1.分子轨道概念

分子轨道理论认为分子中的电子都在由各个原子核和其余电子组成的平均势场中运动，电子的运动状态可用波函数$\\psi$描述,称为分子中的单电子波函数，或分子轨道。  

一个分子中有一系列分子轨道$\\psi_i(i=1, 2, …, n)$, 每个分子轨道描述一个单电子态，它们各有自己的能量本征值$E_i$。电子在各分子轨道所描述的单电子态上的排布遵循能量最低原理和泡利原理，即电子按能量从低到高排布，每个分子轨道内最多容纳一对自旋相反的电子。分子总能量是各电子所占据分子轨道能量之和。  

#### 2.分子轨道形成

一般分子的分子轨道都不能从Schrödinger方程严格解出，要得到近似的分子轨道可以通过原子轨道的线性组合（Linear Combination of atomic orbitals）构造，即线性变分法。上节中计算出的$H^+_2$成键轨道和反键轨道都是由原子轨道$\\psi_a$和$\\psi_b$的线性组合构成的。实际上，分子轨道法是处理$H^+_2$问题时所用方法的推广。LCAO中线性组合的系数，以及原子轨道内可能包括的可调参数（比如电子感受到的有效电荷数$Z^*$），都可以通过线性变分法调节，使该状态的能量达到最小。  

要使原子轨道有效地组合成分子轨道，必须满足能级高低相近、轨道最大重叠、对称性匹配3个条件。  

**对称性匹配**：两原子轨道重叠部分符号相同，则形成能量降低的成键轨道；符号相反，形成反键轨道；若两者效果抵消，则形成非键轨道。  

**轨道最大重叠**：使$\\beta$积分（交换积分）最大，要求两原子轨道重叠有一定取向，使共价键具有方向性。  

**能级高低相近**：两原子轨道能极差越大，组成分子轨道成键能力就越小；当量原子轨道能级不同时，能级降低的分子轨道含有较多成分的低能级原子轨道，能级升高的分子轨道含有较多成分的高能级原子轨道。

能量高低相近条件可近似证明如下：设$\\psi_a$和$\\psi_b$为A,B两个原子的能级高低不同的原子轨道，$E_a<E_b$。

它们组合成分子轨道，即$\\psi = c_a\\psi_a+c_b\\psi_b$。

展开久期行列式，并假设$H_{aa}=E_a$,$H_{bb}=E_b$,$H_{ab}=\\beta$,$S_{ab}=0$,则有

$$(E_a-E)(E_b-E)-\\beta^2=0$$

解得分子轨道能量E的两个解

$$E_1=\\displaystyle \\cfrac{1}{2}[(E_a+E_b)-\\sqrt{(E_a-E_b)^2+4\\beta^2}]=E_a-U$$

$$E_2=\\displaystyle \\cfrac{1}{2}[(E_a+E_b)+\\sqrt{(E_a-E_b)^2+4\\beta^2}]=E_b+U$$

式中$U=\\displaystyle \\cfrac{1}{2}[\\sqrt{(E_a-E_b)^2+4\\beta^2}-(E_b-E_a)]>0$。

因为U>0,能级高低顺序是$E_1<E_a<E_b<E_2$；$E_1$是成键轨道的能级，$E_2$是反键轨道的能级。$E_1$比$E_a$还要低，降低值为U；$E_2$比$E_b$还要高，升高值为U。

U不仅和$\\beta$有关，而且和$(E_b-E_a)$的差值有关，当$E_a=E_b$时，$U=|\\beta|$,$\\beta$是负值，所得结果与变分法解$H^+_2$所得$E_1、E_2$相同；当$(E_a-E_b)>>|\\beta|$时，$U\\approx0,E_1\\approx E_a,E_2\\approx E_b$。

从久期方程组出发，如将E值分别用$E_1=E_a-U$和$E_2=E_b+U$代入，化简，得

$$(\\displaystyle \\cfrac{c_a}{c_b})_1=-\\displaystyle \\cfrac{U}{\\beta}\\approx0,\\psi_1\\approx\\psi_a$$

$$(\\displaystyle \\cfrac{c_a}{c_b})_2=\\displaystyle \\cfrac{U}{\\beta}\\approx0,\\psi_2\\approx\\psi_b$$

分子轨道$\\psi_1$和$\\psi_2$还原为原子轨道$\\psi_a$和$\\psi_b$，不能有效成键。
""")
        st.markdown("""
### 3.3.2 分子轨道的分类和分布特点

#### 1.$\\sigma$轨道和$\\sigma$键

具有圆柱对称性的分子轨道，对称轴就是连接两个原子核的键轴。可由s轨道与s轨道、s轨道与p轨道、p轨道与p轨道等形成。$\\sigma$轨道上的电子为$\\sigma$电子，由$\\sigma$电子形成的共价键为$\\sigma$键。

![RUNOOB 图标](https://pic2.zhimg.com/100/v2-38d992274793430c358333f55c9118ae_r.jpeg) 

![RUNOOB 图标](https://pic4.zhimg.com/100/v2-6fc43725ee1b6a5c1e4d97ba4e07e885_r.jpeg) 

#### 2.$\\pi$轨道和$\\pi$键

取键轴沿$z$轴方向，原子的$p_x$和$p_y$轨道的极大值方向均与键轴垂直；当有两个原子沿$z$轴靠近，2个$p_x$（或$p_y$）轨道沿键轴方向重叠，形成$\\pi$轨道。通过键轴有一个节面，若两轨道符号相反叠加，则垂直键轴还有一个节面。

![RUNOOB 图标](https://pic2.zhimg.com/100/v2-eee2344ee959e38811f4c07c0c749265_r.jpeg)

![RUNOOB 图标](https://pic3.zhimg.com/100/v2-477a44b96eae763fd4274b064bba7b87_r.jpeg)    

#### 3.$\\delta$轨道和$\\delta$键

通过键轴有两个节面。若键轴方向为$z$轴方向，则2个$d_{xy}$（或$d_{x^2-y^2}$）轨道重叠可形成$\\delta$轨道。出现在某些含金属多重键的过渡金属化合物中。

![RUNOOB 图标](https://pic2.zhimg.com/100/v2-861c97ba7bf409eb893160f9673fcf9f_r.jpeg)

![RUNOOB 图标](https://pic2.zhimg.com/100/v2-070b1c0eb7c040158f708ff6d3732bf9_r.jpeg)   

#### 4.分子轨道的区分

根据构成它的原子轨道区分：如由1s原子轨道组成的成键$\\sigma$轨道以$\\sigma_{1s}$表示，由2p轨道组成的反键$\\pi$轨道以$\\pi_{2p}^*$表示。  
根据对称性区分：以键轴中心为原点，中心对称以g表示，中心反对称以u表示。

""")
        st.markdown("""
### 3.3.3 同核双原子分子的结构

#### 1.$H_2$分子结构

$H_2$分子基态电子组态为$(\\sigma_{1s})^2$，描述其轨道运动的波函数为$\\psi_{轨道}=\\sigma_{1s}(1)\\sigma_{1s}(2)$  

考虑Pauli原理，其自旋函数为$\\displaystyle \\cfrac{1}{\\sqrt{2}}[\\alpha(1)\\beta(2)-\\alpha(2)\\beta(1)]$   

全波函数$\\psi_{全}=\\sigma_{1s}(1)\\sigma_{1s}(2)\\displaystyle \\cfrac{1}{\\sqrt{2}}[\\alpha(1)\\beta(2)-\\alpha(2)\\beta(1)]$  

以Slater行列式表示为  

$$\\psi_{全}=\\displaystyle \\cfrac{1}{\\sqrt{2}}\\left[ \\begin{matrix} \\sigma_{1s}(1)\\alpha(1) &\\sigma_{1s}(1)\\beta(1) \\\\ \\sigma_{1s}(2)\\alpha(2) &\\sigma_{1s}(2)\\beta(2)\\end{matrix} \\right]$$  

求得$H_2$分子平衡核间距为73pm，平衡解离能为336.7$kJ·mol^{-1}$，而实验测得平衡核间距为74.12pm，平衡解离能为458.0$kJ·mol^{-1}$，符合情况不好。

#### 2.分子轨道能级顺序

分子轨道能级由两个因素决定：构成**分子轨道的原子轨道类型**和**原子轨道的重叠情况**。 

从原子轨道能级考虑，$1s<2s<2p$，故这些轨道组合成的分子轨道能级依次上升；  

从价层轨道重叠情况考虑，形成$\\sigma$键的轨道重叠比形成$\\pi$键的轨道重叠大；  

得出第二周期同核双原子分子的价层分子轨道能级顺序为  

$$\\sigma_{2s}<\\sigma_{2s}^*<\\sigma_{2p_z}<\\pi_{2p_x}=\\pi_{2p_y}<\\pi_{2p_x}^*=\\pi_{2p_y}^*<\\sigma_{2p_z}^*$$

#### 3.s-p混杂

当价层2s和2p$_z$原子轨道能级相近时，由它们组成的对称性相同的分子轨道能进一步相互作用，组成新的分子轨道。

由于各分子轨道不再是相应原子轨道的叠加，不能用原子轨道的符号表示，而改用对称性表示；分子轨道能级高低次序为  

$$1\\sigma_g<1\\sigma_u<1\\pi_u<2\\sigma_g<1\\pi_g<2\\sigma_u$$

$1\\sigma_u$和$2\\sigma_g$在核间很小，分别变为弱反键和弱成键；

在第二周期元素中，F、O的2s和2p轨道能级差值较大，s-p混杂较少，原分子轨道能级顺序不改变，而O之前的元素s-p混杂显著，能级高低发生变化。

#### 4.例子

$O_2$价电子组态为

$$(\\sigma_{2s})^2(\\sigma_{2s}^*)^2(\\sigma_{2p_z})^2(\\pi_{2p_x})^2(\\pi_{2p_y})^2(\\pi_{2p_x}^*)1(\\pi_{2p_y}^*)1$$  

相当于1个$\\sigma$键和2个三电子$\\pi$键（能量上只相当于半个键），键级为2；2个单电子使$O_2$分子有顺磁性。

$N_2$价电子组态为

$$(1\\sigma_g)^2(1\\sigma_u)^2(1\\pi_u)^4(2\\sigma_g)^2$$  

三重键为1个$\\sigma$键$[(1\\sigma_g)^2]$和2个$\\pi$键$[(1\\pi_u)^4]$，$(1\\sigma_g)^2$和$(2\\sigma_g)^2$分别具有弱反键和弱成键性质，称为两对孤对电子。

$C_2$价电子组态为

$$(1\\sigma_g)^2(1\\sigma_u)^2(1\\pi_u)^4$$  

由于s-p混杂，$1\\sigma_u$为弱反键轨道，键级在2-3之间。
""")
        st.markdown("""
### 3.3.4 异核双原子分子的结构

异核原子间内层电子的能级高低可以相差很大，但最外层电子的能级高低总是接近的，它们可利用最外层轨道组合成分子轨道。

$CO$价电子组态为

$$(1\\sigma)^2(2\\sigma)^2(1\\pi)^4(3\\sigma)^2$$  

与$N_2$是等电子体，电子排布大致相同，差别是由氧原子提供给分子轨道的电子比碳原子提供的多2个。因此，虽然氧原子的电负性比碳原子高，但氧原子端显正电性，碳原子端显负电性，且偶极矩较小。

$HF$价电子组态为

$$(\\sigma_{2s})^2(\\sigma)^2(\\pi_{2p})^4$$  

有三对非键电子$[(\\sigma_{2s})^2]$$[(\\pi_{2p})^4]$，在F原子周围形成3对孤对电子；F原子（电负性大的原子）对成键轨道的贡献较多，而H原子（电负性小的原子）对反键轨道的贡献较多。
""")
    if pages == '3.4 氢气分子的结构和价键理论':
        st.markdown("""
        ## 3.4 $H_2$分子的结构和价键理论
""")
        st.markdown("""
        ### 3.4.1 价键法解$H_2$的结构

$H_2$分子的Hamilton算符（以原子单位表示）：

$\\hat{H}=[-\\displaystyle \\cfrac{1}{2}\\nabla^2_1-\\displaystyle \\cfrac{1}{r_{a_1}}]+[-\\displaystyle \\cfrac {1}{2}\\nabla^2_2-\\displaystyle \\cfrac{1}{r_{b_2}}]+[-\\displaystyle \\cfrac{1}{r_{a_2}}-\\displaystyle \\cfrac{1}{r_{b_1}}+\\displaystyle \\cfrac{1}{r_{12}}+\\displaystyle \\cfrac{1}{R}]=\\hat{H}_a(1)+\\hat{H}_b(2)+\\hat{H}'$

$\\hat{H}_a(1)$：电子1在$H_A$原子中的Hamilton算符  

$\\hat{H}_b(2)$：电子2在$H_B$原子中的Hamilton算符

$\\hat{H}'$：两个原子组成氢分子后增加的相互作用的势能算符项  

以$\\psi_a=(\\displaystyle \\cfrac{1}{\\sqrt{\\pi}})e^{-r_a}$表示$H_A$的基态波函数，$\\psi_b=(\\displaystyle \\cfrac{1}{\\sqrt{\\pi}})e^{-r_b}$表示$H_B$的基态波函数，当两个氢原子远离，无相互作用时，体系波函数

$\\psi_1(1, 2)=\\psi_a(1)\\psi_b(2)$或$\\psi_2(1, 2)=\\psi_a(2)\\psi_b(1)$（1、2表示第一个电子或第二个电子的坐标）

将$\\psi_1$和$\\psi_2$线性组合，得到$\\psi(1,2)=c_1\\psi_1+c_2\\psi_2$

将其作为$H_2$的近似函数，利用线性变分法可得到：  

$\\psi_+=\\displaystyle \\cfrac{1}{\\sqrt{2+2S_{12}}}(\\psi_1+\\psi_2)=\\displaystyle \\cfrac{1}{\\sqrt{2+2S_{12}}}[\\psi_a(1)\\psi_b(2)+\\psi_a(2)\\psi_b(1)]$     

$E_+=\\displaystyle \\cfrac{H_{11}+H_{12}}{1+S_{12}}$    

$\\psi_-=\\displaystyle \\cfrac{1}{\\sqrt{2-2S_{12}}}(\\psi_1-\\psi_2)=\\displaystyle \\cfrac{1}{\\sqrt{2-2S_{12}}}[\\psi_a(1)\\psi_b(2)-\\psi_a(2)\\psi_b(1)]$    

$E_-=\\displaystyle \\cfrac{H_{11}-H_{12}}{1-S_{12}}$     

$\\psi_+$和$\\psi_-$仅是轨道运动部分的波函数，未包含自旋函数；根据Pauli原理，全波函数应为反对称波函数。

能量低的$\\psi_+$是对称的，故其相应的自旋函数必须反对称：$\\displaystyle \\cfrac{1}{\\sqrt{2}}[\\alpha(1)\\beta(2)-\\alpha(2)\\beta(1)]$   

$$\\psi_{+(全)}=\\psi_+\\displaystyle \\cfrac{1}{\\sqrt{2}}[\\alpha(1)\\beta(2)-\\alpha(2)\\beta(1)]$$

能量高的$\\psi_-$是反对称的，故其相应的自旋函数必须对称。包含2个电子体系的对称自旋波函数有3个：  

$$\\alpha(1)\\alpha(2),m_s = 1$$

$$\\beta(1)\\beta(2),m_s = -1$$

$$\\displaystyle \\cfrac{1}{\\sqrt{2}}[\\alpha(1)\\beta(2)+\\alpha(2)\\beta(1)],m_s = 0$$

$$\\psi_{-(全)}=\\psi_-
\\left\\{ 
\\begin{matrix}
\\alpha(1)\\alpha(2) \\\\
\\beta(1)\\beta(2) \\\\
\\displaystyle \\cfrac{1}{\\sqrt{2}}[\\alpha(1)\\beta(2)+\\alpha(2)\\beta(1)] \\\\
\\end{matrix}
\\right.
$$

故和$\\psi_-$对应的是三重态。

$H_2$处于平衡核间距时，2个电子总概率密度函数$\\rho=2\\int|\\psi|^2d\\tau_2=2\\int|\\psi|^2d\\tau_1$ 

对稳定态：$\\rho_+=\\rho(1)+\\rho(2)=\\int\\psi^2_+(1, 2)d\\tau_1+\\int\\psi^2_+(1, 2)d\\tau_2$   

将$\\psi_+$代入，得

$$\\rho_+=\\displaystyle \\cfrac{1}{1+S^2}[\\psi^2_a+\\psi^2_b+2S\\psi_a\\psi_b]$$

$$\\rho_-=\\displaystyle \\cfrac{1}{1-S^2}[\\psi^2_a+\\psi^2_b-2S\\psi_a\\psi_b]$$   

由于$S=\\int\\psi^*_a\\psi_bd\\tau$，为正值，故稳定态核间概率密度增加，体系能量降低；而激发态核间概率密度降低，核外侧增加，体系能量升高。
""")
        st.markdown("""
### 3.4.2 价键理论

以原子轨道作为近似基函数，描述分子中电子的运动规律。 

对共价键本质的阐释：一对自旋反平行的电子相互接近，使体系能量降低，形成化学键。

根据价键理论，为了增加体系稳定性，各原子价层轨道中未成对电子应尽可能配对，形成最多数目的化学键；原子轨道中未成对电子数即为原子价。由于电子配对后无法再与其他电子配对，从而导致了共价键具有饱和性。原子轨道重叠越多，形成的共价键越牢固，故原子轨道的取向将影响共价键的方向。
""")
        st.markdown("""
### 3.4.3 价键理论和分子轨道理论的比较（以$H_2$分子为例）

#### 1.变分函数不同

价键法（VB）：以原子轨道$\\psi_1(1, 2)=\\psi_a(1)\\psi_b(2)$和$\\psi_2(1, 2)=\\psi_a(2)\\psi_b(1)$作为基函数，两个成键电子保持自己原子的特点，键只与成键的原子有关，具有定域键概念。

分子轨道法（MO）：以原子轨道组合成的分子轨道$\\psi(1)=\\psi_a(1)+\\psi_b(1)$和$\\psi(2)=\\psi_a(2)+\\psi_b(2)$作为基函数，每个分子轨道都涉及整个分子，具有离域键概念。

#### 2.得到基态波函数结果不同

$$\\psi_{VB}=\\displaystyle \\cfrac{1}{\\sqrt{2+2S^2}}[\\psi_a(1)\\psi_b(2)+\\psi_a(2)\\psi_b(1)]$$

$$\\psi_{MO}=\\displaystyle \\cfrac{1}{\\sqrt{2+2S}}[\\psi_a(1)+\\psi_b(1)][\\psi_a(2)+\\psi_b(2)]$$

若将$\\psi_{MO}$展开，得

$$\\psi_{MO}=\\displaystyle \\cfrac{1}{\\sqrt{2+2S}}[\\psi_a(1)\\psi_b(2)+\\psi_a(2)\\psi_b(1)+\\psi_a(1)\\psi_a(2)+\\psi_b(1)\\psi_b(2)]$$

其中前两项与$\\psi_{VB}$相同，可认为是2个电子分别处于不同原子的原子轨道中，为共价项；后两项可认为是2个电子都处于同一原子的原子轨道中，相当于$H_a^+H_b^-$和$H_a^-H_b^+$，为离子项。VB法得到的基态波函数全由共价项构成，忽略了离子项；而MO法得到的基态波函数中共价项和离子项各占50%，过度夸大了离子项的作用。

#### 3.两种方法的改进

**对VB的改进:**加进离子项，则

$$\\psi_{VB（改）}=\\psi_a(1)\\psi_b(2)+\\psi_a(2)\\psi_b(1)+\\delta[\\psi_a(1)\\psi_a(2)+\\psi_b(1)\\psi_b(2)]$$

$\\delta$与核间距$R$有关，当$R$趋于无穷大时，$\\delta$趋于0。以上式为变分函数求解，得平衡时$\\delta=0.26$。

**对MO的改进:**将其他组态如激发态加入变分函数（组态相互作用），得

$$\\psi_{MO（改）}=[\\psi_a(1)+\\psi_b(1)][\\psi_a(2)+\\psi_b(2)]+\\lambda[\\psi_a(1)-\\psi_b(1)][\\psi_a(2)+\\psi_b(2)]$$

该函数尚未归一化，可乘一个常数$\\displaystyle \\cfrac{1}{1-\\lambda}$，得

$$\\psi_{MO（改）}=\\psi_a(1)\\psi_b(2)+\\psi_a(2)\\psi_b(1)+\\displaystyle \\cfrac{1+\\lambda}{1-\\lambda}[\\psi_a(1)\\psi_a(2)+\\psi_b(1)\\psi_b(2)]$$

当$\\delta=\\displaystyle \\cfrac{1+\\lambda}{1-\\lambda}$时，$\\psi_{MO（改）}=\\psi_{VB（改）}$

#### 4.电子云分布的对比

$$\\rho_{VB}=\\displaystyle \\cfrac{1}{1+S^2}[\\psi^2_a+\\psi^2_b+2S\\psi_a\\psi_b]$$

$$\\rho_{MO}=\\displaystyle \\cfrac{1}{1+S}[(\\psi_a+\\psi_b)^2]$$

由于$S=\\int\\psi^*_a\\psi_bd\\tau<1$，在两核之间$\\rho_{MO}>\\rho_{VB}$，即在MO法中把电子云过多地集中到核间，引起排斥增大，因而求得解离能偏低。
""")