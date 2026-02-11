import gradio as gr

def greet(name, intensity):
    return "Hello world!"

demo = gr.Interface(
    fn=greet,
    inputs=["image"],
    outputs=["text"],
    api_name="predict"
)
a = "dsada" + 22
demo.launch()