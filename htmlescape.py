html_escape_table = {
     "&": "&amp;",
     '"': "&quot;",
     "'": "&apos;",
     ">": "&gt;",
     "<": "&lt;",
     }
 
def htmlesc(text):
    return "".join(html_escape_table.get(c,c) for c in text)