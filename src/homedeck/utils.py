import os
import shutil
import subprocess
import zipfile
from typing import Union

from .enums import ButtonElementAction

HAS_OPTIPNG = shutil.which('optipng') is not None


def normalize_tuple(offset):
    if isinstance(offset, tuple):
        return offset

    if isinstance(offset, int):
        return (offset, offset)

    if isinstance(offset, str):
        try:
            tmp = offset.split(' ')
            return (int(tmp[0]), int(tmp[1]))
        except Exception:
            pass

    return (0, 0)


def normalize_hex_color(color: Union[str, int]):
    if not color:
        return None

    color = str(color)

    # Remove '/' prefix
    if color.startswith('/'):
        color = color[1:]

    # Padding
    color = color.ljust(6, '0')

    return color.upper()


def hex_to_rgb(hex_color: str, alpha=None):
    hex_color = normalize_hex_color(hex_color)
    r, g, b = [int(hex_color[i:i + 2], 16) for i in (0, 2, 4)]

    if alpha is not None:
        return (r, g, b, alpha)

    return (r, g, b)


def deep_merge(base: dict, override: dict, *, allow_none=False):
    for key, value in override.items():
        if key not in base:
            base[key] = value
        elif isinstance(base[key], dict) and isinstance(value, dict):
            base[key] = deep_merge(base[key], value)
        elif allow_none or value is not None:
            base[key] = value

    return base


def apply_presets(*, source: dict, presets_config={}):
    if presets_config is None or not isinstance(source, dict):
        return source

    # Save a set of applied presets to avoid infinite loop
    applied_presets = set()

    output = source
    while True:
        output.setdefault('presets', [])
        preset_list = output['presets']
        del output['presets']
        if not preset_list:
            break

        if not isinstance(preset_list, list):
            preset_list = [preset_list]

        # Loop through presets, reversed
        merged_data = {}
        for preset_name in reversed(preset_list):
            if preset_name in applied_presets:
                continue

            applied_presets.add(preset_name)

            preset_data = presets_config.get(preset_name, None)
            if not preset_data:
                continue

            # Loop through preset_data
            for key, value in preset_data.items():
                if key not in merged_data:
                    merged_data[key] = value
                elif isinstance(value, dict):
                    merged_data[key] = deep_merge(merged_data[key], value)

        output = deep_merge(merged_data, output, allow_none=True)

    return output


def compress_folder(folder_path, output_zip, compress_level=0):
    method = zipfile.ZIP_STORED if compress_level == 0 else zipfile.ZIP_DEFLATED
    with zipfile.ZipFile(output_zip, 'w', method, compresslevel=compress_level) as zipf:
        # Write dummy.txt at the beginning of the zip file
        dummy_path = os.path.join(folder_path, 'dummy.txt')
        if (os.path.exists(dummy_path)):
            zipf.write(dummy_path, os.path.relpath(dummy_path, folder_path))

        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path == dummy_path:
                    # Don't write dummy file again
                    continue

                arcname = os.path.relpath(file_path, folder_path)  # Preserve folder structure
                zipf.write(file_path, arcname)


def optimize_image(file_path, optimize_level=2):
    if not HAS_OPTIPNG:
        return

    try:
        subprocess.run(['optipng', f'-o{optimize_level}', file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except Exception as e:
        print(e)


def normalize_button_positions(positions: dict):
    ''' convert "$page.next" to enum("$page.next") '''
    keys = list(positions.keys())
    for key in keys:
        positions[ButtonElementAction(key)] = positions[key]
        del positions[key]

    return positions
