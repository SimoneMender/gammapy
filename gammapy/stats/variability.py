# Licensed under a 3-clause BSD style license - see LICENSE.rst
import numpy as np
import scipy.stats as stats

__all__ = [
    "compute_fvar",
    "compute_fpp",
    "compute_chisq",
]


def compute_fvar(flux, flux_err, axis=0):
    r"""Calculate the fractional excess variance.

    This method accesses the ``FLUX`` and ``FLUX_ERR`` columns
    from the lightcurve data.

    The fractional excess variance :math:`F_{var}`, an intrinsic
    variability estimator, is given by

    .. math::
        F_{var} = \sqrt{ \frac{S^{2} - \bar{ \sigma^{2}}}{ \bar{x}^{2}}}

    It is the excess variance after accounting for the measurement errors
    on the light curve :math:`\sigma`. :math:`S` is the variance.

    It is important to note that the errors on the flux must be gaussian.

    Parameters
    ----------
    flux : `~astropy.units.Quantity`
        the measured fluxes
    flux_err : `~astropy.units.Quantity`
        the error on measured fluxes
    axis : int, optional
        Axis along which the excess variance is computed.
        The default is to compute the value on axis 0.

    Returns
    -------
    fvar, fvar_err : `~numpy.ndarray`
        Fractional excess variance.

    References
    ----------
    .. [Vaughan2003] "On characterizing the variability properties of X-ray light
       curves from active galaxies", Vaughan et al. (2003)
       https://ui.adsabs.harvard.edu/abs/2003MNRAS.345.1271V
    """

    flux_mean = np.nanmean(flux, axis=axis)
    n_points = np.count_nonzero(~np.isnan(flux), axis=axis)

    s_square = np.nansum((flux - flux_mean) ** 2, axis=axis) / (n_points - 1)
    sig_square = np.nansum(flux_err**2, axis=axis) / n_points
    fvar = np.sqrt(np.abs(s_square - sig_square)) / flux_mean

    sigxserr_a = np.sqrt(2 / n_points) * sig_square / flux_mean**2
    sigxserr_b = np.sqrt(sig_square / n_points) * (2 * fvar / flux_mean)
    sigxserr = np.sqrt(sigxserr_a**2 + sigxserr_b**2)
    fvar_err = sigxserr / (2 * fvar)

    return fvar, fvar_err


def compute_fpp(flux, flux_err, axis=0):
    r"""Calculate the point-to-point excess variance.

    F_pp is a quantity strongly related to the fractional excess variance F_var
    implemented in `~gammapy.stats.compute_fvar`; F_pp probes the variability
    on a shorter timescale.

    For white noise, F_pp and F_var give the same value.
    However, for red noise, F_var will be larger
    than F_pp, as the variations will be larger on longer timescales.

    It is important to note that the errors on the flux must be Gaussian.

    Parameters
    ----------
    flux : `~astropy.units.Quantity`
        the measured fluxes
    flux_err : `~astropy.units.Quantity`
        the error on measured fluxes
    axis : int, optional
        Axis along which the excess variance is computed.
        The default is to compute the value on axis 0.

    Returns
    -------
    fpp, fpp_err : `~numpy.ndarray`
        Point-to-point excess variance.

    References
    ----------
    .. [Edelson2002] "X-Ray Spectral Variability and Rapid Variability
       of the Soft X-Ray Spectrum Seyfert 1 Galaxies
       Arakelian 564 and Ton S180", Edelson et al. (2002), equation 3,
       https://iopscience.iop.org/article/10.1086/323779
    """

    flux_mean = np.nanmean(flux, axis=axis)
    n_points = np.count_nonzero(~np.isnan(flux), axis=axis)
    flux = flux.swapaxes(0, axis).T

    s_square = np.nansum((flux[..., 1:] - flux[..., :-1]) ** 2, axis=-1) / (
        n_points.T - 1
    )
    sig_square = np.nansum(flux_err**2, axis=axis) / n_points
    fpp = np.sqrt(np.abs(s_square.T - sig_square)) / flux_mean

    sigxserr_a = np.sqrt(2 / n_points) * sig_square / flux_mean**2
    sigxserr_b = np.sqrt(sig_square / n_points) * (2 * fpp / flux_mean)
    sigxserr = np.sqrt(sigxserr_a**2 + sigxserr_b**2)
    fpp_err = sigxserr / (2 * fpp)

    return fpp, fpp_err


def compute_chisq(flux):
    r"""Calculate the chi-square test for `LightCurve`.

    Chisquare test is a variability estimator. It computes
    deviations from the expected value here mean value

    Parameters
    ----------
    flux : `~astropy.units.Quantity`
        the measured fluxes

    Returns
    -------
    ChiSq, P-value : tuple of float or `~numpy.ndarray`
        Tuple of Chi-square and P-value
    """
    yexp = np.mean(flux)
    yobs = flux.data
    chi2, pval = stats.chisquare(yobs, yexp)
    return chi2, pval
