
var startcoords = -1;
var canvas = document.getElementById('mapCanvas');

canvas.addEventListener("mousedown", mousedown, false);
var dragOn = -1;
var mapwidth = -1;
var mapheight = -1;

function getCoord(event) {
    var x = new Number();
    var y = new Number();
    if (event.x != undefined && event.y != undefined)
    {
        x = event.x;
        x = event.y;
    } else {
        x = event.clientX + document.body.scrollLeft + 
            document.documentElement.scrollLeft;
        y = event.clientY + document.body.scrollTop + 
            document.documentElement.scrollTop;
    }

    x -= canvas.offsetLeft;
    y -= canvas.offsetTop;

    x = Math.floor(x/10);
    y = Math.floor(y/10);
    return [x, y];

}

function mousedown(event) {

    var coords = getCoord(event);
    console.log(coords[0] + ', ' + coords[1]);
    startcoords = coords;

    canvas.addEventListener("mousemove", mousemove);
    canvas.addEventListener("mouseup", mouseup);
    return;
}

function mousemove(e) {
}

function mouseup(event) {
    dragOn = -1;
    canvas.removeEventListener("mousemove", mousemove);
    canvas.removeEventListener("mouseup", mouseup);

    var coords = getCoord(event);

    $.get("/solve",
        { sx: startcoords[0], sy: startcoords[1], dx: coords[0], dy: coords[1]},
        function (data) {
            renderPath(data);  
        }
    );
}

/*
 * Create the world button handler 
 */
$("#genbutton").click(function(e) {

    mapwidth = $("select#mapwidth").val();
    mapheight = $("select#mapheight").val();

    $.get("/newmap", 
        { mapwidth: mapwidth, mapheight: mapheight},
        function (data) {
            renderWorld(data);
    });
});

/*
 * Renders the world on the canvas
 */
function renderWorld(data) {
    data = JSON.parse(data);
    var width = data["width"];
    var height = data["height"];
    var mapdata = data["mapdata"];
    var xsize = 10;
    var ysize = 10;
    var ctx = canvas.getContext('2d');
    ctx.fillStyle='#38B0DE';
    ctx.fillRect(0,0, 1000, 400);
    for (var i=0;i<mapdata.length;i++)
    {
        var xcoord = xsize*Math.floor(i % width);
        var ycoord = ysize*Math.floor(i / width);
        if (mapdata[i] == 1) {
            ctx.fillStyle='#38B0DE';
        } else {
            ctx.fillStyle='#215E21';
        }

    ctx.fillRect(xcoord,ycoord,xsize,ysize);
    }


}

/*
 * Renders the path from the start to finish on the canvas
 */
function renderPath(data) {
    data = JSON.parse(data)
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = '#ff0000';
    for (var i=0;i<data.length;i++)
    {
       var xcoord = data[i][0] * 10 
       var ycoord = data[i][1] * 10 
       ctx.fillRect(xcoord,ycoord,10,10);


    }
}

