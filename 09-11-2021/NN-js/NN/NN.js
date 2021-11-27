function SoftmaxFunction()
{
    this.apply = function(x, derivative = false)
    {
        if (!derivative)
            return Math.exp(x);
        else
            throw 'Softmax function must be used only in the last layer.';
    }

    SoftmaxFunction.prototype.normalize = function(array)
    {
        var sum = array.sum();
        for (var i = 0; i < array.length; i++)
            array[i] /= sum;
    }
}

function ReLuFunction()
{
    this.apply = function(x, derivative = false)
    {
        if (!derivative)
            return Math.max(0, x);
        else
            return x > 0 | 0;
    }
}

function Neuron()
{
    this.W = null;
    this.b = 0;
    this.ActFunc = null;

    var gradW = null;
    var gradB = 0;

    this.create = function(inDim, actFuncName)
    {
        this.W = Array.prototype.random(inDim, -0.5, 0.5);
        this.b = 0;
        switch (actFuncName)
        {
            case 'relu':
                this.ActFunc = new ReLuFunction();
                break;
            case 'softmax':
                this.ActFunc = new SoftmaxFunction();
                break;
            default:
                throw 'Unsupported activation function';
        }   

        gradW = new Float32Array(inDim);
        gradB = 0;
    }

    this.predict = function(x)
    {
        var z = this.b;
        for (var i = 0; i < x.length; i++)
            z += this.W[i] * x[i];

        var a = this.ActFunc.apply(z);
        return a;
    }

    this.updateGradWeights = function(outError, previousActivations)
    {
        for (var i = 0; i < this.W.length; i++)
            gradW[i] += outError * previousActivations[i];

        gradB += outError;
    }

    this.getGradError = function(outError)
    {
        var outErr = new Float32Array(this.W.length);
        for (var i = 0; i < this.W.length; i++)
            outErr[i] = this.W[i] * outError;

        return outErr;
    }

    this.updateWeights = function(factor)
    {
        for (var i = 0; i < this.W.length; i++)
            this.W[i] -= factor * gradW[i];
        
        this.b -= factor * gradB;

        //reset grad
        gradW = new Float32Array(gradW.length);
        gradB = 0;
    }
}

function DenseLayer(inDim, outDim, actFuncName)
{
    this.Neurons = [];
    this.ActFuncName = actFuncName;
    
    create(this, inDim, outDim, actFuncName);

    function create(l, inDim, outDim, actFuncName)
    {
        for (var i = 0; i < outDim; i++)
        {
            var n = new Neuron();
            n.create(inDim, actFuncName);
            l.Neurons.push(n);
        }

        l.ActFuncName = actFuncName;
    }

    this.predict = function(input)
    {
        var a = [];
        for (var i = 0; i < this.Neurons.length; i++)
        {
            var aN = this.Neurons[i].predict(input);
            a[i] = aN;
        }

        if (this.ActFuncName == 'softmax')
            SoftmaxFunction.prototype.normalize(a);

        return a;
    }


    this.updateGradWeights = function(outErrors, previousActivations)
    {
        for (var i = 0; i < this.Neurons.length; i++)
            this.Neurons[i].updateGradWeights(outErrors[i], previousActivations);
    }

    this.calcGradError = function(outErrors, prevActivations, prevLayer)
    {
        var inDim = this.Neurons[0].W.length;
        var outError = new Float32Array(inDim);

        for (var nIdx = 0; nIdx < this.Neurons.length; nIdx++)
        {
            var nOutErr = this.Neurons[nIdx].getGradError(outErrors[nIdx]);
            
            for (var i = 0; i < outError.length; i++)
                outError[i] += nOutErr[i];
        }
         
        for (var i = 0; i < outError.length; i++)
            outError[i] *= prevLayer.Neurons[i].ActFunc.apply(prevActivations[i], true);

        return outError;
    }

    this.updateWeights = function(factor)
    {
        for (var i = 0; i < this.Neurons.length; i++)
            this.Neurons[i].updateWeights(factor);
    }
}

