import sqlite3
import gradio as gr
import pandas as pd   

def bigHitters():
    conn = sqlite3.connect('baseball.db')
    cursor = conn.cursor()
    query = """
        WITH bh AS (
            SELECT nameFirst,nameLast,batting.playerID as playerID
            FROM batting inner join people
            on batting.playerID = people.playerID
            WHERE teamID = 'PHI'
            GROUP BY batting.playerID
            ORDER BY sum(HR) desc
            LIMIT 10)
        SELECT nameFirst,nameLast,playerID
        FROM bh
        ORDER BY nameLast desc
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    choices = []
    for record in records:
        name = f"{record[0]} {record[1]}"
        choices.append((name,record[2]))
    return choices

print(bigHitters())




# with gr.Blocks() as iface:
#     dd = gr.Dropdown()


# iface.launch()






