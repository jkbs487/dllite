is_simple_core = False

if is_simple_core:
    from dllite.core_simple import Variable
    from dllite.core_simple import Function
    from dllite.core_simple import using_config
    from dllite.core_simple import no_grid
    from dllite.core_simple import as_array
    from dllite.core_simple import as_variable
    from dllite.core_simple import setup_variable
else:
    from dllite.core import Variable
    from dllite.core import Function
    from dllite.core import using_config
    from dllite.core import no_grid
    from dllite.core import as_array
    from dllite.core import as_variable
    from dllite.core import setup_variable
    from dllite.core import test_mode
    from dllite.core import Parameter
    from dllite.layers import Layer
    from dllite.models import Model
    from dllite.dataloaders import DataLoader
    from dllite.core import Config

setup_variable()