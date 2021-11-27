var canvas;
var context;
var isMouseDown = false;

window.addEventListener('load', e =>
{
  canvas = document.getElementById("canvas");
  context = canvas.getContext("2d");

  context.lineWidth = 2;
  context.strokeStyle = 'white';

  clearCanvas();

  canvas.addEventListener('mousedown', _onMouseDown);
  canvas.addEventListener('mouseup',   _onMouseUp);
  canvas.addEventListener('mouseout',  _onMouseUp);
  canvas.addEventListener('mousemove', _onMouseMove);
});

function registerOnDrawn(action)
{
   canvas = document.getElementById("canvas");
   canvas.addEventListener('mouseup',   action);
   canvas.addEventListener('mouseout',  action);
}

function _getXY(e)
{
   var rW = canvas.clientWidth / canvas.width;
   var rH = canvas.clientHeight / canvas.height;

   var x = (e.clientX - canvas.offsetLeft) / rW;
   var y = (e.clientY - canvas.offsetTop) / rH;
   return [x, y];
}

function _onMouseDown(e) 
{
  isMouseDown = true;
  var [x, y] = _getXY(e);

  context.beginPath();
  context.moveTo(x, y);
}

function _onMouseUp() 
{
   context.closePath();
   isMouseDown = false;
}

function _onMouseMove(e) 
{
  if (isMouseDown == false)
    return; 
 
  var [x, y] = _getXY(e);

  context.lineTo(x, y);
  context.stroke();	
}

function clearCanvas() 
{
   context.clearRect(0, 0, canvas.width, canvas.height);

   context.fillStyle = "black";
   context.fillRect(0, 0, canvas.width, canvas.height); 
}