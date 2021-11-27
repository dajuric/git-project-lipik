async function fetchMNIST()
{
    async function fetchData(url)
    {
        var data = null; 
        try
        {
            response = await fetch(url);
            if(!response.ok)
                throw new Error('Can not fetch data.');

            return response.arrayBuffer();
        }
        catch(e)
        {
            console.error('There has been a problem with your fetch operation:', e);
        }
    }

    function parseLabels(arrayBuffer)
    {
        var headerView = new DataView(arrayBuffer);
        //var checksum = headerView.getInt32(0, false);
        var numLabels = headerView.getInt32(4, false);

        var dataView = new Uint8Array(arrayBuffer, 8, numLabels);
        return dataView;
    }

    function parseImages(arrayBuffer)
    {
        var headerView = new DataView(arrayBuffer);
        //var checksum = headerView.getInt32(0, false);
        var numImages = headerView.getInt32(4, false);
        var rowCount = headerView.getInt32(8, false);
        var colCount = headerView.getInt32(12, false);

        var images = [];
        for (var i=0; i < numImages; i++)
        {
            var start = 16 + i * rowCount * colCount;
            var imView = new Uint8Array(arrayBuffer, start, rowCount * colCount);

            //convert to [0..1] range
            images[i] = new Float32Array(1 * rowCount * colCount);
            for (var k = 0; k < rowCount * colCount; k++)
                images[i][k] = imView[k] / 255;
        }

        return images;
    }


    var arrBuffL = await fetchData('../data/train-labels-idx1-ubyte');
    var trainLabels = parseLabels(arrBuffL);

    var arrBuffI = await fetchData('../data/train-images-idx3-ubyte');
    var trainImages = parseImages(arrBuffI);

    var arrBuffL = await fetchData('../data/t10k-labels-idx1-ubyte');
    var testLabels = parseLabels(arrBuffL);

    var arrBuffI = await fetchData('../data/t10k-images-idx3-ubyte');
    var testImages = parseImages(arrBuffI);

    return [trainImages, trainLabels, testImages, testLabels];
}

function showPredictionsMNIST(images, predictedLabels, trueLabels, canvas)
{
    const IM_DIM = 28;
    const CELL_MARGIN = 5;
    const FONT_SIZE = 15;

    var rowCount = (canvas.height / (CELL_MARGIN + IM_DIM + FONT_SIZE)) | 0;
    var colCount = (canvas.width  / (CELL_MARGIN + IM_DIM)) | 0;
    var ctx = canvas.getContext("2d");

    for (var imIdx = 0; imIdx < images.length; imIdx++)
    {
        var imgData = ctx.createImageData(IM_DIM, IM_DIM);
        var data = imgData.data;

        for (var i = 0; i < IM_DIM * IM_DIM; i++)
        {
            data[i * 4 + 0] = images[imIdx][i] * 255;
            data[i * 4 + 1] = images[imIdx][i] * 255;
            data[i * 4 + 2] = images[imIdx][i] * 255;
            data[i * 4 + 3] = 255;
        }

        var rIdx = Math.floor(imIdx / colCount) * (CELL_MARGIN + IM_DIM + FONT_SIZE) + CELL_MARGIN;
        var cIdx = Math.floor(imIdx % colCount) * (CELL_MARGIN + IM_DIM) + CELL_MARGIN;
        ctx.putImageData(imgData, cIdx, rIdx);

        ctx.font = `${FONT_SIZE}px Arial`;
        ctx.fillStyle = (predictedLabels[imIdx] == trueLabels[imIdx]) ? "black": "red";
        ctx.fillText(String(predictedLabels[imIdx]), cIdx + (IM_DIM - FONT_SIZE), rIdx + (IM_DIM + FONT_SIZE));
    }
}

function canvasToMNIST(canvasId)
{
    var canvas = document.getElementById(canvasId);
    var ctx = canvas.getContext("2d");
    var data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;

    var mnist = new Float32Array(data.length / 4);
    for(var i=0; i< mnist.length; i++)
        mnist[i] = data[i * 4 + 0] / 255;

    return mnist;
}