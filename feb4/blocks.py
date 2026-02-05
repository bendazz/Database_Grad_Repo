import gradio as gr 

def f(x,y):
    return x+y


with gr.Blocks() as iface:
    with gr.Row():
        with gr.Column():
            xbox = gr.Number(label = "Type in a number")
            ybox = gr.Number(label = "Type in another number")            
        with gr.Column():
            sumbox = gr.Number(label = "This is the sum of these numbers")
            

    xbox.change(fn = f,inputs = [xbox,ybox],outputs = [sumbox])
    ybox.change(fn = f,inputs = [xbox,ybox],outputs = [sumbox])
    

iface.launch()