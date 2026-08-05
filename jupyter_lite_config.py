"""Prijenosiva konfiguracija JupyterLite izgradnje za razvoj i CI.

U virtualnom okruženju kernelova se ekstenzija nalazi pod ``sys.prefix`` i
JupyterLite je otkriva automatski. Instalacija Pythona iz Microsoft Storea
može korisničke pakete smjestiti izvan toga prefiksa; zato ovdje eksplicitno
dodajemo standardne Jupyter labextension putanje koje nisu već pokrivene
``sys.prefix``-om. Time se sprječava dvostruka registracija ekstenzija (npr.
``jupyterlab_pygments``) na okruženjima gdje su paketi instalirani i u
korisničkom direktoriju i u virtualnom okruženju. Ne navodi se nijedna
strojno specifična apsolutna putanja.
"""

import sys
from pathlib import Path

from jupyter_core.paths import jupyter_path

_SHARE_LABEXTENSIONS = Path("share") / "jupyter" / "labextensions"
_sys_prefix_labextensions = Path(sys.prefix) / _SHARE_LABEXTENSIONS

c.FederatedExtensionAddon.extra_labextensions_path = [  # type: ignore[name-defined]  # noqa: F821
    p
    for p in jupyter_path("labextensions")
    if Path(p) != _sys_prefix_labextensions
]
c.LiteBuildConfig.extra_ignore_lite_config = (  # type: ignore[name-defined]  # noqa: F821
    r"tools[/\\]tmp",
)
