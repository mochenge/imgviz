from . import normalize

import numpy as np


class Nchannel2RGB:

    """Convert nchannel array to rgb by PCA."""

    def __init__(self):
        self._pca = None
        self._min_value = None
        self._max_value = None

    def __call__(self, nchannel, dtype=np.uint8):
        import sklearn.decomposition

        assert nchannel.ndim == 3, 'nchannel.ndim must be 2 or 3'
        assert np.issubdtype(nchannel.dtype, np.floating), \
            'nchannel.dtype must be floating'
        H, W, D = nchannel.shape

        if self._min_value is None:
            self._min_value = np.nanmin(nchannel, axis=(0, 1))
        if self._max_value is None:
            self._max_value = np.nanmax(nchannel, axis=(0, 1))
        dst = normalize.normalize(nchannel, self._min_value, self._max_value)

        dst = dst.reshape(-1, D)
        if self._pca is None:
            self._pca = sklearn.decomposition.PCA(n_components=3)
            dst = self._pca.fit_transform(dst)
        else:
            dst = self._pca.transform(dst)
        dst = dst.reshape(H, W, 3)

        if dtype == np.uint8:
            dst = (dst * 255).round().astype(np.uint8)
        else:
            assert np.issubdtype(dtype, np.floating), \
                'dtype must be uint8 or floating'
            dst = dst.astype(dtype)
        return dst


def nchannel2rgb(nchannel, pca=None, min_value=None, max_value=None):
    return Nchannel2RGB()(nchannel)