import numpy as np
import sympy as sy
from sympy.abc import x
import math
import plotly.graph_objects as go
import streamlit as st


def wave_function_display():
    """
        @author: Tang Miaojiong

        如有引用请注明原作者
    """
    # let 2Z/na_0 = 1
    pages = st.sidebar.radio('choose a mode', ('波函数值', '一维图像', '二维图像', '三维图像'))

    def LegendreP(n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        p0 = 1
        p1 = x
        for i in range(n - 1):
            temp = ((2 * i + 3) * x * p1 - (i + 1) * p0) / (i + 2)
            p0 = p1
            p1 = temp
        return p1

    def associate_LegendreP(m, n):
        if m >= 0:
            return (1 - x ** 2) ** (m / 2) * sy.diff(LegendreP(n), x, abs(m))
        else:
            return -1 * associate_LegendreP(-m, n)

    def LaguerreP(a, n):
        if n == 0:
            return 1
        elif n == 1:
            return 1 + a - x
        p0 = 1
        p1 = 1 + a - x
        for i in range(n - 1):
            temp = ((2 * i + 3 + a - x) * p1 - (i + 1 + a) * p0) / (i + 2)
            p0 = p1
            p1 = temp
        return p1

    def R_(n, l, r):
        L = sy.lambdify(x, LaguerreP(2 * l + 1, n - l - 1))
        return np.sqrt(8 / n ** 3) * np.sqrt(math.factorial(n - l - 1)) / np.sqrt(2 * n * math.factorial(n + l)) * (
                2 * r / n) ** l * np.exp(-r / n) * L(2 * r / n)

    def Y_(l, m, t, p):
        t_ = sy.Symbol("t_")
        expr = sy.simplify(sy.Pow(1 - sy.cos(t_) ** 2, 0.5))
        exp = sy.simplify(associate_LegendreP(m, l).subs(x, sy.cos(t_)))
        P = sy.lambdify(t_, exp.subs(expr, sy.sin(t_)))
        return np.sqrt(2 * l + 1) / np.sqrt(4 * np.pi) * np.sqrt(
            math.factorial(l - abs(m)) / math.factorial(l + abs(m))) * P(t) * np.cos(m * p)

    def Psi(n, l, m, r, t, p):
        return R_(n, l, r) * Y_(l, m, t, p)

    if pages == '波函数值':
        st.markdown("""
                本程序可以计算氢原子的任意波函数及值，大多数组件包括图形都可以进行交互。

                氢原子波函数等值面函数值很小，如果发现未显示图形，可以先利用提供的接口估算某一位置处的函数值，再将计算得到的函数值作为等值面代入，之后调整容器范围和采样密度，就可以得到理想的波函数图形。

                注：
                - 《结构化学基础（第三版）》中的球谐函数(1,±1)、一部分轨道的波函数、大多数查到的归一化系数表达式都是错误的，读者可以自行检验是否正确。

                - 经过推理验证，知乎用户wkxdl的量子力学笔记[氢原子勒让德方程](https://zhuanlan.zhihu.com/p/131295215)、[氢原子拉盖尔方程](https://zhuanlan.zhihu.com/p/131296509)中得到的结论基本是正确的。

                - 为了便于展示，下面都令$Z/a_0=1$。

                - 本程序中的每一个波函数并不是抄录下来的，而是根据氢原子勒让德方程以及氢原子拉盖尔方程推演出来的，因此理论上可以计算任意轨道，不管它是否已被证实。

                - 程序本体开源，点击左侧“**Show Code**”即可查看
                """)

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        n = st.number_input("输入主量子数，n>0", min_value=1, format="%d", value=3)
    with col2:
        l = st.number_input("输入角量子数，0<=l<n", min_value=0, format="%d", value=2)
    with col3:
        m = st.number_input("输入磁量子数，-l<=m<=l", min_value=-l, format="%d", value=0)

    def wave(n, l, m):
        r_, t_, p_ = sy.symbols('r, theta, phi')

        def R_(n, l):
            L = sy.lambdify(x, LaguerreP(2 * l + 1, n - l - 1))
            return sy.sqrt(8 / sy.Pow(n, 3)) * sy.sqrt(sy.factorial(n - l - 1)) / sy.sqrt(
                2 * n * sy.factorial(n + l)) * (2 * r_ / n) ** l * sy.exp(-r_ / n) * L(2 * r_ / n)

        def Y_(l, m):
            expr = sy.simplify(sy.Pow(1 - sy.cos(t_) ** 2, 0.5))
            P = sy.simplify(associate_LegendreP(m, l).subs(x, sy.cos(t_)))
            return sy.sqrt(2 * l + 1) / sy.sqrt(4 * sy.pi) * sy.sqrt(
                sy.factorial(l - abs(m)) / sy.factorial(l + abs(m))) * sy.cos(m * p_) * P.subs(expr, sy.sin(t_))

        def Psi(n, l, m):
            return R_(n, l) * Y_(l, m)

        return sy.latex(sy.simplify(Psi(n, l, m)))

    st.latex(wave(n, l, m))

    if pages == '波函数值':
        col4, col5, col6 = st.beta_columns(3)
        with col4:
            r = st.number_input("输入半径", min_value=0.0, format="%e", value=0.0)
        with col5:
            t = st.number_input("输入θ", min_value=0.0, value=0.0, max_value=np.pi)
        with col6:
            p = st.number_input("输入φ", min_value=0.0, value=0.0, max_value=2 * np.pi)
        if st.button("计算波函数值"):
            st.write(Psi(n, l, m, r, t, p))

    if pages == '一维图像':
        st.markdown("""
        波函数的一维图像展示的是在一个确定的方向上（由$\\theta$和$\\phi$决定），波函数值随半径增大的变化，就好像洛阳铲取出的土层。
        """)
        col7, col8 = st.beta_columns(2)
        with col7:
            t_ = st.number_input("输入θ", min_value=0.0, value=0.0, max_value=np.pi)
        with col8:
            p_ = st.number_input("输入φ", min_value=0.0, value=0.0, max_value=2 * np.pi)
        r_max = st.number_input("输入最大r", min_value=0.0, value=45.0)
        import plotly.express as px
        R = np.mgrid[0:r_max:100j]
        values = Psi(n, l, m, R, t_, p_)
        fig = px.line(y=values, x=R)
        st.plotly_chart(fig, use_container_width=True)

    if pages == '二维图像':
        st.markdown("""
        波函数的二维图像展示的是在指定角度（方便起见令$\\phi=0$）下的等值线图，相当于三维图像的剖面。
""")
        r_max = st.number_input("输入最大r", min_value=0.0, value=45.0)
        X, Z = np.mgrid[-r_max:r_max:100j, -r_max:r_max:100j]
        R = np.sqrt(X ** 2 + Z ** 2)
        T = np.arccos(Z / R)
        values = Psi(n, l, m, R, T, 0)
        fig = go.Figure(data=go.Contour(
            x=X.flatten(),
            y=Z.flatten(),
            z=values.flatten()
        ))
        st.plotly_chart(fig, use_container_width=True)

    if pages == '三维图像':
        st.markdown("""
        波函数的三维图像展示的是波函数在三维空间中的等值面图
""")
        col9, col10, col11 = st.beta_columns(3)
        with col9:
            a = st.number_input("输入立方体容器范围", value=45)
        with col10:
            d = st.number_input("输入采样密度", min_value=1, format="%d", value=50)
        X, Y, Z = np.mgrid[-a:a:d * 1j, -a:a:d * 1j, -a:a:d * 1j]
        R = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)

        def p_gen(Y, X):
            ans = []
            for i in range(len(X)):
                ans2 = []
                for j in range(len(X[i])):
                    ans3 = []
                    for k in range(len(X[i][j])):
                        if X[i][j][k] >= 0:
                            ans3.append(np.arctan(Y[i][j][k] / X[i][j][k]))
                        else:
                            ans3.append(np.arctan(Y[i][j][k] / X[i][j][k]) + np.pi)
                    ans2.append(ans3)
                ans.append(ans2)
            return np.array(ans)

        T = np.arccos(Z / R)
        P = p_gen(Y, X)
        values = Psi(n, l, m, R, T, P)
        with col11:
            v = st.number_input("输入波函数值", min_value=0.0, value=0.00001, max_value=1.0, format="%e")
        fig = go.Figure(data=go.Volume(
            x=X.flatten(),
            y=Y.flatten(),
            z=Z.flatten(),
            value=values.flatten(),
            isomin=-v,
            isomax=v,
            opacity=0.6,
            caps=dict(x_show=False, y_show=False)
        ))

        st.plotly_chart(fig, use_container_width=True)