from _typeshed import Incomplete

class Factory:
    filename: Incomplete
    plots: Incomplete
    titles: Incomplete
    lookup: Incomplete
    y_max: Incomplete
    x_max: Incomplete
    offset: int
    precisions: Incomplete
    styles: Incomplete
    widths: Incomplete
    style_parameters: Incomplete
    def __init__(self, filename: str = 'spectrum_plot.html') -> None: ...
    def new_plot(self, precision: str = '5e-6', title: Incomplete | None = None) -> None: ...
    def add(self, data, color=(0, 0, 0), style: str = 'sticks', mz_range: Incomplete | None = None, opacity: float = 0.8, name: Incomplete | None = None, plot_num: int = -1, title: Incomplete | None = None) -> None: ...
    def info(self) -> None: ...
    def get_data(self): ...
    def save(self, filename: Incomplete | None = None, xLimits: Incomplete | None = None) -> None: ...
