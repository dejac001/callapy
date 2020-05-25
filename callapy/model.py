r"""
The physical adsorption of both solute
and solvent from liquid solutions onto solids
is difficult to determine in widely adopted
static (i.e., batch) experiments, because
only the bulk liquid reservoir can be probed
directly. The consequences of this limitation
are best explained by the mass balances.
The total mass balance for uptake from
a binary mixture can be expressed as

.. todo::
    add figure here

.. math::
    V_\text{in}\rho_\text{in} = V_\text{eq}\rho_\text{eq} + m\left(Q_\text{A} + Q_\text{S}\right)
    :label: total_mb

where :math:`V_\text{in}` is the initial solution volume,
:math:`\rho_\text{in}` is the initial solution density,
:math:`V_\text{eq}` is the solution volume measured at equilibrium,
:math:`\rho_\text{eq}` is the solution density at equilibrium,
:math:`m` is the mass of the solid,
:math:`Q_\text{A}` is the loading of the solute A,
and :math:`Q_\text{S}` is the loading of the solvent S.
The mass balance on the solute is

.. math::
    V_\text{in}C_\text{A,in} = V_\text{eq}C_\text{A,eq} + m Q_\text{A}
    :label: component_mb

where :math:`C_\text{A,in}` is the initial concentration
of the solute A, and :math:`C_\text{A,eq}` is the
concentration of the solute A measured at equilibrium.

From the batch adsorption procedure, :math:`V_\text{in}`,
:math:`C_\text{A,in}`, :math:`C_\text{A,eq}`,
and :math:`m` are measured.
The initial (:math:`\rho_\text{in}`)
and equilibrium (:math:`\rho_\text{eq}`) densities
are usually either determined from separate experiments,
taken from available literature reports,
or estimated from pure component densities.
As a result, Equations :eq:`total_mb` and :eq:`component_mb`
have three unknowns (:math:`V_\text{eq}`, :math:`Q_\text{A}`,
and :math:`Q_\text{S}`), giving them no unique solution.

Different options typically employed in the
literature are displayed below

========================================        ========================================================================
Name                                                Additional Relation
========================================        ========================================================================
Excess adsorption (XS)                           :math:`V_\text{in}=V_\text{eq}`
No solvent adsorbs (NS)                          :math:`Q_\text{S}=0`
Volume change by solute adsorption (VC)          :math:`V_\text{eq}=V_\text{in} - mQ_\text{A}/\rho_\text{A}`
Pore filling adsorption (PF)                     :math:`V_\text{p}=Q_\text{A}/\rho_\text{A} + Q_\text{S}/\rho_\text{S}`
========================================        ========================================================================

"""


class DataPoint:
    r"""One data point

    :param V_in: initial volume, :math:`V_\text{in}`
    :param d_in: initial density, :math:`\rho_\text{in}`
    :param d_eq: equilibrium density, :math:`\rho_\text{eq}`
    :param m: mass of zeolite, :math:`m`
    :param C_Ain: initial concentration of solute A, :math:`C_\text{A,in}`
    :param C_Aeq: equilibrium concentration of solute A, :math:`C_\text{A,eq}`
    :param d_A: estimated density of adsorbate used in calculating PF adsorption, defaults to None
    :param d_S: estimated density of solvent in pores in calculating PF adsoption, defaults to None
    :param V_units: units for volume, defaults to ""
    :param C_units: units for concentration, defaults to ""
    :param m_units: units for mass of solid, defaults to ""
    :param d_units: units for density, defaults to ""


    """

    def __init__(self, V_in: float, d_in: float, d_eq: float, m: float,
                 C_Ain: float, C_Aeq: float,
                 d_A: float = None,
                 d_S: float = None,
                 V_p: float = None,
                 V_units: str = "",
                 C_units: str = "",
                 m_units: str = "",
                 d_units: str = ""
                 ):
        self.V_in = V_in
        self.d_in = d_in
        self.d_eq = d_eq
        self.m = m
        self.C_Ain = C_Ain
        self.C_Aeq = C_Aeq
        self.V_units = V_units
        self.C_units = C_units
        self.m_units = m_units
        self.d_units = d_units
        self.d_A = d_A
        self.d_S = d_S
        self.V_p = V_p
