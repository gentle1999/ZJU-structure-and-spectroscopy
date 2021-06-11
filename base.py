import inspect
import textwrap
from collections import OrderedDict

import streamlit as st
from streamlit.logger import get_logger
from demos import intro, fundamentals_of_quantum_mechanics, the_structure_and_properties_of_atoms, \
    wave_function_display, structural_chemistry_of_covalent_bonds_and_diatomic_molecules, symmetry_of_molecules, \
    hybridization_and_HMO, complexes, ion

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
