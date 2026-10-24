#!/usr/bin/env bash
# Launch with the isolated prefix and graphics configuration used for testing.
# The prefix must already contain the x64 DXVK 3.1 d3d11.dll and dxgi.dll.
set -euo pipefail
if [[ $# -ne 2 ]]; then
    echo "Usage: $0 /absolute/path/to/wine-prefix /absolute/path/to/virtualdj.exe" >&2
    exit 2
fi
prefix=$(realpath -e -- "$1")
executable=$(realpath -e -- "$2")
[[ -d "$prefix/drive_c" && -f "$executable" ]] || exit 2
for dll in d3d11 dxgi; do
    if [[ ! -f "$prefix/drive_c/windows/system32/$dll.dll" ]]; then
        echo "Missing $dll.dll in prefix; install x64 DXVK 3.1 first." >&2
        exit 2
    fi
done
export WINEPREFIX="$prefix"
export WINEDEBUG=-all
export WINEDLLOVERRIDES='mscoree,mshtml=;d3d11,dxgi=n'
export DXVK_LOG_LEVEL=warn
cd -- "$(dirname -- "$executable")"
exec wine "$executable"
