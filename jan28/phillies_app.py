import sqlite3
import gradio as gr 
import pandas as pd  

def fetch_phillies():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT playerID
        FROM batting
        WHERE teamID = 'PHI' AND yearID = 1976
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    players = []
    for record in records:
        players.append(record[0])
    return players

def f(player):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT HR
        FROM batting
        WHERE yearID = 1976 AND teamID = 'PHI' AND playerID = ?
    """
    cursor.execute(query,[player])
    records = cursor.fetchall()
    conn.close()
    return records[0][0]


with gr.Blocks() as iface:
    phillies_dd = gr.Dropdown(fetch_phillies(),interactive = True,value = None,label = "Select a Phillie")
    HRbox = gr.Number(label = "Homerun Total")
    phillies_dd.change(fn = f, inputs = [phillies_dd], outputs = [HRbox])

iface.launch()

