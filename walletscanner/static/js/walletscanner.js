$(document).ready(function() {
    let tronlink = window.tronWeb && window.tronWeb.defaultAddress.base58;
    $("#send-wallet-to-django").click(function() {
        $.ajax({
            url: "/wallet/",
            type: "POST",
            dataType: "json",
            data: {
                tronlink: tronlink,
                csrfmiddlewaretoken: '{{ csrf_token }}'
                },
            success : function(json) {
                alert("Successfully sent the Wallet to Django");
            },
            error : function(xhr,errmsg,err) {
                alert("Could not send Wallet to Django. Error: " + xhr.status + ": " + xhr.responseText);
            }
        });
    });
});

// FUNCTION TO CHECK IF TRONLINK IS AVAILABLE IN BROWSER
function getTronlink(){
    
    let tronlink = window.tronWeb && window.tronWeb.defaultAddress.base58 // VARIABLE TO TAKE IN WALLET ADDRESS

    if(tronlink){
        $("#trontest").html(`<p>WALLET: ${ tronlink }</p>`); 
    } else {
        $("#trontest").html(`<p>Please sign in to Tronlink and reload page.</p>`);
    }
    return {
        tronlink
    };
}

// FUNCTION TO SUBMIT A DONATION USING GOOGLE CHROME TRONLINK EXTENSION
// FROM: https://developers.tron.network/docs/tronlink-integration
function paymentTronlink(){    
    var obj = setInterval(async ()=>{
        if (window.tronWeb && window.tronWeb.defaultAddress.base58) {
            clearInterval(obj)
            var tronweb = window.tronWeb
            var wallet = window.tronWeb && window.tronWeb.defaultAddress.base58
            var payment = 1000000
            var currency = 'TRX'
            // Calling Tronlink / sendTrx(to, amount sun, from, options)
            var tx = await tronweb.transactionBuilder.sendTrx('TWFEaFsLiC7EDfgCqjnZKx8gbfNiZftPwT', payment, wallet)
            var signedTx = await tronweb.trx.sign(tx)
            var broastTx = await tronweb.trx.sendRawTransaction(signedTx)
            console.log(broastTx);
            
            if (broastTx.result) {
                var paymentTimestamp = Date.now();
                console.log(paymentTimestamp, wallet, payment, currency);
                return {
                    paymentTimestamp: paymentTimestamp,
                    wallet: wallet,
                    payment: payment,
                    currency: currency
                };    
            }           
        }
    }, 10)
}


//var result = paymentTronlink();

//var paymentTimestamp = result.paymentTimestamp
//var wallet = result.wallet;
//var payment = result.payment;
//var currency = result.currency;
//console.log(paymentTimestamp, wallet, payment, currency);