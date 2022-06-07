"""
@article{bansal_estimation_2011,
	title = {Estimation of depth to the bottom of magnetic sources by a modified centroid method for fractal distribution of sources: {An} application to aeromagnetic data in {Germany}},
	volume = {76},
	url = {https://library.seg.org/doi/full/10.1190/1.3560017},
	doi = {10.1190/1.3560017},
	number = {3},
	journal = {GEOPHYSICS},
	author = {Bansal, A. R. and Gabriel, G. and Dimri, V. P. and Krawczyk, C. M.},
	year = {2011},
	pages = {L11--L22},
}
"""

from .optimise_tanaka import CurieOptimiseTanaka

class CurieOptimiseBansal(CurieOptimiseTanaka):
    def __init__(self, grid, x_0, x_1, y_0, y_1, **kwargs):
        super(CurieOptimiseBansal, self).__init__(grid, x_0, x_1, y_0, y_1)