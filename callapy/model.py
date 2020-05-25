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

The excess adsorption (XS) is one common approach.
In this case, the volume of solution at equilibrium is assumed
to be the same as the initial volume of solution.
The third relationship required to close the mass balances is

.. math::
    V_\text{in} = V_\text{eq}

The solute loading calculated by the XS approach is expressed as

.. math::
    Q_{\mathrm{A}}^{\mathrm{XS}} = \frac{V_{\mathrm{in}}\left(C_{\mathrm{A,in}}-C_{\mathrm{A,eq}}\right)}{m}
    :label: XS_QA

The solvent loading calculated by the XS approach is expressed as

.. math::
    Q_{\mathrm{S}}^{\mathrm{XS}} = \frac{V_{\mathrm{in}}\left[
        \rho_{\mathrm{in}}-\rho_{\mathrm{eq}}-
        \left(C_{\mathrm{A,in}}-C_{\mathrm{A,eq}}\right)\right]}{m}

Another option is to assume that no solvent (NS) adsorbs into the solid
(i.e., only solute adsorbs).
The third relationship required to close the mass balances is

.. math::
    Q_\text{S} = 0
    :label: NS_QS

The solute loading calculated by the NS approach can be obtained by

.. math::
    Q_{\mathrm{A}}^{\mathrm{NS}} = \frac{
        V_{\mathrm{in}}\left[\rho_{\mathrm{in}}-\left(
        \frac{C_{\mathrm{A,in}}}{C_{\mathrm{A,eq}}}\rho_{\mathrm{eq}}\right)\right]}
        {m\left(1-\frac{\rho_{\mathrm{eq}}}{C_{\mathrm{A,eq}}}\right)}
    :label: NS_QA

By definition, the solvent loading for the NS approach is zero.

The volume change by solute adsorption method (VC) estimates the volume
change of solution based off of how much solute adsorbs.
The third relqtionship required to close the mass balances is

.. math::
    V_\text{eq}=V_\text{in} - mQ_\text{A}/\rho_\text{A}


The solute loading calculated by the VC method is calculated as

.. math::
    Q_{\mathrm{A}}^{\mathrm{VC}} = \frac{V_{\mathrm{in}}\left(C_{\mathrm{A,in}}-C_{\mathrm{A,eq}}\right)}{
    m\left(1-\frac{C_{\mathrm{A,eq}}}{\rho_{\mathrm{A}}}\right)}
    :label: VC_QA

where :math:`\rho_\text{A}` is an estimated adsorbed density
of the solute A.
The solvent loading calculated by the VC approach is expressed as

.. math::
    Q_{\mathrm{S}}^{\mathrm{VC}} = \frac{V_{\mathrm{in}}}{m}\left[
    \rho_{\mathrm{in}}-\rho_{\mathrm{eq}}
    -\left(1-\frac{\rho_{\mathrm{eq}}}{\rho_{\mathrm{A}}}\right)
    \left(\frac{C_{\mathrm{A,in}}-C_{\mathrm{A,eq}}}
    {1-\frac{C_{\mathrm{A,eq}}}{\rho_{\mathrm{A}}}}\right)
    \right]
    :label: VC_QS

Another option is to assume that the pores in the solid are
filled upon adsorption.
The additional relationship is

.. math::
    V_\text{p}=Q_\text{A}/\rho_\text{A} + Q_\text{S}/\rho_\text{S}

where :math:`\rho_\text{S}` is an estimated density of the
solvent, and :math:`V_\text{p}` is an estimated pore volume of the adsorbent.

For the pore filling model, the solute loading can be calculated as

.. math::
    Q_{\mathrm{A}}^{\mathrm{PF}} = \frac{
    V_{\mathrm{in}}\left[\rho_{\mathrm{in}}-\left(
    \frac{C_{\mathrm{A,in}}}{C_{\mathrm{A,eq}}}\rho_{\mathrm{eq}}\right)\right]
    -m\rho_{\mathrm{S}}V_{\mathrm{p}}
    }{
    m\left(1-\frac{\rho_{\mathrm{eq}}}{C_{\mathrm{A,eq}}} -
    \frac{\rho_{\mathrm{S}}}{\rho_{\mathrm{A}}}\right)
    }
    :label: PF_QA

