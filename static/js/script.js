const QuaggaConf = {
    inputStream: {
        target : document.querySelector("#camera"),
        type: "LiveStream",
        constraints: {
            width: { min: 640 },
            height : { min: 480 },
            facingMode : "environment"
        }
    },
    decoder : {
        readers: ['code_128_reader']
    }
};

Quagga.init(QuaggaConf, function(e){
    if (e){
        return console.log(e);
    }
    Quagga.start()
});

Quagga.onDetected(function (result){
    let barcodeValue = result.codeResult.code;
    alert(barcodeValue);
});