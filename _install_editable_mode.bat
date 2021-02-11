@pushd %~dp0
py -3.6 -m pip install -e .
@popd

@IF "%1" NEQ "SILENT" (
    PAUSE
)