while the solvent loading can be calculated as

.. math::
    Q_{\mathrm{S}}^{\mathrm{PF}} =
    V_{\mathrm{p}}\rho_{\mathrm{S}}-\frac{\rho_{\mathrm{S}}}{\rho_{\mathrm{A}}}\left(
    \frac{
    V_{\mathrm{in}}\left[\rho_{\mathrm{in}}-\left(
    \frac{C_{\mathrm{A,in}}}{C_{\mathrm{A,eq}}}\rho_{\mathrm{eq}}\right)\right]
    -m\rho_{\mathrm{S}}V_{\mathrm{p}}
    }{
    m\left(1-\frac{\rho_{\mathrm{eq}}}{C_{\mathrm{A,eq}}} -
    \frac{\rho_{\mathrm{S}}}{\rho_{\mathrm{A}}}\right)
    }
    \right)

"""


import typing
import numpy as np
import uncertainties as u
input_data = typing.Union[float, typing.List, typing.Tuple, typing.Generator, np.array]
error_data = typing.Union[float, typing.List, typing.Tuple, typing.Generator, np.array, None]


class Model:
    r"""

    :param V_in: initial volume, :math:`V_\text{in}`
    :type V_in: input_data
    :param d_in: initial density, :math:`\rho_\text{in}`
    :type d_in: input_data
    :param d_eq: equilibrium density, :math:`\rho_\text{eq}`
    :type d_eq: input_data
    :param m: mass of zeolite, :math:`m`
    :type m: input_data
    :param CA_in: initial concentration of solute A, :math:`C_\text{A,in}`
    :type CA_in: input_data
    :param CA_eq: equilibrium concentration of solute A, :math:`C_\text{A,eq}`
    :type CA_eq: input_data
    :param d_A: estimated density of adsorbate used in calculating PF adsorption, defaults to None
    :type d_A: input_data, optional
    :param d_S: estimated density of solvent in pores in calculating PF adsoption, defaults to None
    :type d_S: input_data, optional
    :param V_units: units for volume, defaults to ""
    :param V_units: str, optional
    :param C_units: units for concentration, defaults to ""
    :param C_units: str, optional
    :param m_units: units for mass of solid, defaults to ""
    :param m_units: str, optional
    :param d_units: units for density, defaults to ""
    :param d_units: str, optional
    :param V_p: estimated pore volume within solid, defaults to None
    :param V_p: float, optional
    :param e_V_in: error of initial volume, defaults to last decimal point input from :attr:`.Model.V_in`
    :type e_V_in: error_data, optional
    :param e_d_in: error of initial density, defaults to last decimal point input from d_in
    :type e_d_in: error_data, optional
    :param e_d_eq: error of equilibrium density, defaults to last decimal point input from d_eq
    :type e_d_eq: error_data, optional
    :param e_m: error of adsorbent mass, defaults to last decimal point input from e_m
    :type e_m: error_data, optional
    :param e_CA_in: error of adsorbent mass, defaults to last decimal point input from CA_in
    :type e_CA_in: error_data, optional
    :param e_CA_eq: error of adsorbent mass, defaults to last decimal point input from CA_eq
    :type e_CA_eq: error_data, optional

    """

    def __init__(self, **kwargs):
        self.V_in: input_data = kwargs.pop('V_in')
        self.d_in: input_data = kwargs.pop('d_in')
        self.d_eq: input_data = kwargs.pop('d_eq')
        self.m: input_data = kwargs.pop('m')
        self.CA_in: input_data = kwargs.pop('CA_in')
        self.CA_eq: input_data = kwargs.pop('CA_eq')
        self.d_A: input_data = kwargs.pop('d_A', None)
        self.d_S: input_data = kwargs.pop('d_S', None)
        self.V_p: float = kwargs.pop('V_p', None)
        self.V_units: str = kwargs.pop('V_units')
        self.C_units: str = kwargs.pop('C_units')
        self.m_units: str = kwargs.pop('m_units')
        self.d_units: str = kwargs.pop('d_units')
        self.e_V_in: error_data = kwargs.pop('e_V_in', None)
        self.e_d_in: error_data = kwargs.pop('e_d_in', None)
        self.e_d_eq: error_data = kwargs.pop('e_d_eq', None)
        self.e_m: error_data = kwargs.pop('e_m', None)
        self.e_CA_in: error_data = kwargs.pop('e_CA_in', None)

        # todo: if errors are not provided, estimate from last decimal point of each input data
        # todo: convert input datas into uncertainties types np.array([u.ufloat(1., 2.)...])

    def eval_XS(self) -> typing.Tuple:
        r"""Excess adsorption model (XS)

        :param kwargs: key-word arguments
        :return: (:math:`Q_\text{A}`, :math:`Q_\text{S}`, :math:`V_\text{eq}`)
        """
        Q_A = self.V_in * (self.CA_in - self.CA_eq) / self.m
        Q_S = self.V_in * ((self.d_in - self.d_eq) - (self.CA_in - self.CA_eq)) / self.m
        return Q_A, Q_S, self.V_in

    def eval_NS(self) -> typing.Tuple:
        r"""No-solvent adsorption model (NS)

        :param kwargs: key-word arguments
        :return: (:math:`Q_\text{A}`, :math:`Q_\text{S}`, :math:`V_\text{eq}`)
        """
        Q_A = self.V_in * (self.d_in - self.CA_in / self.CA_eq * self.d_eq) / (1 - self.d_eq / self.CA_eq) / self.m
        V_eq = (self.V_in * self.CA_in - self.m * Q_A) / self.CA_eq
        Q_S = u.ufloat(0., 0.)  # todo: change form if more than one data point
        return Q_A, Q_S, V_eq

    def eval_VC(self):
        r"""Volume change by solute adsorption model (VC)

        :param d_A: estimated adsorbed density of solute A, :math:`\rho_\text{A}`
        :param kwargs: key-word arguments
        :return: (:math:`Q_\text{A}`, :math:`Q_\text{S}`, :math:`V_\text{eq}`)
        """
        assert self.d_A is not None, 'Adsorbed density needed for VC method'
        Q_A = self.V_in * (self.CA_in - self.CA_eq) / (self.m * (1 - self.CA_eq / self.d_A))
        V_eq = self.V_in - self.m * Q_A / self.d_A
        Q_S = (self.V_in * self.d_in - V_eq * self.d_eq - self.m * Q_A) / self.m
        return Q_A, Q_S, V_eq

    def PF(self):
        r"""Pore-filling adsorption model (PF)

        :param d_A: estimated adsorbed density of solute A, :math:`\rho_\text{A}`
        :param d_S: estimated adsorbed density of solute S, :math:`\rho_\text{S}`
        :param V_p: estimated pore volume of solid, :math:`V_\text{p}`
        :param kwargs: key-word arguments
        :return: (:math:`Q_\text{A}`, :math:`Q_\text{S}`, :math:`V_\text{eq}`)
        """
        assert self.d_A is not None, 'Adsorbed density needed for PC'
        assert self.V_p is not None, 'Pore volume needed for PF method'
        assert self.d_S is not None, 'Adsorbed density needed for VC method'
        Q_A = ((self.CA_in - (self.d_in / self.d_eq - self.V_p * self.d_S * self.m / (self.V_in * self.d_eq)) * self.CA_eq)
              / (self.m / self.V_in * (1 + (self.d_S/self.d_A - 1) * self.CA_eq / self.d_eq)))
        Q_S = (self.V_p - Q_A/self.d_A) * self.d_S
        V_eq = (self.V_in * self.CA_in - self.m * Q_A) / self.CA_eq
        return Q_A, Q_S, V_eq

