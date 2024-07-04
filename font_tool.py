import os
import subprocess


class UnsupportedFontFormatError(Exception):
    def __init__(self, format_name: str):
        super().__init__(f"Unsupported font format: {format_name}")


def path_exists(path: str) -> bool:
    return os.path.exists(path)


def is_file(path: str) -> bool:
    return os.path.isfile(path)


def convert_font(input_path: str, output_path: str, target_format: str) -> bool:
    """
        Converts a font file to the specified target format using PyFontConverter.

        Args:
            input_path (str): Path to the input font file (TTF or OTF).
            output_path (str): Path where the converted font file will be saved.
            target_format (str): Target format ('woff' or 'woff2').

        Returns:
            bool: True if conversion is successful, False otherwise.
        """
    if not is_file(input_path):
        raise FileExistsError(f"File {input_path} does not exists.")

    if not path_exists(output_path):
        raise NotADirectoryError(f"Output folder {output_path} does not exists.")

    font_formats = ["ttf", "otf", "woff", "woff2"]
    filename, extension = os.path.splitext(os.path.basename(input_path))
    extension = extension[1:].lower()
    target_format = target_format.lower()

    if extension not in font_formats:
        raise UnsupportedFontFormatError(extension)

    if target_format not in font_formats:
        raise UnsupportedFontFormatError(target_format)

    converter_name = {
        "ft_woff": "ft2wf",
        "otf_ttf": "otf2ttf",
        "ttf_otf": "ttf2otf",
        "wf_ft": "wf2ft",
    }

    if extension == "ttf" and target_format == "woff":
        converter_type = converter_name["ft_woff"]
    elif extension == "otf" and target_format == "ttf":
        converter_type = converter_name["otf_ttf"]
    elif extension in ["ttf", "otf"] and target_format in ["woff", "woff2"]:
        converter_type = converter_name["ft_woff"]
    elif extension == "ttf" and target_format == "otf":
        converter_type = converter_name["ttf_otf"]
    elif extension in ["woff", "woff2"] and target_format in ["ttf", "otf"]:
        converter_type = converter_name["wf_ft"]
    else:
        raise ValueError(f"Unsupported conversion: {extension} to {target_format}")

    command = ["font-converter", converter_type, input_path, "-out", output_path]

    try:
        subprocess.run(command)
        return True
    except Exception as e:
        print(f"Error convert {input_path}: {e}")
        return False

