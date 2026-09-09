"""Prijenosiva konfiguracija JupyterLite izgradnje za razvoj i CI.

JupyterLite automatski skenira ``sys.prefix/share/jupyter/labextensions``.
``jupyter_path("labextensions")`` tu istu putanju na Linuxu vraća i među
standardnim putanjama, pa bi njezino ponovno dodavanje proizvelo dva jednaka
``doit`` zadatka za isti federirani dodatak. Instalacija Pythona iz Microsoft
Storea, s druge strane, može korisničke pakete smjestiti izvan ``sys.prefix``.
Zato ovdje dodajemo samo postojeće, razriješene i jedinstvene korisničke
putanje koje JupyterLite već ne skenira sam.
"""

from pathlib import Path

from jupyter_core.paths import jupyter_path
from jupyterlite_core.addons.federated_extensions import FederatedExtensionAddon


def _path_key(path: Path) -> str:
    """Vrati stabilan ključ putanje i na Windowsu i iza Linux symlinkova."""

    return str(path.expanduser().resolve()).casefold()


def _extra_labextension_paths() -> list[str]:
    """Pronađi samo labextension putanje izvan ugrađenoga ``sys.prefix``."""

    builtin = Path(FederatedExtensionAddon.labextensions_path)
    seen = {_path_key(builtin)}
    extra: list[str] = []

    for raw_path in jupyter_path("labextensions"):
        path = Path(raw_path).expanduser()
        key = _path_key(path)
        if key in seen:
            continue
        seen.add(key)
        if path.is_dir():
            extra.append(str(path.resolve()))

    return extra


c.FederatedExtensionAddon.extra_labextensions_path = (  # type: ignore[name-defined]  # noqa: F821
    _extra_labextension_paths()
)
c.LiteBuildConfig.extra_ignore_lite_config = (  # type: ignore[name-defined]  # noqa: F821
    r"tools[/\\]tmp",
)
