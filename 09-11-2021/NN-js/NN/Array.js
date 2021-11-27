Array.prototype.last = function()
{
    return this[this.length - 1];
};

Array.prototype.random = function(length, min, max)
{
    var arr = new Float32Array(length);
    for (var i = 0; i < length; i++)
        arr[i] = Math.random() * (max - min) + min;

    return arr;
}

Array.prototype.sub = function(bArr)
{
    var aArr = this;
    var res = new Float32Array(aArr.length);
    
    for (var i = 0; i < res.length; i++)
        res[i] = aArr[i] - bArr[i];

    return res;
}

Array.prototype.sum = function()
{
    var arr = this;

    var sum = 0;
    for (var i = 0; i < arr.length; i++)
        sum += arr[i];

    return sum;
}

Array.prototype.maxIndex = function()
{
    var arr = this;
    var maxIdx = 0; var maxVal = 0;

    for (var i = 0; i < arr.length; i++)
    {
        if (maxVal < arr[i])
        {
            maxVal = arr[i];
            maxIdx = i;
        }
    }

    return [maxIdx, maxVal];
}