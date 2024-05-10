import gradio as gr
from lib.base64_image import convert
from lib.openai_call import call
from lib.config import AUTH_USER_ID, AUTH_USER_PW, WEBSITES_PORT


def server(message, _):
    text = message["text"]
    file = None

    if len(message["files"]) > 0:
        file = convert(message["files"][0])

    return call(text, file)


page = gr.ChatInterface(
    server,
    title="マルチモーダルチャット",
    description="検証用",
    multimodal=True,
    css="footer {visibility: hidden}",
).queue()

if __name__ == "__main__":

    if not AUTH_USER_ID:
        page.launch(
            share=False,
            server_port=WEBSITES_PORT,
            server_name="0.0.0.0",
        )
    else:
        page.launch(
            share=False,
            auth=(AUTH_USER_ID, AUTH_USER_PW),
            server_port=WEBSITES_PORT,
            server_name="0.0.0.0",
        )
