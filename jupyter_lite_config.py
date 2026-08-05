"""Prijenosiva konfiguracija JupyterLite izgradnje za razvoj i CI.

U virtualnom okruženju kernelova se ekstenzija nalazi pod ``sys.prefix`` i
JupyterLite je otkriva automatski. Instalacija Pythona iz Microsoft Storea
može korisničke pakete smjestiti izvan toga prefiksa; zato ovdje eksplicitno
dodajemo sve standardne Jupyter labextension putanje. Ne navodi se nijedna
strojno specifična apsolutna putanja.
"""

from jupyter_core.paths import jupyter_path


c.FederatedExtensionAddon.extra_labextensions_path = jupyter_path(  # type: ignore[name-defined]  # noqa: F821
    "labextensions"
)
c.LiteBuildConfig.extra_ignore_lite_config = (  # type: ignore[name-defined]  # noqa: F821
    r"tools[/\\]tmp",
)
