import numpy
import random
from room import Room
from field import Field

field_size = 9
base_field = Field(field_size)

def generation(count=10, size=field_size):
    tmp_field = Field(size)
    tmp_field.place_room(int(size/2),int(size/2))
    for i in range(count):
        random_cell = random.choice(tmp_field.white_list)
        tmp_field.place_room(random_cell[0], random_cell[1])
    return tmp_field


def create_html(field=base_field, size=field_size):
    html = """
    <html><body><div class="aaa"><table>
    """
    print(len(field))
    for y in range(len(field)):
        html += """<tr>"""
        for x in range(len(field[y])):
            html += f"<td onclick=send({y},{x}) class="
            try:
                if field[x][y].is_empty: 
                    if [x, y] in field.white_list: html += "free"
                    else: html += "empty"
                elif field[x][y].is_locked: html += "lock"
                else: html += "used"
            except: html += "empty"
            html += "></td>"

        html += """</tr>"""
    html += """
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    </table></div></body></html>
    <script>
function send(x, y){
$.ajax({
    url: '/test/post',         /* Куда отправить запрос */
    method: 'get',             /* Метод запроса (post или get) */
    dataType: 'html',          /* Тип данных в ответе (xml, json, script, html). */
    data: {x: x,
            y:y
    },     /* Данные передаваемые в массиве */
    success: function(data){ 
        $("html").html(data) /* В переменной data содержится ответ от index.php. */
    }
    });
}
"""
    html += """</script>
    <style>
    table{
        width: 100%;
        height: 100%;
    }
    td {
        border: 1px solid black;
        margin: 1px 1px;
        min-width: """ + f"{100/size}%" + """;
        min-height: """ + f"{100/size}%" + """;
    }
    .free {
        background-color: green;
    }
    .used {
        background-color: blue;
    }
    .lock {
        background-color: red;
    }
    </stile>
    """
    
    return html
