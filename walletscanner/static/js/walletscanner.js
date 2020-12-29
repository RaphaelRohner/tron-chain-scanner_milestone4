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
            var current_wallet = window.tronWeb && window.tronWeb.defaultAddress.base58
            // Calling Tronlink / sendTrx(to, amount sun, from, options)
            var tx = await tronweb.transactionBuilder.sendTrx('TWFEaFsLiC7EDfgCqjnZKx8gbfNiZftPwT', 1000000, current_wallet)
            var signedTx = await tronweb.trx.sign(tx)
            var broastTx = await tronweb.trx.sendRawTransaction(signedTx)
        }
    }, 10)
}