function NN()
{
    this.Layers = [];

    this.add = function(l)
    {
        this.Layers.push(l);
    }

    this.predict = function(sample)
    {
        var activations = [];
        activations.push(sample);

        for (var lIdx = 0; lIdx < this.Layers.length; lIdx++)
        {
             var l = this.Layers[lIdx];
             var a = l.predict(activations.last());
             activations.push(a);   
        }

        return activations.slice(1);
    }

    this.fitEpoch = function(samples, labels, batchSize, learningFactor)
    {
        for (var batch = 0; batch < (samples.length / batchSize); batch++)
        {
            var batchOutputs = []; var batchLabels = [];
            for (var s = 0; s < batchSize; s++)
            {
                var sIdx = (Math.random() * samples.length) | 0;
                var out = this._backpropagate(samples[sIdx], labels[sIdx]);

                batchOutputs.push(out);
                batchLabels.push(labels[sIdx]);
            }
            
            var cost = calcCost(batchOutputs, batchLabels);
            var completed = (batch + 1) / (samples.length / batchSize);
            console.log('Epoch completed: ' + Math.round(completed * 100) + '%. Cost: ' + cost.toFixed(2) + '.');

            for (var lIdx = 0; lIdx < this.Layers.length; lIdx++)
                this.Layers[lIdx].updateWeights(learningFactor / samples.length);
        }
    }

    this._backpropagate = function(sample, label)
    {
        var activations = this.predict(sample);
        var out = activations.last();

        var target = new Float32Array(out.length);
        target[label] = 1;

        //update output W,b
        var outErr = out.sub(target);
        var prevAct = activations[activations.length-1-1];
        this.Layers.last().updateGradWeights(outErr, prevAct);

        //update the rest of W,b
        for (var i = this.Layers.length-1-1; i >= 0; i--)
        {
            outErr = this.Layers[i + 1].calcGradError(outErr, activations[i], this.Layers[i]);
            prevAct = (i == 0) ? sample: activations[i-1];

            this.Layers[i].updateGradWeights(outErr, prevAct);
        }

        return activations.last();
    }

    function calcCost(outputs, labels)
    {
        var cost = 0;
        for (var sIdx = 0; sIdx < labels.length; sIdx++)
        {
            var oSum = outputs[sIdx].sum();
            var o = outputs[sIdx][labels[sIdx]];
            o = Math.log(o / oSum);

            cost += o;        
        }

        return -cost / labels.length;
    }
}

function testAccuracy(nn, samples, labels)
{
    var correctCount = 0;
    for (var sIdx = 0; sIdx < samples.length; sIdx++)
    {
        var a = nn.predict(samples[sIdx]).last();
        var [maxIdx, _] = a.maxIndex();

        if (maxIdx == labels[sIdx])
            correctCount++;
    }

    var testAcc = correctCount / samples.length * 100;
    console.log("-----Test accuracy: " + Math.round(testAcc) + "%.-----");

    return testAcc;
}



NN.prototype.save = function()
{
    //https://stackoverflow.com/questions/19721439/download-json-object-as-a-file-from-browser
    function downloadObjectAsJson(exportObj, exportName)
    {
        var dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(exportObj));
        var downloadAnchorNode = document.createElement('a');
        downloadAnchorNode.setAttribute("href",     dataStr);
        downloadAnchorNode.setAttribute("download", exportName);
        document.body.appendChild(downloadAnchorNode); // required for firefox
        downloadAnchorNode.click();
        downloadAnchorNode.remove();
    }

    //serialize 
    var serializedLayers = [];
    for (var l of this.Layers)
    {
        sl = 
        { 
            outDim: l.Neurons.length, 
            inDim: l.Neurons[0].W.length, 
            actFunc: l.ActFuncName, 
            name: l instanceof DenseLayer ? "dense": "-",
            neurons: []
        }

        for (var n of l.Neurons)
        {
            sn = 
            {
                W: n.W,
                b: n.b
            }

            sl.neurons.push(sn);
        }

        serializedLayers.push(sl);
    } 

    downloadObjectAsJson(serializedLayers, "nn.json");    
}

NN.load = async function(url)
{
    var response = await fetch(url);
    var serializedLayers = await response.json();
    
    var nn = new NN();
    for (var sl of serializedLayers)
    {
        if (sl.name != "dense")
            throw Error("Unsupported layer.");

        l = new DenseLayer(sl.inDim, sl.outDim, sl.actFunc);
        for (var nIdx = 0; nIdx < l.Neurons.length; nIdx++)
        {
            for (var i = 0; i < l.Neurons[nIdx].W.length; i++)
                l.Neurons[nIdx].W[i] = sl.neurons[nIdx].W[i];

            l.Neurons[nIdx].b = sl.neurons[nIdx].b;
        }

        nn.add(l);
    }

    return nn;
}

