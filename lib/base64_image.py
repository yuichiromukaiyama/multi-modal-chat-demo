import base64
from mimetypes import guess_type


def convert(image_path: str) -> str:

    mimetype, _ = guess_type(image_path)
    encoded_image = base64.b64encode(open(image_path, "rb").read()).decode("ascii")

    if mimetype is None:
        mimetype = "application/octet-stream"

    return f"data:{mimetype};base64,{encoded_image}"
